import cv2
import numpy as np
import os
PATH_TO_YOUR_CROP = './UndistortAndCropThese'
image_files = [os.path.join(path, name) for path, subdirs, files in os.walk(PATH_TO_YOUR_CROP) for name in files if (name.endswith("_1.png") and 'mini_dora' not in path)]
image_files1 = [os.path.join(path, name) for path, subdirs, files in os.walk(PATH_TO_YOUR_CROP) for name in files if (name.endswith("_0.png") and 'mini_dora' not in path)]
image_files.sort()  # Ensure files are in order
image_files1.sort()  # Ensure files are in order
def binary_threshold():
    if not os.path.exists("./thresh_1"):
        print("Directory does not exist:", PATH_TO_YOUR_CROP)
        os.makedirs("./thresh_1")
    for image_file, image_file1 in zip(image_files, image_files1): 
        print("Processing:", image_file)
        image = cv2.imread(image_file)
        gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #gray1= cv2.GaussianBlur(gray1, (95, 95), 0)
        image= cv2.imread(image_file1)
        gray2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #gray2= cv2.GaussianBlur(gray2, (95, 95), 0)
        threshval, thresh = cv2.threshold(gray1, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
        print(threshval)
        threshval, thresh = cv2.threshold(gray1, threshval, 255, cv2.THRESH_BINARY)
        if not os.path.exists(os.path.join("./thresh_1", image_file[image_file.index("\\")+1:image_file.rindex("\\")])):
            os.makedirs(os.path.join("./thresh_1", image_file[image_file.index("\\")+1:image_file.rindex("\\")]))
        cv2.imwrite(os.path.join("./thresh_1", image_file[image_file.index("\\")+1:image_file.rindex("\\")], "0.png"), thresh)
        threshval, thresh1= cv2.threshold(gray2, threshval, 255, cv2.THRESH_BINARY)
        cv2.imwrite(os.path.join("./thresh_1", image_file[image_file.index("\\")+1:image_file.rindex("\\")], "1.png"), thresh1)
        thresh2=cv2.absdiff(thresh, thresh1)
        cv2.imwrite(os.path.join("./thresh_1", image_file[image_file.index("\\")+1:image_file.rindex("\\")], "2.png"), thresh2)
        
        # detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
        # contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
        # max_perimeter = 0
        # for contour in contours:
        #     perimeter = cv2.arcLength(contour, True)
        #     if perimeter > max_perimeter:
        #         max_perimeter = perimeter
        #         max_contour = contour
        
        # print("Perimeter:", max_perimeter)  
        # epsilon = 0.05*cv2.arcLength(max_contour,True)
        # approx = cv2.approxPolyDP(max_contour,epsilon,True)                        
        # # draw contours on the original image
        # image_copy = image.copy()
        # #cv2.drawContours(image=image_copy, contours=[approx], contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
        # cv2.fillPoly(thresh, pts=[approx], color=255)            
        
        # cv2.imwrite(os.path.join("./thresh_1", image_file[image_file.index("\\")+1:image_file.rindex("\\")], "3.png"), thresh)

        kernel = np.ones((9, 9), np.uint8)
        img_erosion = cv2.erode(thresh2, kernel, iterations=1)
        cv2.imwrite(os.path.join("./thresh_1", image_file[image_file.index("\\")+1:image_file.rindex("\\")], "3.png"), img_erosion)

def hsv_threshold():
    if not os.path.exists("./thresh_2"):
        os.makedirs("./thresh_2")
    list1=[]
    v_img = None
    for image_file, image_file1 in zip(image_files, image_files1): 
        print("Processing:", image_file)
        image = cv2.imread(image_file)
        image=image[:1003,:]
        list1.append(image)
        if(v_img is None):
            v_img = image
        else:
            v_img = cv2.vconcat([v_img, image])
        if not os.path.exists(os.path.join("./thresh_2", image_file[image_file.index("\\")+1:image_file.rindex("\\")])):
            os.makedirs(os.path.join("./thresh_2", image_file[image_file.index("\\")+1:image_file.rindex("\\")]))
        
        cv2.imwrite(os.path.join("./thresh_2", image_file[image_file.index("\\")+1:image_file.rindex("\\")], "0.png"), image)

    cv2.imwrite(os.path.join("./thresh_2", "stack.png"), v_img)
    hsv1=cv2.cvtColor(v_img,cv2.COLOR_BGR2HSV)
    
    h, s, v = cv2.split(v_img)

    # Find min and max for each channel
    h_min, s_min, v_min = h.min(), s.min(), v.min()
    h_max, s_max, v_max = h.max(), s.max(), v.max()

    print(f"Min HSV: ({h_min}, {s_min}, {v_min})")
    print(f"Max HSV: ({h_max}, {s_max}, {v_max})")
    for image_file, image_file1 in zip(image_files, image_files1): 
        print("Processing:", image_file)
        image = cv2.imread(image_file)
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_bound = np.array([10, 10, 10])
        upper_bound = np.array([255, 255, 255])
        print(f"Lower Bound: {type(lower_bound)}, Upper Bound: {type(upper_bound)}")
        mask = cv2.inRange(image, lower_bound, upper_bound)
        cv2.imwrite(os.path.join("./thresh_2", image_file[image_file.index("\\")+1:image_file.rindex("\\")], "1.png"), mask)
binary_threshold()