import numpy as np
import cv_func
import cv2

def mod1_ps_init(park_image, thres, level):
	im, (im2, contours, hierarchy) = cv_func.detect_contour(park_image, thres)
	cnt, x_y, r = cv_func.detect_hierarchy(contours, hierarchy, level)

	cv_func.display_contour(im, cnt, "detected_parking")
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return (x_y, r)

def mod2_ps_detect(park_image, thres, x_y, r, level):
	cropped_images = cv_func.crop_image(park_image, x_y, 2*r)
	state = []

	for x in cropped_images:
		s = 0
		im = x.copy()
		img = cv2.medianBlur(im,5)
		# cimg = cv2.cvtColor(im,cv2.COLOR_GRAY2BGR)		
		
		circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=40,minRadius=int(0.5*r),maxRadius=int(1.5*r))
		
		if circles is not None:
			s = 1
			circles = np.round(circles[0, :]).astype("int")
			for (x, y, r) in circles:
				cv2.circle(im, (x, y), r, (0, 255, 255), 4)

		
		cv2.imshow("out",im)
		cv2.waitKey(0)
	
		state.append(s)
	cv2.destroyAllWindows()			
		
	return state