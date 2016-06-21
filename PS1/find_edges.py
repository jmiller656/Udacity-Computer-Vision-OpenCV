#Josh Miller
#6/21/16
#Initial Edge Detection for Problem set 1
import cv2
import numpy as np
import hough
#Read in image
inputImage = cv2.imread('input/ps1-input0.png');
#Sanity check, show original image
cv2.imshow('image',inputImage);
cv2.waitKey(0);
cv2.destroyAllWindows();
#Find edges
edges = cv2.Canny(inputImage,100,200);
#Show Edges of input image
cv2.imshow('image',edges);
cv2.waitKey(0);
cv2.destroyAllWindows();
#Get Hough accumulator array of edge image
H = hough.hough_lines(edges);
cv2.imshow('image',H);
cv2.waitKey(0);
cv2.destroyAllWindows();
lines = inputImage;
peaks = hough.find_peaks(H,4);
for theta,rho in peaks:
	a = np.cos(theta);
	b = np.sin(theta);
	x0 = a*rho;
	y0 = b*rho;
	x1 = int(x0 + 1000*(-b));
	y1 = int(x0 + 1000*(a));
	x2 = int(x0 - 1000*(-b));
	y2 = int(x0 - 1000*(a));
	cv2.line(lines,(x1,y1),(x2,y2),(0,255,0),2);
cv2.imshow('image',lines);
cv2.waitKey(0);
cv2.destroyAllWindows();
