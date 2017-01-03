#Josh Miller
#1/2/17
#Answers to questions 1-3 of Problem set zero
import cv2
import numpy as np
import utils

"""
Number 1 ///////////////////////////////////////////
"""
im1 = cv2.imread('Input/img1.png');
im2 = cv2.imread('Input/img2.png');

#Useful dimensions we will be using later
l1 =  im1.shape[0];
w1 =  im1.shape[1];
l2 = im2.shape[0];
w2 = im2.shape[1];
temp = im1[:, :,0];

#Show image 1
utils.showAndWait(im1)

"""
Number 2 ///////////////////////////////////////////
"""
im1[:,:,0] = im1[:,:,2];
im1[:,:,2] = temp;
utils.showAndWait(im1)

#Save red and blue swap
cv2.imwrite("Output/swap red and blue.jpg",im1);

#Get monochromes of the image
red,green,blue = utils.getRGBMonochromes(im1)

#Save green monochrome
cv2.imwrite('Output/green_monochrome.png',green);

#show green monochrome
utils.showAndWait(red)

#show red monochrome
utils.showAndWait(green)

#show blue monochrome
utils.showAndWait(blue)

#show image 2
utils.showAndWait(im2)

"""
Number 3 ///////////////////////////////////////////
"""
green2 = np.zeros((l2,w2,3),dtype=im2.dtype);
green2[:,:,1] = im2[:,:,1];
green2 = cv2.cvtColor(green2, cv2.COLOR_BGR2GRAY);
utils.showAndWait(green2)
center = green[((l1/2)-50):((l1/2)+50),((w1/2)-50):((w1/2)+50)];
utils.showAndWait(center)
green2[l2/2-50:l2/2+50,w2/2-50:w2/2+50] = center;
utils.showAndWait(green2)
cv2.imwrite('Output/weird_center_thing.png',green2);

"""
Number 4 ///////////////////////////////////////////
"""
green3 = cv2.imread('Output/green_monochrome.png');
print "Min = " + repr(green.min());
print "Max = " + repr(green.max());

ms = cv2.meanStdDev(green);
mean = ms[0][0][0];
sigma = ms[1][0][0];

print "Mean = " + str(mean);
print "StdDev = " + repr(sigma);

#Apply normalization to image
for x in range(green3.shape[0]):
	for y in range(green3.shape[1]):
		for z in range(green3.shape[2]):
			temp = (green3[x][y][z] - mean);
			temp /= sigma;
			temp *= 10;
			temp += mean;
			green3[x][y][z] = temp;
utils.showAndWait(green)
cv2.imwrite('Output/filtered.png',green3);

#Create and apply kernel
kernel = np.zeros((1,3),green.dtype);
kernel[0][2] = 1;
dst = cv2.filter2D(green,-1,kernel);

#Save image with kernel applied
cv2.imwrite('Output/left_convolution_2px.png',dst);

#Show original and then image with kernel applied for comparison
utils.showAndWait(green)
utils.showAndWait(dst)

#Subtract shifted image from original for interesting results
diff = green -dst;

#Save difference as image
cv2.imwrite('Output/diff_left_conv_2px.png',diff);
utils.showAndWait(diff)

"""
Number 5 ///////////////////////////////////////////
"""
#Read in our image
im1 = cv2.imread('Input/img1.png');

#Establish our noise filter
filt = np.zeros((im1.shape[0],im1.shape[1]),np.uint8);
cv2.randn(filt,(0),(50));
#Apply noise filter to green channel(BGR channel 1)
for i in range(im1.shape[0]):
	for j in range(im1.shape[1]):
		if int(im1[i][j][1]) + int(filt[i][j]) < 255:
			im1[i][j][1] += filt[i][j];
#Display Image
utils.showAndWait(im1)

#Save image
cv2.imwrite('Output/gaussian_green.png',im1);
#Refresh im1 to original image
im1 = cv2.imread('Input/img1.png');
#New noise filter, this may be a lot of blue noise (really high sigma <stdDev>)
#I'm not sure if it's because blue noise is actually
#hard for people to see, or just because I'm colorblind
#so... yeah, justifying it here just in case.
cv2.randn(filt,(0),(300));
#Apply new filter
for i in range(im1.shape[0]):
	for j in range(im1.shape[1]):
		if int(im1[i][j][0]) + int(filt[i][j]) < 255:
			im1[i][j][0] += filt[i][j];
#Show Image
utils.showAndWait(im1)
#Save Image
cv2.imwrite('Output/gaussian_blue.png',im1);

print("Done")
