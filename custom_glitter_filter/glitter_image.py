import random

import cv2
import numpy as np

image = cv2.imread('pic.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

gray = cv2.GaussianBlur(gray, (9, 9), 0)
thresh1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 1)

cv2.imshow('adaptive', thresh1)
cv2.waitKey()



# thresh1 is binary image has only 0 0r 255 no planes
rows, cols = np.shape(thresh1)

# canvas on which we r going to print our image will hv 3 planes
canvas = np.zeros((rows,cols,3), dtype='uint8')

for i in range(rows):
    for j in range(cols):
        for k in range(3): #k is num of planes
            if thresh1[i][j] == 255:
                color = random.randrange(0,255,1)
                #paint our canvas with random color
                canvas[i][j][k] = color
            else:
                color = 0
                canvas[i][j][k] = color


cv2.imshow('glitter', canvas)
cv2.waitKey()
