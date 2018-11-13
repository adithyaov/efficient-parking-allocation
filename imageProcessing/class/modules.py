# import sys
# sys.path.insert(0, '3rd_party/models/tutorials/image/imagenet')
# import classify_image as ci

from skimage.measure import compare_ssim
import argparse
import math
import time
import numpy as np
import cv_func
import cv2

from imutils.video import VideoStream as VS

def get_feed_points(p_lot_id):
	live_stream = VS(src=p_lot_id).start()
	time.sleep(2.0)

	image = live_stream.read()
	cv2.imwrite('/home/saki/ISH-2018/imageProcessing/refs/'+str(p_lot_id)+'ref.jpg', image)
	im, (im2, contours, hierarchy) = cv_func.detect_contour(image, 70)
	cnt, x_y, r = cv_func.detect_hierarchy(contours, hierarchy, 0)

	# cv2.drawContours(im, cnt, -1, (0,255,0), 3)
	# cv2.imshow("detected_contour", im)
	# cv2.waitKey(0)

	# cv2.destroyAllWindows()
	live_stream.stop()

	return x_y

def mark_points(p_lot_id, rows):
	ref = cv2.imread('/home/saki/ISH-2018/imageProcessing/refs/'+str(p_lot_id)+'ref.jpg')
	img = ref.copy()

	font = cv2.FONT_HERSHEY_SIMPLEX

	for x, y, pid in rows:
		cv2.putText(img,str(pid),(int(x),int(y)), int(font), 1,(0,0,255),2,cv2.LINE_AA)

	cv2.imwrite('/home/saki/ISH-2018/imageProcessing/refs/tmp.jpg', img)
	f = open('/home/saki/ISH-2018/imageProcessing/refs/tmp.jpg', 'rb')

	return f.read()

def get_current_state(p_lot_id, rows):
	live_stream = VS(src=p_lot_id).start()
	time.sleep(2.0)

	cr = 16
	fc = 0.6

	img = live_stream.read()
	ref = cv2.imread('/home/saki/ISH-2018/imageProcessing/refs/'+str(p_lot_id)+'ref.jpg')

	live_stream.stop()

	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
	x_y = map(lambda x: [x[0], x[1]], rows)
	ids = map(lambda x: x[2], rows)

	ref_crop = cv_func.crop_image(ref, x_y, cr)
	img_crop = cv_func.crop_image(img, x_y, cr)

	norm = []

	for x in range(len(ref_crop)):
		(score, diff) = compare_ssim(ref_crop[x], img_crop[x], full=True)
		if score < fc:
			score = 1
		else:
			score = 0
		norm.append(score)


	return zip(ids, norm)


def mod0_ps_bond(image, thres, level):
	park_image = image.copy()
	
	im, (im2, contours, hierarchy) = cv_func.detect_contour(park_image, thres)
	cnt, x_y, r = cv_func.detect_hierarchy(contours, hierarchy, level)
	
	cv2.drawContours(im, cnt, -1, (0,255,0), 3)

	return im


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

# def arg_parse(file):
# 	parser = argparse.ArgumentParser()
# 	parser.add_argument('--model_dir', type=str, default='/tmp/imagenet', help="")
# 	parser.add_argument('--image_file', type=str, default=file, help="")
# 	parser.add_argument('--num_top_predictions', type=int, default=1, help="")

# 	return parser.parse_known_args()	

# def mod3_ps_object(image, thres, x_y, r, level):
# 	park_image = image.copy()
# 	cropped_images = cv_func.crop_image(park_image, x_y, 2*r)

# 	for x in cropped_images:
# 		cv2.imwrite('temp.jpg', x)
# 		ci.FLAGS, ci.unparsed = arg_parse('temp.jpg')
# 		name, score = ci.main(ci.FLAGS)
# 		print name, score

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