import cv2
import numpy as np
import math
#Get Hough Accumulator Array of edge image
def hough_lines(edges):
	d = int(math.sqrt((edges.shape[0] * edges.shape[0]) + (edges.shape[1] * edges.shape[1])));
	D = d*2 + 1 ;
	H = np.zeros(shape=(D,180))
	for x in range(edges.shape[0]):
		for y in range(edges.shape[1]):
			if edges[x,y] == 255:
				for theta in range(180):
					rtheta = (np.pi / 180) * (theta-1);
					temp = int((x*np.cos(rtheta) - y*np.sin(rtheta)) );
					temp = (temp + d) % d;
					H[temp,(theta-1)%180] += 1;
	return H;

#Find peaks in Hough Accumularot Array
def find_peaks(H,num_peaks):
	peaks = [];
	temp_max = 0;
	temp_coord = [];
	for i in range(num_peaks):
		for x in range(H.shape[0]):
			for y in range(H.shape[1]):
				if H[x,y] > temp_max:					
					t = [x,y];
					if t not in peaks:
						temp_max = H[x,y];
						temp_coord = t;
		peaks.append(temp_coord);
		temp_max = 0;
		temp_coord = [];
	return peaks;
