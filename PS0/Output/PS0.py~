#Josh Miller
#6/6/16
#Answers to questions 1-3 of Problem set zero
import cv2
import numpy as np

#Number 1:
im1 = cv2.imread('img1.png');
im2 = cv2.imread('img2.png');
l1 =  im1.shape[0];
w1 =  im1.shape[1];
l2 = im2.shape[0];
w2 = im2.shape[1];
temp = im1[:, :,0];
cv2.imshow('image',im1);
cv2.waitKey(0);
cv2.destroyAllWindows();

#Number 2:
im1[:,:,0] = im1[:,:,2];
im1[:,:,2] = temp;
cv2.imshow('image',im1);
cv2.imwrite("swap red and blue.jpg",im1);
cv2.waitKey(0);
cv2.destroyAllWindows();
im1 = cv2.imread('img1.png');
green = np.zeros((l1,w1,3),dtype=im1.dtype);
red = np.zeros((l1,w1,3),dtype=im1.dtype);
blue = np.zeros((l1,w1,3),dtype=im1.dtype);
green[0:l1,0:w1,1] =  im1[0:l1,0:w1,1];
red[0:l1,0:w1,2] = im1[0:l1,0:w1,2];
red[0:l1,0:w1,0] = im1[0:l1,0:w1,0];
green = cv2.cvtColor(green, cv2.COLOR_BGR2GRAY);
red = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY);
blue = cv2.cvtColor(blue, cv2.COLOR_BGR2GRAY);
cv2.imwrite('green_monochrome.png',green);
cv2.imshow('image',green);
cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.imwrite('red_monochrome.png',red);
cv2.imshow('image',red);
cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.imwrite('blue_monochrome.png',blue);
cv2.imshow('image',blue);
cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.imshow('image',im2);
cv2.waitKey(0);
cv2.destroyAllWindows();
#Number 3:
green2 = np.zeros((l2,w2,3),dtype=im2.dtype);
	#Ahhhhh, love this syntax so much more
green2[:,:,1] = im2[:,:,1];
green2 = cv2.cvtColor(green2, cv2.COLOR_BGR2GRAY);
cv2.imshow('image',green2);
cv2.waitKey(0);
cv2.destroyAllWindows();
cent = green[((l1/2)-50):((l1/2)+50),((w1/2)-50):((w1/2)+50)];
cv2.imshow('image',cent);
cv2.waitKey(0);
cv2.destroyAllWindows();
green2[l2/2-50:l2/2+50,w2/2-50:w2/2+50] = cent;
cv2.imshow('image',green2);
cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.imwrite('weird_center_thing.png',green2);
