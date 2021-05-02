""" Image Encoding and decoding using base64 """

import base64

image = open('./Media/apple.jpeg', 'rb')
image_read = image.read()

image_64_encode = base64.encodebytes(image_read)
print(image_64_encode)

image_64_decode = base64.decodebytes(image_64_encode)
image_result = open('./Media/apple.png', 'wb')
image_result.write(image_64_decode)