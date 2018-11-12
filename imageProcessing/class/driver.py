import cv2
import modules

image = cv2.imread('park_space.jpg')

x_y, r = modules.mod1_ps_init(image, 225, 2)
modules.mod2_ps_detect(image, 225, x_y, r, 2)