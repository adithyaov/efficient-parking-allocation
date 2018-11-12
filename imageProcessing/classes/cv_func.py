import numpy as np
import imutils
import math
import cv2

def detect_contour(image, thres_val):
	im = cv2.imread(image)
	im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	ret, im_thresh = cv2.threshold(imgray, thres_val, 255, 0)
	
	return (im, cv2.findContours(im_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE))

def detect_hierarchy(hierarchy, level):
	x_y = []
	cnt = []
	r = 0

	for contour in range(len(hierarchy[0])):
		a,b,c,d = hierarchy[0][contour]
		if d == level:
			pattern = contours[contour]
			M = cv2.moments(pattern)
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			x_y.append([cx, cy])
			cnt.append(park_space)
			r = (r + math.sqrt(M['m00']/3.14)) / 2

	return (cnt, x_y, r)

def crop_image(img, x_y, cr):
	images = []

	for y, x in x_y:
		images.append(img[int(x-cr):int(x+cr),int(y-cr):int(y+cr)])

	return images