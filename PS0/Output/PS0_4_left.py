#Josh Miller
#6/7/16
#Answers to questions 4 (the rest) of Problem set zero
import cv2
import numpy as np
green = cv2.imread('green_monochrome.png');
kernel = np.zeros((1,3),green.dtype);
kernel[0][2] = 1;
dst = cv2.filter2D(green,-1,kernel);
cv2.imshow('image',green);
cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.imwrite('left_convolution_2px.png',dst);
cv2.imshow('image',dst);
cv2.waitKey(0);
cv2.destroyAllWindows();
diff = green -dst;
cv2.imwrite('diff_left_conv_2px.png',diff);
cv2.imshow('image',diff);
cv2.waitKey(0);
cv2.destroyAllWindows();
