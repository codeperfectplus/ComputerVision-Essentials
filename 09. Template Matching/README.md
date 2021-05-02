## Template Matching

Template Matching is a method for searching and finding the location of a template image in a larger image.
OpenCV comes with a function cv2.matchTemplate() for this purpose. It simply slides the template image over the input
image (as in 2D convolution) and compares the template and patch of input image under the template image.

