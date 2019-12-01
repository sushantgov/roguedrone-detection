import cv2 
import os
import sys
import numpy as np
from matplotlib import pyplot as plt
destn = "/home/sushant/Pictures/output.png"
path = "/home/sushant/Pictures/sample.png"
im1 = cv2.imread('/home/sushant/Pictures/sample.png',0)
im2 = cv2.adaptiveThreshold(im1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
edges = cv2.Canny(im2, 0, 70)

cv2.imshow('original',im1)

cv2.imwrite('/home/sushant/Pictures/out2.png', im2)
cv2.waitKey(0)
cv2.destroyAllWindows()