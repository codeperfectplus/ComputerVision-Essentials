""" Instance Segmentation using PixelLib and Mask_Rcnn Pretained model on coco dataset """

import pixellib
from PIL import Image
from pixellib.instance import instance_segmentation

model_path = "./assets/mask_rcnn_coco.h5"
image_path = "./Media/road.jpg"
image_output = './media/road_segmentation.jpg'

# creating instace 
segment_image = instance_segmentation()
segment_image.load_model(model_path)

# applying semantic segmentation
segment_image.segmentImage(image_path, show_bboxes = True, output_image_name=image_output)

# showing the output
img = Image.open(image_output)
img.show()
