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

# Need to resize to prevent image size from blowing up
width, height = img.size
aspect_ratio = height/width
new_width = 100     # hardcoded lol, its just a reasonable size
new_height = int(aspect_ratio * new_width * 0.55)  # hardcode 0.55 to account for general aspect ratio of pixel characters.
resized_image = img.resize((new_width, new_height))

grayscale_image = resized_image.convert("L")

# Hardcode characters, they represent different pixel intensities (choose 10 for simplicity)
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

ascii_art = ""
pixels = grayscale_image.getdata()
for pixel_value in pixels:
    ascii_art += ASCII_CHARS[pixel_value // 25]     # need 25 to agree w/ the number of intensities

ascii_art = "".join([ascii_art[index:index+new_width] for index in range(0, len(ascii_art), new_width)])

font = ImageFont.load_default()

char_width, char_height = font.getbbox('@')[2:4]  # using getbbox to get the width and height of a character, assume all chars are the same size
image_width = char_width * new_width
image_height = char_height * new_height

image = Image.new('RGB', (image_width, image_height), color='white')
draw = ImageDraw.Draw(image)

for y in range(new_height):
    for x in range(new_width):
        index = y * new_width + x
        char = ascii_art[index]

        draw_x = x * char_width
        draw_y = y * char_height

        draw.text((draw_x, draw_y), char, fill='black')


image.show()
