import cv2
import numpy as np

# Create a blank white image
width, height = 819, 455
image = np.ones((height, width, 3), dtype=np.uint8) * 255  # White background

# Draw red triangle (R)
triangle_cnt = np.array([[0.25*width/2, 0.75*height/2], [width/3, 0.25*height/2], [width/2, 0.75*height/2]], dtype=np.int32)
cv2.drawContours(image, [triangle_cnt], 0, (0, 0, 255), -1)  # Red fill (BGR)

# Draw blue rectangle (B)
top_left = (width//4, height//2)
bottom_right = (width//2, int(0.75 * height))
cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), -1)  # Blue fill (BGR)

# Draw green circle (G)
center = (int(0.75*width), int(0.75 * height))
radius = int(0.25*width/2)
cv2.circle(image, center, radius, (0, 255, 0), -1)  # Green fill (BGR)

# Save the image
cv2.imwrite("basic_shapes.png", image)
