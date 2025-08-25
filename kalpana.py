
import cv2
import numpy as np
import raw
import os
import json
import csv
import matplotlib.pyplot as plt
with open('kalpana.json', 'r') as file:
    data = json.load(file)
camera_matrix = np.load('camera_matrix.npy')
dist_coeffs = np.load('dist_coeffs.npy')

PATH_TO_YOUR_PAIRED = './chaarAdhyay'
PATH_TO_YOUR_CROP = './UndistortAndCropThese'
image_files = [os.path.join(path, name) for path, subdirs, files in os.walk(PATH_TO_YOUR_PAIRED) for name in files if name==data['undistort_file']]
image_files.sort()  # Ensure files are in order

def undistort():    
    for image_file in image_files:
        #print(cv2.imread(image_file).shape) # Load the image to ensure it exists

        image = raw.raw_to_npArray(image_file)
        undistorted_image = cv2.undistort(image, camera_matrix, dist_coeffs)
        print("UndistortAndCropThese/camShader"+image_file[image_file.index("\\")+1:])
        if not os.path.exists(os.path.join("UndistortAndCropThese", image_file[image_file.index("\\")+1: image_file.rindex("\\")])):
            os.makedirs(os.path.join("UndistortAndCropThese", image_file[image_file.index("\\")+1: image_file.rindex("\\")]))
        cv2.imwrite("UndistortAndCropThese/"+image_file[image_file.index("\\")+1:-4]+".png", undistorted_image)
        gray1 = cv2.cvtColor(undistorted_image, cv2.COLOR_BGR2GRAY)
        
        hist = cv2.calcHist([gray1], [0], None, [256], [0, 256])
        plt.plot(hist)
        # label the x-axis
        plt.xlabel('Pixel Intensity')
        # label the y-axis
        plt.ylabel('Number of Pixels')
        # display the title
        plt.title('Grayscale Histogram')
        if data["thresholding_algorithm"] == "global":
            threshval, thresh = cv2.threshold(gray1, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
            plt.plot([threshval, threshval], [0, 1e7])
            threshval, thresh=cv2.threshold(gray1, 0.25*threshval, 255, cv2.THRESH_BINARY)
            plt.plot([threshval, threshval], [0, 1e7])
            plt.savefig("UndistortAndCropThese/"+image_file[image_file.index("\\")+1:-4]+"_histogram.png")
            plt.clf()  # Clear the current figure
        elif data["thresholding_algorithm"] == "adaptive":
            #thresh = cv2.adaptiveThreshold(gray1,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,9999,data["c"])
            with open('adaptiveThreshold.csv', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    #print(row)
                    if( row['src'] == image_file[image_file.index("\\")+1:image_file.rindex("\\")]):
                        thresh = cv2.adaptiveThreshold(gray1,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,int(row['blockSize']),int(row['C']))
            # thresh2 = cv2.adaptiveThreshold(gray2,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,3333,data["c"])
        #print(threshval)
        #kernel = np.ones((5, 5), np.uint8)
        #img_erosion = cv2.dilate(thresh, kernel, iterations=3)
        #img_erosion = cv2.erode(img_erosion, kernel, iterations=3)
        cv2.imwrite("UndistortAndCropThese/"+image_file[image_file.index("\\")+1:-4]+"_thresh.png", thresh)
        # cv2.imwrite("UndistortAndCropThese/"+image_file[image_file.index("\\")+1:-4]+"_thresh2.png", thresh2)

        # abs_diff = cv2.absdiff(thresh, thresh2)
        # cv2.imwrite("UndistortAndCropThese/"+image_file[image_file.index("\\")+1:-4]+"_absdiff.png", abs_diff)
        
undistort()

image_files1 = [os.path.join(path, name) for path, subdirs, files in os.walk(data["crop_folder"]) for name in files]
image_files1.sort()  # Ensure files are in order


def crop():
    for image_file1, image_file in zip(image_files1, image_files):
        image=cv2.imread(image_file1)
        image2=raw.raw_to_npArray(image_file)
        print(camera_matrix[1,2], image.shape[0]/2)
        if(image2.shape[0]/2 > camera_matrix[1,2]):
            image1=image[round(image.shape[0]/2-camera_matrix[1,2]) : , : ]
        elif(image2.shape[0]/2 < camera_matrix[1,2]):
            image1=image[ : image2.shape[0] , : ]
        if(image2.shape[1]/2 > camera_matrix[0,2]):
            image1=image1[ :, round(image1.shape[1]/2-camera_matrix[0,2]) : ]
        elif(image2.shape[1]/2 < camera_matrix[0,2]):
            image1=image1[ :, : image2.shape[1] ]
        print(image.shape, image1.shape, os.path.basename(PATH_TO_YOUR_PAIRED))
        cv2.imwrite(os.path.join(PATH_TO_YOUR_CROP, os.path.basename(image_file1)[:-4], os.path.basename(image_file1)), image1)

        gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray1, 0, 255, cv2.THRESH_BINARY)
        cv2.imwrite(os.path.join(PATH_TO_YOUR_CROP, os.path.basename(image_file1)[:-4], "thresh_"+os.path.basename(image_file1)), thresh)

crop()

def difference():
    for image_file1, image_file in zip(image_files1, image_files):
        thresh = cv2.imread("UndistortAndCropThese/"+image_file[image_file.index("\\")+1:-4]+"_thresh.png")
        thresh1= cv2.imread(os.path.join(PATH_TO_YOUR_CROP, os.path.basename(image_file1)[:-4], "thresh_"+os.path.basename(image_file1)))
        thresh2=cv2.absdiff(thresh, thresh1)

        # thresh01=cv2.imread("UndistortAndCropThese/"+image_file[image_file.index("\\")+1:-4]+"_thresh2.png")
        # thresh21= cv2.absdiff(thresh01, thresh1)

        kernel = np.ones((5, 5), np.uint8)
        img_erosion = cv2.erode(thresh2, kernel, iterations=3)
        cv2.imwrite(os.path.join(PATH_TO_YOUR_CROP, os.path.basename(image_file1)[:-4], "diff_"+os.path.basename(image_file1)), thresh2)
        #cv2.imwrite(os.path.join(PATH_TO_YOUR_CROP, os.path.basename(image_file1)[:-4], "diff2_"+os.path.basename(image_file1)), thresh21)
        src1 = cv2.imread("UndistortAndCropThese/"+image_file[image_file.index("\\")+1:-4]+".png")
        src2= cv2.imread(os.path.join(PATH_TO_YOUR_CROP, os.path.basename(image_file1)[:-4], os.path.basename(image_file1)))
        dst = cv2.addWeighted(src1, 0.3, src2, 0.7, 0.0)
        cv2.imwrite(os.path.join(PATH_TO_YOUR_CROP, os.path.basename(image_file1)[:-4], "blend_"+os.path.basename(image_file1)), dst)
difference()
