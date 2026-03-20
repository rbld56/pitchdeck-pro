#!/usr/bin/env python3
"""Generate images via Gemini 3.1 Flash Image Preview (Nano Banana 2).

Requires:
    pip install google-genai
    export GEMINI_API_KEY=your_key_here

Usage:
    python generate-image-nanobanana.py --prompt "abstract AI visualization" --output hero.png
    python generate-image-nanobanana.py --prompt "style like reference" --reference-image ref.png --output out.png
"""

import argparse
import base64
import os
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Generate images via Gemini 3.1 Flash Image Preview")
    parser.add_argument("--prompt", required=True, help="Image generation prompt")
    parser.add_argument("--output", required=True, help="Output file path (PNG)")
    parser.add_argument("--reference-image", action="append", default=[], help="Reference image path (can be specified multiple times, up to 14)")
    parser.add_argument("--aspect-ratio", default="16:9", choices=["16:9", "1:1", "4:3", "9:16"], help="Aspect ratio (default: 16:9)")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.", file=sys.stderr)
        print("Get your key at https://aistudio.google.com/", file=sys.stderr)
        sys.exit(1)

    if len(args.reference_image) > 14:
        print("Error: Maximum 14 reference images supported.", file=sys.stderr)
        sys.exit(1)

    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("Error: google-genai package not installed.", file=sys.stderr)
        print("Install with: pip install google-genai", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    # Build content parts: reference images first, then text prompt
    contents = []

    for ref_path in args.reference_image:
        ref_file = Path(ref_path)
        if not ref_file.exists():
            print(f"Error: Reference image not found: {ref_path}", file=sys.stderr)
            sys.exit(1)

        suffix = ref_file.suffix.lower()
        mime_map = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}
        mime_type = mime_map.get(suffix, "image/png")

        image_data = ref_file.read_bytes()
        contents.append(types.Part.from_bytes(data=image_data, mime_type=mime_type))

    contents.append(args.prompt)

    # Configure generation for image output
    generation_config = types.GenerateContentConfig(
        response_modalities=["IMAGE", "TEXT"],
        temperature=1.0,
    )

    print(f"Generating image with prompt: {args.prompt[:80]}...")
    response = client.models.generate_content(
        model="gemini-2.0-flash-preview-image-generation",
        contents=contents,
        config=generation_config,
    )

    # Extract image from response
    image_saved = False
    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(part.inline_data.data)
            print(f"Image saved to: {output_path}")
            image_saved = True
            break
        elif part.text is not None:
            print(f"Model response: {part.text}")

    if not image_saved:
        print("Error: No image was generated. The model returned text only.", file=sys.stderr)
        print("Try a more specific prompt or adjust the request.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
