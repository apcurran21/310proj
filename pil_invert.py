"""
Inverts the colors of png images, with other color channel effects potentially.

Daniel Vandersand, Evan Waite, Andy Curran
"""

# import PIL as p
from PIL import Image, ImageOps
from pathlib import Path
import json
import base64

UPLOADED_IMG_DIR = Path("uploaded")
UPLOADED_IMG = "images-owls-png-hd-owl-free-download-png-png-image-485.png"


img = Image.open(str(UPLOADED_IMG_DIR.joinpath(UPLOADED_IMG)))
# img likely has an alpha channel if it's a png, so convert to RGB
img_rgb = img.convert("RGB")
inv = ImageOps.invert(img_rgb)
inv.show()


# save the image locally
# r.save('foo.png')

# we would likely b64 encode and send in the body of a json
