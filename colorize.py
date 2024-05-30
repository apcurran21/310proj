"""
Colorizes black and white png images using the OpenCV deep neural network framework.
Inspired by https://pyimagesearch.com/2019/02/25/black-and-white-image-colorization-with-opencv-and-deep-learning/

Daniel Vandersand, Evan Waite, Andy Curran
"""

# required packages
# Note - how do we manage package versions?
from pathlib import path
import json
import base64
import numpy as np
import cv2

# 