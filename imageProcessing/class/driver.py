import cv2
import modules

image = cv2.imread('park_space_uc.jpg')
x_y, r = modules.mod1_ps_init(image, 225, 2)

image = cv2.imread('park_space_uc.jpg', 0)
state = modules.mod2_ps_detect(image, 225, x_y, r, 2)
print state, sum(state)

image = cv2.imread('park_space_oc.jpg', 0)
state = modules.mod2_ps_detect(image, 225, x_y, r, 2)
print state, sum(state)