import sys
sys.path.insert(0, '3rd_party/models/tutorials/image/imagenet')
import classify_image as ci
import argparse

import numpy as np
import cv_func
import cv2

def mod0_ps_bond(image, thres, level):
	park_image = image.copy()
	im, (im2, contours, hierarchy) = cv_func.detect_contour(park_image, thres)
	cnt, x_y, r = cv_func.detect_hierarchy(contours, hierarchy, level)

	cv_func.display_contour(im, cnt, "detected_parking")
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	x_y_list = []
	for i in cnt[0]:
		x_y_list.append([i[0][0], i[0][1]])

	return x_y_list

def mod1_ps_init(image, thres, level):
	park_image = image.copy()
	im, (im2, contours, hierarchy) = cv_func.detect_contour(park_image, thres)
	cnt, x_y, r = cv_func.detect_hierarchy(contours, hierarchy, level)

	cv_func.display_contour(im, cnt, "detected_parking_lots")
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return (x_y, r)

def mod2_ps_detect(image, thres, x_y, r, level):
	park_image = image.copy()
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

		
		cv2.imshow("state",im)
		cv2.waitKey(0)
	
		state.append(s)
	cv2.destroyAllWindows()			
		
	return state

def arg_parse(file):
	parser = argparse.ArgumentParser()
	parser.add_argument('--model_dir', type=str, default='/tmp/imagenet', help="")
	parser.add_argument('--image_file', type=str, default=file, help="")
	parser.add_argument('--num_top_predictions', type=int, default=1, help="")

	return parser.parse_known_args()	

def mod3_ps_object(image, thres, x_y, r, level):
	park_image = image.copy()
	cropped_images = cv_func.crop_image(park_image, x_y, 2*r)

	for x in cropped_images:
		cv2.imwrite('temp.jpg', x)
		ci.FLAGS, ci.unparsed = arg_parse('temp.jpg')
		name, score = ci.main(ci.FLAGS)
		print name, score

def mod4_psrb_ref(ref, out, x_y, r, thres):
	ref_img = ref.copy()
	out_img = out.copy()

	ret, ref_thresh = cv2.threshold(ref_img, thres, 255, 0)
	ret, out_thresh = cv2.threshold(out_img, thres, 255, 0)

	ref_crop = cv_func.crop_image(ref_thresh, x_y, 2*r)
	out_crop = cv_func.crop_image(out_thresh, x_y, 2*r)

	norm = []

	for x in range(len(ref_crop)):
		diff = ref_crop[x]-out_crop[x]
		norm.append(np.linalg.norm(diff))
	
	return norm/max(norm)


def mod5_ps_draw(image, x_y):
	park_image = image.copy()
	for x, y in x_y:
		cv2.circle(park_image, (x, y), 3, (0,0,255), -1)

	cv2.imshow("tada", park_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return park_image