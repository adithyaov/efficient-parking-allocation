import cv_func
import cv2

def mod1_ps_init(park_image, thres, level):
	im, (im2, contours, hierarchy) = cv_func.detect_contour(park_image, thres)
	cnt, x_y, r = cv_func.detect_hierarchy(contours, hierarchy, level)

	print "Press any key to close image"
	cv_func.display_contour(im, cnt, "detected_parking")
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return (x_y, r)

def mod2_ps_detect(park_image, thres, x_y, r, level):
	cropped_images = cv_func.crop_image(park_image, x_y, 2*r)

	# for x in cropped_images:
	# cv2.imshow(str(x), x)

	counter = 0
	for x in cropped_images:
		im, (im2, contours, hierarchy) = cv_func.detect_contour(x, thres)
		cnt, x_y, r = cv_func.detect_hierarchy(contours, hierarchy, level)
		counter = counter + 1
		cv_func.display_contour(im, cnt, str(counter))


	cv2.waitKey(0)
	cv2.destroyAllWindows()