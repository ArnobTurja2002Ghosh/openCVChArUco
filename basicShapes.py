import cv2
import numpy as np

# Create a blank white image
width, height = 819, 455
image = np.ones((height, width, 3), dtype=np.uint8) * 255  # White background

def basic_shapes():
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

def boundary():
    pt1 = (0, 0)
    pt2=(0, height)
    for i in range(0, int(width/16), 5):  
        pt1 = (i, 0)
        pt2 = (i, height) 
        cv2.line(image,pt1,pt2,(0,0,0),1)
        
    top_left = tuple(map(int, (width-((width/16)/2)/10, 0) ))
    bottom_right = tuple(map(int, (width, height) ))
    for i in range(10):
        color1 = (list(np.random.choice(range(256), size=3)))  
        color =[int(color1[0]), int(color1[1]), int(color1[2])]  
        cv2.rectangle(image, top_left, bottom_right, color, -1)
        bottom_right = tuple(map(int, (top_left[0], bottom_right[1]) ))
        top_left = tuple(map(int, (top_left[0] - ((width/16)/2)/10, top_left[1]) ))
    top_left = tuple(map(int, (0, 0) ))
    bottom_right = tuple(map(int, (width, ((height/9)/2)/10) ))   
    for i in range(10):
        color1 = (list(np.random.choice(range(256), size=3)))  
        color =[int(color1[0]), int(color1[1]), int(color1[2])]  
        cv2.rectangle(image, top_left, bottom_right, color, -1)
        top_left = tuple(map(int, (top_left[0], bottom_right[1]) ))
        bottom_right = tuple(map(int, (bottom_right[0], bottom_right[1] + ((height/9)/2)/10) ))
    
    bottom_right = tuple(map(int, (width, height) ))  
    top_left = tuple(map(int, (0, height-((height/9)/2)/10) ))  
    for i in range(10):
        color1 = (list(np.random.choice(range(256), size=3)))  
        color =[int(color1[0]), int(color1[1]), int(color1[2])]  
        cv2.rectangle(image, top_left, bottom_right, color, -1)
        bottom_right = tuple(map(int, (bottom_right[0], top_left[1]) ))
        top_left = tuple(map(int, (top_left[0], top_left[1] - ((height/9)/2)/10) ))
    cv2.imwrite("boundary.png", image)

boundary()