# problem 01: Find out the number of coins using OpenCV


import cv2
import numpy as np

#to read the image
img = cv2.imread("opencv/img/coins.jpg")

# Convert to grayscale.
gry_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur
blr = cv2.GaussianBlur(gry_img, (15, 15), cv2.BORDER_DEFAULT)

# black and white filter
ret,bw_img = cv2.threshold(blr, 10, 855,8)

#detect edegs
edg = cv2.Canny(bw_img, 50, 200)

#make outline
outline = cv2.dilate(edg, (10,10), iterations = 1)

#add counter
(cnt, hrchy) = cv2.findContours(outline.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, cnt, -1, (0, 255, 0), 2 )

cv2.imshow('Coins', cv2.resize(img, (600, 600)))
cv2.waitKey(0)

print(" The number of coins in the image is: ", len(cnt))
