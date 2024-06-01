"""
Inverts the colors of png images, with other color channel effects potentially.

Daniel Vandersand, Evan Waite, Andy Curran
"""

# import PIL as p
from PIL import Image, ImageOps
from pathlib import Path
import json
import base64

INPUT_IMG = "/tmp/input.jpg"
OUTPUT_IMG = "/tmp/output.jpg"


img = Image.open(INPUT_IMG)
# img likely has an alpha channel if it's a png/jpg, so convert to RGB
img_rgb = img.convert("RGB")
inv = ImageOps.invert(img_rgb)
inv.show()


# save the image locally
# r.save('foo.png')

# we would likely b64 encode and send in the body of a json
