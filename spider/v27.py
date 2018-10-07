import pytesseract as pt

from PIL import Image

image = Image.open("/Users/liuwenbing/Desktop/timg.png")

test = pt.image_to_string(image)

print(test)
