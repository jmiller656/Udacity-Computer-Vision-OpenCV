#Josh Miller
#1/2/17
#Answers to questions 1-3 of Problem set zero
import cv2
import numpy as np
import utils

#Number 1:
im1 = cv2.imread('img1.png');
im2 = cv2.imread('img2.png');
l1 =  im1.shape[0];
w1 =  im1.shape[1];
l2 = im2.shape[0];
w2 = im2.shape[1];
temp = im1[:, :,0];
utils.showAndWait(im1)

#Number 2
im1[:,:,0] = im1[:,:,2];
im1[:,:,2] = temp;
utils.showAndWait(im1)
cv2.imwrite("swap red and blue.jpg",im1);

r,g,b = getRGBMonochromes(im1)
cv2.imwrite('green_monochrome.png',g);
#show green monochrome
utils.showAndWait(r)
#show red monochrome
utils.showAndWait(g)
#show blue monochrome
utils.showAndWait(b)

utils.showAndWait(im2)

#Number 3:
green2 = np.zeros((l2,w2,3),dtype=im2.dtype);
green2[:,:,1] = im2[:,:,1];
green2 = cv2.cvtColor(green2, cv2.COLOR_BGR2GRAY);
utils.showAndWait(green2)
cent = green[((l1/2)-50):((l1/2)+50),((w1/2)-50):((w1/2)+50)];
utils.showAndWait(cent)
green2[l2/2-50:l2/2+50,w2/2-50:w2/2+50] = cent;
utils.showAndWait(green2)
cv2.imwrite('weird_center_thing.png',green2);

