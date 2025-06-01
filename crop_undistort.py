import cv2
import numpy as np
camera_matrix = np.load('camera_matrix.npy')
dist_coeffs = np.load('dist_coeffs.npy')
import raw
import os
import time
import threading


PATH_TO_YOUR_PAIRED = './pairedImages'
PATH_TO_YOUR_CROP = './UndistortAndCropThese'
image_files = [os.path.join(path, name) for path, subdirs, files in os.walk(PATH_TO_YOUR_PAIRED) for name in files if name.endswith("_1.nef")]
image_files.sort()  # Ensure files are in order
currentlyReading={"image_file":None, "image_no": None, "newly_added": False}
def undistort():
    
    for image_file in image_files:
        t1 = time.time()
        #print(cv2.imread(image_file).shape) # Load the image to ensure it exists

        currentlyReading["image_file"] = image_file
        currentlyReading["image_no"] = image_files.index(image_file)
        currentlyReading["newly_added"] = True

        image = raw.raw_to_npArray(image_file)
        undistorted_image = cv2.undistort(image, camera_matrix, dist_coeffs)
        print("UndistortAndCropThese/camShader"+image_file[image_file.index("\\")+1:])
        cv2.imwrite("UndistortAndCropThese/camShader"+image_file[image_file.index("\\")+1:-4]+".png", undistorted_image)
        t2 = time.time()
        print(f"Processed in {t2 - t1:.2f} seconds")
    currentlyReading["image_file"] = None
threading.Thread(target=undistort, daemon=True).start()
gui=np.full((200*3, 200*7, 3), 45, dtype=np.uint8) 
while(currentlyReading["image_file"] is not None):
    if(currentlyReading["newly_added"]):
        currentlyReading["newly_added"] = False
        image_file = currentlyReading["image_file"]
        col = currentlyReading["image_no"]%7
        row= currentlyReading["image_no"]//7
        image = cv2.imread(image_file)
        gui[row*200:row*200+image.shape[0], col*200:col*200+image.shape[1]] = image
    cv2.imshow("UndistortAndCropThese", gui)
    cv2.waitKey(3000)
cv2.destroyAllWindows()    

image_files = [os.path.join(path, name) for path, subdirs, files in os.walk(PATH_TO_YOUR_CROP) for name in files if not "_" in name]
image_files.sort()  # Ensure files are in order
for image_file in image_files:
    image=cv2.imread(image_file)
    image1=image[round(image.shape[0]/2-camera_matrix[1,2]) : , round(image.shape[1]/2-camera_matrix[0,2]) : ]
    print(image.shape, image1.shape)
    cv2.imwrite(image_file[:-4]+"_0.png", image1)