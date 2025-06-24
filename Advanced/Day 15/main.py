# Coding With Kien - 365 Days of Python Programming
# Advanced - Day 15

# Image Watermarking Tool
# This script requires 'Pillow' and 'requests':
# pip install Pillow requests

from PIL import Image, ImageDraw, ImageFont
import requests
import os

def create_dummy_image(filename="source_image.jpg"):
    """Creates a placeholder image to work with."""
    try:
        url = "https://picsum.photos/800/600"
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Dummy image downloaded as {filename}")
        return filename
    except requests.exceptions.RequestException as e:
        print(f"Could not download dummy image: {e}")
        return None

def watermark_image(input_image_path, output_image_path, watermark_text):
    """
    Adds a text watermark to an image.
    """
    if not os.path.exists(input_image_path):
        print(f"Error: Input image '{input_image_path}' not found.")
        return

    try:
        original_image = Image.open(input_image_path).convert("RGBA")
        
        # Create a transparent layer for the text
        txt_layer = Image.new("RGBA", original_image.size, (255, 255, 255, 0))
        
        # Setup font
        try:
            # Try to use a common font
            font = ImageFont.truetype("arial.ttf", 50)
        except IOError:
            # If not found, use a default font
            font = ImageFont.load_default()
            print("Arial font not found, using default font.")

        # Setup drawing context
        draw = ImageDraw.Draw(txt_layer)
        
        # Position for the text (bottom right corner)
        text_width, text_height = draw.textsize(watermark_text, font=font)
        x = original_image.width - text_width - 10
        y = original_image.height - text_height - 10
        
        # Draw the text with transparency
        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128)) # White, semi-transparent
        
        # Combine the original image with the text layer
        watermarked_image = Image.alpha_composite(original_image, txt_layer)
        
        # Save the result as a PNG to preserve transparency, or convert back to RGB for JPG
        watermarked_image = watermarked_image.convert("RGB")
        watermarked_image.save(output_image_path)
        
        print(f"Watermark added. Image saved as {output_image_path}")

    except Exception as e:
        print(f"An error occurred during watermarking: {e}")


# --- Example Usage ---
source_image = create_dummy_image()
if source_image:
    output_image = "watermarked_image.jpg"
    watermark = "© 365 Days of Python"
    watermark_image(source_image, output_image, watermark) 