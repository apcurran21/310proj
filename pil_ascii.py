"""
Transforms a given image into an ASCII-art version of itself.

Daniel Vandersand, Evan Waite, Andy Curran
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import json
import base64

UPLOADED_IMG_DIR = Path("uploaded")
OUTPUT_IMG_DIR = Path("ouput")
UPLOADED_IMG = "images-owls-png-hd-owl-free-download-png-png-image-485.png"
OUTPUT_IMG_PREFIX = "transformed";


img = Image.open(str(UPLOADED_IMG_DIR.joinpath(UPLOADED_IMG)))


# Resize the image to reduce the number of pixels and therefore the number of ASCII
width, height = img.size
print(f"input image dims: width={width}, height={height}")
aspect_ratio = height/width
new_width = 100
new_height = int(aspect_ratio * new_width * 0.55)  # 0.55 is an adjustment factor to account for the aspect ratio of characters
resized_image = img.resize((new_width, new_height))
# img.show()
print("showed regular img")
# resized_image.show()

# Convert the image to grayscale
grayscale_image = resized_image.convert("L")
# grayscale_image.show()
print("showed scaled gray image")

# Define the ASCII characters to represent different intensity levels
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Convert each pixel to an ASCII character based on its intensity level
ascii_art = ""
pixels = grayscale_image.getdata()
for pixel_value in pixels:
    ascii_art += ASCII_CHARS[pixel_value // 25]  # 25 is used to divide the grayscale intensity into 10 levels

# Reshape the ASCII art string to match the width of the image
# ascii_art = "\n".join([ascii_art[index:index+new_width] for index in range(0, len(ascii_art), new_width)])
ascii_art = "".join([ascii_art[index:index+new_width] for index in range(0, len(ascii_art), new_width)])
print(f"ascii_art has {len(ascii_art)} characters")

# print(ascii_art)

### convert the string into an image file
font = ImageFont.load_default()
# If you want to use a different font, use ImageFont.truetype
# font = ImageFont.truetype("arial.ttf", 12)

char_width, char_height = font.getbbox('@')[2:4]  # Using getbbox to get the width and height of a character, assume all chars are the same size
print()
print(f"char dims: width={char_width}, height={char_height}")
print(f"input image dims: width={width}, height={height}")
image_width = char_width * width
image_height = char_height * height
print(f"output image dims: width={image_width}, height={image_height}")
print(f"output image dims: width={char_width * width}, height={char_height * height}")
print(f"shrunk output image dims: width={new_width}, height={new_height}")

# Create a new blank image with white background
image = Image.new('RGB', (image_width, image_height), color='white')
draw = ImageDraw.Draw(image)

# Draw the ASCII characters onto the image
for y, row in enumerate(ascii_art):
    for x, char in enumerate(row):
        draw.text((x * char_width, y * char_height), char, fill='black', font=font)

# Print or save the ASCII art
# print(ascii_art)
image.show()
