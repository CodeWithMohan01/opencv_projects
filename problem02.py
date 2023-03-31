# problem 02: Find out the largest and the smallest coin with circle drawn around it.

import cv2
import numpy as np

# Read the image
img = cv2.imread("opencv/img/coins.png")

# Convert to grayscale.
gry_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur
blr = cv2.GaussianBlur(gry_img, (15, 15), cv2.BORDER_DEFAULT)

# black and white filter
ret,bw_img = cv2.threshold(blr, 10, 855,8)

#detect edges
edg = cv2.Canny(bw_img, 50, 200)

#make outline
outline = cv2.dilate(edg, (10,10), iterations = 3)

#add counter
(cnt, hrchy) = cv2.findContours(outline.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Create an empty list to store the areas of all detected coins
areas = []

# Iterate over all contours
for i in cnt:
    # Compute the area of the contour
    area = cv2.contourArea(i)
    # If the area is greater than 1000, consider it a coin
    if area > 1000:
        # Add the area to the list of areas
        areas.append(area)

# Find the smallest and largest coins
smallest = np.argmin(areas)
largest = np.argmax(areas)

# Iterate over all contours again
for i in range(len(cnt)):
    # Compute the area of the contour
    area = cv2.contourArea(cnt[i])
    # If the area is greater than 1000, consider it a coin
    if area > 1000:
        # Draw a circle around the coin
        if i == smallest:
            cv2.circle(img, (int(cv2.minEnclosingCircle(cnt[i])[0][0]), int(cv2.minEnclosingCircle(cnt[i])[0][1])), int(cv2.minEnclosingCircle(cnt[i])[1]), (0, 0, 255), 2)
            cv2.putText(img, "Smallest Coin", (int(cv2.minEnclosingCircle(cnt[i])[0][0]) - 50, int(cv2.minEnclosingCircle(cnt[i])[0][1]) - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        elif i == largest:
            cv2.circle(img, (int(cv2.minEnclosingCircle(cnt[i])[0][0]), int(cv2.minEnclosingCircle(cnt[i])[0][1])), int(cv2.minEnclosingCircle(cnt[i])[1]), (0, 255, 0), 2)
            cv2.putText(img, "Largest Coin", (int(cv2.minEnclosingCircle(cnt[i])[0][0]) - 50, int(cv2.minEnclosingCircle(cnt[i])[0][1]) - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
# Display the image
cv2.imshow('Coins', cv2.resize(img, (900, 800)))
cv2.waitKey(0)
cv2.destroyAllWindows()



