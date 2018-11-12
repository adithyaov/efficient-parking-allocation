import numpy as np
import imutils
import math
import cv2

im = cv2.imread('park.jpg')
imr = imutils.resize(im, width=400)
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 225, 255, 0)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cnt = []
x_y = []
r = 0

for x in range(len(hierarchy[0])):
	a,b,c,d = hierarchy[0][x]
	if d == 2:
		park_space = contours[x]
		M = cv2.moments(park_space)
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])
		x_y.append((cx, cy))
		cnt.append(park_space)
		r = (r + math.sqrt(M['m00']/3.14))/2

print x_y
print r

cv2.drawContours(im, cnt, -1, (0,255,0), 3)

cv2.imshow('contour', im)

cv2.waitKey(0)
cv2.destroyAllWindows()