"""
Transforms an image into a black and white version, allows for a specific dithering level.

Daniel Vandersand, Evan Waite, Andy Curran
"""

from PIL import Image
from pathlib import Path
import json
import base64

UPLOADED_IMG_DIR = Path("uploaded")
OUTPUT_IMG_DIR = Path("ouput")
UPLOADED_IMG = "images-owls-png-hd-owl-free-download-png-png-image-485.png"
OUTPUT_IMG_PREFIX = "transformed";

# different image functions & dictionary to store them
thresh = 100
binary = lambda x : 255 if x > thresh else 0
identity = lambda x : x

img_fns = {
    'binary' : binary,
    'identity' : identity
}

# read image file from disk
img = Image.open(str(UPLOADED_IMG_DIR.joinpath(UPLOADED_IMG)))

# do the simplest conversion (produces a range of black and white)
bw = img.convert('L')

# save the file to disk
bw.save(str(OUTPUT_IMG_DIR.joinpath(OUTPUT_IMG_PREFIX + '.jpg')))
















#########################################
## EXTRA IGNORE
#########################################


# # Increase contrast
# enhancer = ImageEnhance.Contrast(img)
# enhanced_img = enhancer.enhance(2.0)  # Increase contrast by a factor of 2
# enhanced_img.show()

### TESTING ###
###############

# img.show()

# bw = img.convert('L').point(img_fns['identity'], mode='1')
# bw = img.convert('L')   # uses L = R * 299/1000 + G * 587/1000 + B * 114/1000 for the intensities

# bw.show()

# thresh = 80
# bw = img.convert('L').point(img_fns['binary'], mode='1')

# bw.show()

# bw_with_dithering = img.convert("1", dither=Image.FLOYDSTEINBERG)

# bw.show()

### Save image and convert for sending to client ###
####################################################
### THIS IS ALL EXAMPLE CODE FROM OTHER 310 PROJS


# # NOTE - the client should be responsible for sending a readable filename, and a unique filename for storage in S3 

# # plan is to just save the PIL Image as a png file, reread the bytes, then send those after encoding.
# bw.save()
# data = open('x.jpg','rb').read()
# data = base64.b64encode(data).decode("utf8")
# r = requests.post('url',data=data)


# base64_bytes = datastr.encode()        # string -> base64 bytes
# bytes = base64.b64decode(base64_bytes) # base64 bytes -> raw bytes

# #
# # write raw bytes to local filesystem for upload:
# #
# print("**Writing local data file**")
# #
# # TODO #1 of 3: what directory do we write to locally?
# # Then open this local file for writing a binary file,
# # write the bytes we received from the client, and
# # close the file.

# # code to write a bytes object to disk (used in the lambda function to write bytes objects)
# # -NOTE actually i don't think we will actually use this, we can save the augmented PIL Image object
# # to disk directly as a jpg. So we would only have to read this file to convert to bytes and send back
# # to the client
# local_filename = "/tmp/data.pdf"
# file= open(local_filename, 'wb')
# file.write(bytes)
# file.close()

# #
# # generate unique filename (used in the lambda function to assign a unique name for S3)
# #
# print("**Uploading local file to S3**")

# basename = pathlib.Path(filename).stem
# extension = pathlib.Path(filename).suffix

# if extension != ".pdf" : 
#     raise Exception("expecting filename to have .pdf extension")

# bucketkey = "benfordapp/" + username + "/" + basename + "-" + str(uuid.uuid4()) + ".pdf"

# print("S3 bucketkey:", bucketkey)


# # code to open a file as a bytes object (used in the lambda function to send an image back to the client)
# infile = open(local_filename, "rb")
# bytes = infile.read()
# infile.close()

# #
# # now encode the pdf as base64. Note b64encode returns
# # a bytes object, not a string. So then we have to convert
# # (decode) the bytes -> string, and then we can serialize
# # the string as JSON for upload to server:
# #
# data = base64.b64encode(bytes)
# datastr = data.decode()

# data = {"filename": local_filename, "data": datastr}

# #
# # call the web service:
# #
# api = '/pdf'
# url = baseurl + api + "/" + userid

# res = requests.post(url, json=data)