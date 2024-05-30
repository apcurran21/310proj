"""
Inverts the colors of png images, with other color channel effects potentially.

Daniel Vandersand, Evan Waite, Andy Curran
"""

# required packages
# Note - how do we manage package versions?
from pathlib import Path
import json
import base64
import numpy as np
import cv2

# Constants
# File locations, naming conventions, etc.
UPLOADED_IMG_DIR = Path("uploaded")
# UPLOADED_IMG = "img.png"
UPLOADED_IMG = "images-owls-png-hd-owl-free-download-png-png-image-485.png"

# simple inversion function, expects 0-255 pixel intensities
def invert(img: np.ndarray):
    return 255 - img

# handler for the incoming image data
# Note - if we decide to offer more color functionality, we could just pass
# in another int argument to select the image effect.
def handle_img():
    img = cv2.imread(str(UPLOADED_IMG_DIR.joinpath(UPLOADED_IMG)))
    inverted_img =  invert(img)
    cv2.imshow(img)

handle_img()