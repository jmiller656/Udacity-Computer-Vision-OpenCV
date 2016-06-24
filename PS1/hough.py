import cv2
import numpy as np
import math
#Get Hough Accumulator Array of edge image in order to find lines
#@param edges: an edge image (ex. processed using canny edge detection) to make the accumulator array for
#@return A hough accumulator array for the edge image
def hough_lines(edges):
	#Maximum length of a line in this image
	d = int(math.sqrt((edges.shape[0] * edges.shape[0]) + (edges.shape[1] * edges.shape[1])));
	#Initialize hough accumulator array of size d x 180; where d is the maximum length of a line in that image (a diagonal going completely across)
	H = np.zeros(shape=(d,180))
	#Voting process for the hough accumulator array
	for x in range(edges.shape[0]):
		for y in range(edges.shape[1]):
			#Only vote if the pixel at x,y is an edge
			if edges[x,y] == 255:
				for theta in range(180):
					#Some slightly spooky math (not that terrible, honestly)
					rtheta = (np.pi / 180) * (theta-1);
					temp = int((x*np.cos(rtheta) + y*np.sin(rtheta)) );
					temp = (temp + d) % d;
					H[temp,(theta-1)%180] += 1;
	return H;

#Find peaks in Hough Accumularot Array
#@param H: hough accumulator array of your edge image
#@param num_peaks: Number of peaks you would like to find
#@return An list of rho-theta pairs to be used for line drawing 
def find_peaks(H,num_peaks):
	peaks = [];
	temp_max = 0;
	temp_coord = [];
	for i in range(num_peaks):
		for x in range(H.shape[0]):
			for y in range(H.shape[1]):
				if H[x,y] > temp_max:					
					t = [x,y];
					#This is done as to not tamper with the
					#Accumulator array, but also not need a deep copy
					#And to make sure we don't just get several copies of
					#The same peak
					if t not in peaks:
						temp_max = H[x,y];
						temp_coord = t;
		peaks.append(temp_coord);
		temp_max = 0;
		temp_coord = [];
	return peaks;
