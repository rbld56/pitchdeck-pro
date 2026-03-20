#!/usr/bin/env python3
"""Generate images via Black Forest Labs FLUX.2 API.

Requires:
    pip install requests
    export BFL_API_KEY=your_key_here

Usage:
    python generate-image-flux.py --prompt "modern hospital corridor" --model pro --output visual.png
    python generate-image-flux.py --prompt "abstract pattern" --model schnell --width 1920 --height 1080 --output bg.png
"""

import argparse
import os
import sys
import time
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: requests package not installed.", file=sys.stderr)
    print("Install with: pip install requests", file=sys.stderr)
    sys.exit(1)


BFL_API_BASE = "https://api.bfl.ml/v1"

MODEL_MAP = {
    "pro": "flux-pro-1.1",
    "dev": "flux-dev",
    "schnell": "flux-schnell",
}


def submit_generation(api_key: str, prompt: str, model: str, width: int, height: int) -> str:
    """Submit an image generation request and return the task ID."""
    model_id = MODEL_MAP.get(model)
    if not model_id:
        print(f"Error: Unknown model '{model}'. Choose from: {', '.join(MODEL_MAP.keys())}", file=sys.stderr)
        sys.exit(1)

    endpoint = f"{BFL_API_BASE}/{model_id}"
    headers = {
        "X-Key": api_key,
        "Content-Type": "application/json",
    }
    payload = {
        "prompt": prompt,
        "width": width,
        "height": height,
    }

    response = requests.post(endpoint, json=payload, headers=headers, timeout=30)
    if response.status_code != 200:
        print(f"Error: API request failed ({response.status_code}): {response.text}", file=sys.stderr)
        sys.exit(1)

    data = response.json()
    task_id = data.get("id")
    if not task_id:
        print(f"Error: No task ID in response: {data}", file=sys.stderr)
        sys.exit(1)

    return task_id


def poll_result(api_key: str, task_id: str, max_wait: int = 120) -> str:
    """Poll for task completion and return the result image URL."""
    headers = {"X-Key": api_key}
    endpoint = f"{BFL_API_BASE}/get_result"

    start_time = time.time()
    while time.time() - start_time < max_wait:
        try:
            response = requests.get(endpoint, params={"id": task_id}, headers=headers, timeout=30)
        except requests.RequestException as e:
            print(f"  Warning: Request error during polling: {e}", file=sys.stderr)
            time.sleep(3)
            continue

        if response.status_code in (429, 500, 502, 503, 504):
            retries = getattr(poll_result, '_retries', 0) + 1
            if retries > 3:
                print(f"Error: Polling failed after 3 retries ({response.status_code})", file=sys.stderr)
                sys.exit(1)
            poll_result._retries = retries
            wait = min(3 * retries, 10)
            print(f"  Warning: {response.status_code} — retrying in {wait}s (attempt {retries}/3)...")
            time.sleep(wait)
            continue

        if response.status_code != 200:
            print(f"Error: Poll request failed ({response.status_code}): {response.text}", file=sys.stderr)
            sys.exit(1)

        data = response.json()
        status = data.get("status")

        if status == "Ready":
            result = data.get("result", {})
            image_url = result.get("sample") if isinstance(result, dict) else None
            if not image_url:
                print(f"Error: No image URL in result: {data}", file=sys.stderr)
                sys.exit(1)
            return image_url

        if status in ("Error", "Request Moderated", "Content Moderated"):
            print(f"Error: Generation failed with status '{status}': {data}", file=sys.stderr)
            sys.exit(1)

        # Still pending
        elapsed = int(time.time() - start_time)
        print(f"  Status: {status} ({elapsed}s elapsed)...")
        time.sleep(2)

    print(f"Error: Timed out after {max_wait}s waiting for generation.", file=sys.stderr)
    sys.exit(1)


def download_image(url: str, output_path: Path):
    """Download the generated image to the output path."""
    response = requests.get(url, timeout=60)
    if response.status_code != 200:
        print(f"Error: Failed to download image ({response.status_code})", file=sys.stderr)
        sys.exit(1)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(response.content)


def main():
    parser = argparse.ArgumentParser(description="Generate images via FLUX.2 (Black Forest Labs API)")
    parser.add_argument("--prompt", required=True, help="Image generation prompt")
    parser.add_argument("--output", required=True, help="Output file path (PNG)")
    parser.add_argument("--model", default="pro", choices=["pro", "dev", "schnell"], help="Model tier (default: pro)")
    parser.add_argument("--width", type=int, default=1920, help="Image width in pixels (default: 1920)")
    parser.add_argument("--height", type=int, default=1080, help="Image height in pixels (default: 1080)")
    args = parser.parse_args()

    api_key = os.environ.get("BFL_API_KEY")
    if not api_key:
        print("Error: BFL_API_KEY environment variable not set.", file=sys.stderr)
        print("Get your key at https://docs.bfl.ai/", file=sys.stderr)
        sys.exit(1)

    model_id = MODEL_MAP[args.model]
    print(f"Generating image with FLUX.2 ({model_id})...")
    print(f"  Prompt: {args.prompt[:80]}...")
    print(f"  Size: {args.width}x{args.height}")

    task_id = submit_generation(api_key, args.prompt, args.model, args.width, args.height)
    print(f"  Task submitted: {task_id}")

    image_url = poll_result(api_key, task_id)
    print(f"  Generation complete. Downloading...")

    output_path = Path(args.output)
    download_image(image_url, output_path)
    print(f"Image saved to: {output_path}")


if __name__ == "__main__":
    main()
