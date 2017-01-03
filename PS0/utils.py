import cv2
import numpy as np

"""
Method to show image and wait for key value 0 input
@param image: the image to show
"""
def showAndWait(image):
	cv2.imshow('image',image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

"""
Method to get monochromes of the red green and blue
channels of an image

@param image: the image to get the monochromes from

@return three numpy arrays representing monochrome images of
the red,green, and blue channels of the image respectively
"""
def getRGBMonochromes(image):
	length =  image.shape[0];
	width =  image.shape[1];
	green = np.zeros((length,width,3),dtype=image.dtype)
	red = np.zeros((length,width,3),dtype=image.dtype)
	blue = np.zeros((length,width,3),dtype=image.dtype)
	green[0:length,0:width,1] =  image[0:length,0:width,1]
	red[0:length,0:width,2] = image[0:length,0:width,2]
	blue[0:length,0:width,0] = image[0:length,0:width,0]
	green = cv2.cvtColor(green, cv2.COLOR_BGR2GRAY)
	red = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY)
	blue = cv2.cvtColor(blue, cv2.COLOR_BGR2GRAY)
	return red,green,blue
