#Josh Miller
#6/8/16
#Answers to question 5 of Problem set zero
import cv2
import numpy as np
#Read in our image
img = cv2.imread('img1.png');
#Did this basically for the sake of convenience
l = img.shape[0];
w = img.shape[1];
h = img.shape[2];
#Establish our noise filter
filt = np.zeros((img.shape[0],img.shape[1]),np.uint8);
cv2.randn(filt,(0),(50));
#Apply noise filter to green channel(BGR channel 1)
for i in range(l):
	for j in range(w):
		if int(img[i][j][1]) + int(filt[i][j]) < 255:
			img[i][j][1] += filt[i][j];
#Display Image
cv2.imshow('image',img);
cv2.waitKey(0);
cv2.destroyAllWindows();
#Save image
cv2.imwrite('gaussian_green.png',img);
#Refresh img to original image
img = cv2.imread('img1.png');
#New noise filter, this may be a lot of blue noise (really high sigma)
#I'm not sure if it's because blue noise is actually
#hard for people to see, or just because I'm colorblind
#so... yeah, justifying it here just in case.
cv2.randn(filt,(0),(300));
#Apply new filter
for i in range(l):
	for j in range(w):
		if int(img[i][j][0]) + int(filt[i][j]) < 255:
			img[i][j][0] += filt[i][j];
#Show Image
cv2.imshow('image',img);
cv2.waitKey(0);
cv2.destroyAllWindows();
#Save Image
cv2.imwrite('gaussian_blue.png',img);
