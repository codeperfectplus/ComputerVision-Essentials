""" Image filters using Keras and tensorflow """
import numpy as np
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import Model
from matplotlib import pyplot as plt

model = VGG16()
model = Model(input=model.input, outputs=model.layers[1].output)
model.summary()

img = load_img("./Media/face-001.jpg")
img = img_to_array(img)
img = np.expand_dims(img, asix=0)
img = preprocess_input(img)
feature_map = model.predict(img)

square = 8
i = 1
for _ in range(square):
    for _ in range(square):
        ax = plt.subplot(square, square, i)
        ax.set_xticks([])
        ax.set_yticks([])
        plt.imshow(feature_map[0, :, :, i-1], cmap='gray')
        i += 1
plt.show()