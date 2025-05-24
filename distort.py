import cv2
import numpy as np
import os
PATH_TO_YOUR_COLORS = './Colors'
def distort_image(img, camera_matrix, dist_coeffs):
    h, w = img.shape[:2]
    
    # Step 1: Generate normalized coordinates
    x, y = np.meshgrid(np.arange(w), np.arange(h))
    x = x.astype(np.float32)
    y = y.astype(np.float32)
    
    # Normalize using camera intrinsics
    x_norm = (x - camera_matrix[0, 2]) / camera_matrix[0, 0]
    y_norm = (y - camera_matrix[1, 2]) / camera_matrix[1, 1]
    
    # Apply distortion to normalized points
    r2 = x_norm**2 + y_norm**2
    k1, k2, p1, p2, k3 = dist_coeffs.ravel()
    
    radial = 1 + k1*r2 + k2*r2**2 + k3*r2**3
    x_dist = x_norm * radial + 2*p1*x_norm*y_norm + p2*(r2 + 2*x_norm**2)
    y_dist = y_norm * radial + p1*(r2 + 2*y_norm**2) + 2*p2*x_norm*y_norm
    
    # Convert back to pixel coordinates
    x_pixel = x_dist * camera_matrix[0, 0] + camera_matrix[0, 2]
    y_pixel = y_dist * camera_matrix[1, 1] + camera_matrix[1, 2]
    
    # Stack and remap
    map_x = x_pixel.astype(np.float32)
    map_y = y_pixel.astype(np.float32)
    distorted = cv2.remap(img, map_x, map_y, interpolation=cv2.INTER_LINEAR)
    
    return distorted
def applyDistortion():
    image_files = [os.path.join(path, name) for path, subdirs, files in os.walk(PATH_TO_YOUR_COLORS) for name in files]
        
    image_files.sort()
    for i,j in enumerate(image_files):
        img = cv2.imread(j)
        dist_coeffs=np.load('dist_coeffs.npy')
        camera_matrix=np.load('camera_matrix.npy')
        distorted = distort_image(img, camera_matrix, dist_coeffs)
        cv2.imwrite("DistortedColors\\"+j[j.rindex("\\"):], distorted)

applyDistortion()
