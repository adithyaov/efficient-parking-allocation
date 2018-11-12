import cv_func
import cv2

im, (im2, contours, hierarchy) = cv_func.detect_contour('park.jpg', 225)
cnt, x_y, r = cv_func.detect_hierarchy(contours, hierarchy, 2)
cropped_images = cv_func.crop_image(im, x_y, 2*r)

cv2.imshow("park", im)

for x in cropped_images:
	cv2.imshow(str(x), x)

cv2.waitKey(0)
cv2.destroyAllWindows()