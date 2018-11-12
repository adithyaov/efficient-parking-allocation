import cv2
import time
import modules
import cv_func

x_y = modules.get_feed_points(1)

time.sleep(2.0)

norm = modules.some_func(1, x_y)

print norm

# image = cv2.imread('park_space_uc.jpg')
# x_y_bond = modules.mod0_ps_bond(image, 225, 1)
# x_y_plot, r = modules.mod1_ps_init(image, 225, 2) #get_feed_points

# image = cv2.imread('park_space_uc.jpg', 0)
# state = modules.mod2_ps_detect(image, 225, x_y_plot, r, 2)
# print state, sum(state)

# image = cv2.imread('park_space_oc.jpg', 0)
# state = modules.mod2_ps_detect(image, 225, x_y_plot, r, 2)
# print state, sum(state)

# image = cv2.imread('park_space_oc.jpg', 0)
# modules.mod3_ps_object(image, 225, x_y_plot, r, 2)

# ref = cv2.imread('park_space_uc.jpg')
# out = cv2.imread('park_space_oc.jpg')

# norm = modules.mod4_psrb_ref(ref, out, x_y_plot, r, 225)
# print norm

# x_y = [[40, 69], [12, 43], [65, 83]]
# mod_image = modules.mod5_ps_draw(image, x_y_bond)