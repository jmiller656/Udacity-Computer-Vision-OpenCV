#Josh Miller
#6/7/16
#Answers to questions (partially) 4 of Problem set zero
import cv2
import numpy as np
green = cv2.imread('green_monochrome.png');
print "Min = " + repr(green.min());
print "Max = " + repr(green.max());
ms = cv2.meanStdDev(green);
mean = ms[0][0][0];
sigma = ms[1][0][0];
print "Mean = " + str(ms[0][0][0]);
print "Sigma = " + repr(ms[1][0][0]);
for x in range(green.shape[0]):
	for y in range(green.shape[1]):
		for z in range(green.shape[2]):
			temp = (green[x][y][z] - mean);
			temp /= sigma;
			temp *= 10;
			temp += mean;
			green[x][y][z] = temp;

cv2.imshow('image',green);
cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.imwrite('filtered.png',green);

