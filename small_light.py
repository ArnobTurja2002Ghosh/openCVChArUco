import cv2
import shutil
import os

PATH_TO_YOUR_CROP = './UndistortAndCropThese'
# def remove_existing_mini_dora():
    
#     image_files = [os.path.join(path, name) for path, subdirs, files in os.walk(PATH_TO_YOUR_CROP) for name in files]
#     image_files.sort()  # Ensure files are in order
#     for image_file in image_files:
#         if os.path.exists(os.path.join(os.path.dirname(image_file),"mini_dora")):
#             shutil.rmtree(os.path.join(os.path.dirname(image_file),"mini_dora"))
#             print("Removed existing mini_dora directory for:", image_file)
def create_mini_dora():
    image_files = [os.path.join(path, name) for path, subdirs, files in os.walk(PATH_TO_YOUR_CROP) for name in files]
    image_files.sort()  # Ensure files are in order
    for image_file in image_files:
        image1 = cv2.imread(image_file)
        image2=cv2.resize(image1, (image1.shape[1]//10, image1.shape[0]//10))
        if not os.path.exists(os.path.join("mini_dora", os.path.dirname(image_file))):
            os.makedirs(os.path.join("mini_dora", os.path.dirname(image_file)))
        
        cv2.imwrite(os.path.join("mini_dora", os.path.dirname(image_file), os.path.basename(image_file)), image2)
        print("Processed:", os.path.join("./mini_dora", image_file[image_file.index("\\")+1:]))
create_mini_dora()
#remove_existing_mini_dora()