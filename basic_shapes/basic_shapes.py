import cv2
import numpy as np
img= cv2.imread('1.jpg')
img1=cv2.resize(img, (819, 455))
width, height = 819, 455
triangle_cnt = np.array([[0.45*width/2, 0.75*height/2], [width*0.46, 0.3*height/2], [width*0.54, 0.85*height/2]], dtype=np.int32)
    
cv2.drawContours(img1, [triangle_cnt], 0, (0, 0, 255), -1)  # Red fill (BGR)

# Draw blue rectangle (B)
top_left = (int(width*0.31), int(height*0.53))
bottom_right = (int(width*0.52), int(0.7 * height))
cv2.rectangle(img1, top_left, bottom_right, (255, 0, 0), -1)  # Blue fill (BGR)

# Draw green circle (G)
center = (int(0.69*width), int(0.7 * height))
radius = int(0.15*width/2)
cv2.circle(img1, center, radius, (0, 255, 0), -1)  # Green fill (BGR)

cv2.imshow('image', img1)
cv2.waitKey(0)