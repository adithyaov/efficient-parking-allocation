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