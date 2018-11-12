import numpy as np
import imutils
import cv2

im = cv2.imread('what.jpg')
imr = imutils.resize(im, width=400)
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 127, 255, 0)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print len(contours)

cv2.drawContours(im, contours[6], -1, (0,255,0), 3)

cv2.imshow('contour', im)

cv2.waitKey(0)
cv2.destroyAllWindows()
