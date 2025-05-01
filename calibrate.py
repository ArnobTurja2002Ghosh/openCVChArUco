import cv2
import os
import numpy as np
import json1
import rawpy
import argparse
from core import TransInv, RpToTrans
import seaborn as sns
import matplotlib.pyplot as plt 
import project_points
import shutil
# ------------------------------
# ENTER YOUR REQUIREMENTS HERE:
ARUCO_DICT = cv2.aruco.DICT_4X4_250

SQUARE_LENGTH = 10
MARKER_LENGTH = 7
# ...
PATH_TO_YOUR_IMAGES = './calibration_images'
# ------------------------------

print("We are using openCV version", cv2.__version__)

def TransfInv(rvec, tvec):
    """
    Inverts a homogeneous transformation matrix

    :param rvec: A rotation vector (3x1) representing the rotation part of the transformation matrix.
    :param tvec: A translation vector (3x1) representing the translation part of the transformation matrix.
    :return: The inverse of the transformation matrix
    """
    T1=RpToTrans(cv2.Rodrigues(rvec)[0], tvec)
    np.testing.assert_allclose([np.dot(T1[:, 0], T1[:, 1]), np.dot(T1[:, 1], T1[:, 2]), np.dot(T1[:, 2], T1[:, 0])], [0, 0, 0], atol=1e-15, err_msg="The rotation part is not valid.")
    return TransInv(T1)


def Transf_to_UpLookatEye(tmat, up_in_cameraFrame, looking_direction_in_cameraFrame):
    """
    Convert a transformation matrix to a look-at vector, an up vector and an eye vector. 
    :param tmat: The transformation matrix representing transformation of camera{c1} in reference to some frame {c2}.
    :param up_in_cameraFrame: The up vector in the camera frame {c1}.
    :param looking_direction_in_cameraFrame: The looking direction vector in the camera frame {c1}.

    :return: A 3x3 matrix where the first column is the up vector, the second column is the lookat point, and the third column is the eye point, all in the reference frame {c2}.
    """
    up=tmat[:3,:3]@up_in_cameraFrame
    looking_direction=tmat[:3,:3]@looking_direction_in_cameraFrame

    np.testing.assert_almost_equal(np.dot(looking_direction.flatten(), up.flatten()), 0, err_msg="Up and looking direction are not orthogonal.")

    return np.concatenate([up, tmat[:3, 3:4]+looking_direction, tmat[:3, 3:4]], axis=1)

def generateCharuco(columns, rows, square_length, marker_length, ratio):
    dictionary = cv2.aruco.getPredefinedDictionary(ARUCO_DICT)
    board = cv2.aruco.CharucoBoard((columns, rows), square_length, marker_length, dictionary)
    if(ratio=='letter'):
        img = cv2.aruco.CharucoBoard.generateImage(board, (3300, 2550), marginSize=802)
        cv2.imwrite("charuco_3300_2550_802.png", img)
    elif(ratio=='lg16'):
        img = cv2.aruco.CharucoBoard.generateImage(board, (3840, 2160), marginSize=240)
        cv2.imwrite("charuco_3840_2160_240.png", img)

def drawDetectedCornersCharuco(img, corners, ids):
    """
    Draw rectangles and IDs to the corners, wrapper

    Parameters
    ----------
    img : numpy.array()
        Two dimensional image matrix. Image can be grayscale image or RGB image
        including 3 layers. Allowed shapes are (x, y, 1) or (x, y, 3).
    corners : numpy.array()
        Checkerboard corners.
    ids : numpy.array()
        Corners' IDs.
    """
    if ids.size > 0:
        id_color = (255, 255, 0)
        # corners = corners.reshape((corners.shape[0], 1, corners.shape[1]))
        # ids = ids.reshape((ids.size, 1))
        cv2.aruco.drawDetectedCornersCharuco(img, corners, ids, id_color)

def calibrate_and_save_parameters():
    # Define the aruco dictionary and charuco board
    dictionary = cv2.aruco.getPredefinedDictionary(ARUCO_DICT)
    board = cv2.aruco.CharucoBoard((14, 7), 341.4/16, (341.4/16)*0.7, dictionary)
    #print(board.getChessboardCorners())
    params = cv2.aruco.DetectorParameters()

    # Load PNG images from folder
    image_files = [os.path.join(PATH_TO_YOUR_IMAGES, f) for f in os.listdir(PATH_TO_YOUR_IMAGES) if f.endswith(".nef")]
    image_files.sort()  # Ensure files are in order
    #print("image files", image_files)
    all_charuco_corners = []
    all_charuco_ids = []
    every_charuco_ids_len =[]
    

    shutil.rmtree('./detectedMarkersDrawn')
    newpath = './detectedMarkersDrawn'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    for image_file in image_files:
        image = raw_to_npArray(image_file)
        #image=cv2.imread(image_file)
        #print("I am reading image of length", image.shape)
        #print(image.shape, Image.open("0.png").size)
        image_copy = image.copy()
        #image_copy=cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("meh", image_copy)
        # cv2.waitKey(0)
        marker_corners=[]
        marker_ids=np.array([])
        marker_corners, marker_ids, _= cv2.aruco.detectMarkers(image, dictionary, parameters=params)

        #marker_corners1, marker_ids1, _= cv2.aruco.detectMarkers(image_rawpy, dictionary, parameters=params)

        # print(marker_corners)
        #print(marker_ids)
        print('reading', image_file)
        print(len(marker_corners)==len(marker_ids), len(marker_ids)==60)
        
        # If at least one marker is detected
        if len(marker_ids) > 0:
            cv2.aruco.drawDetectedMarkers(image_copy, marker_corners, marker_ids)
            
            
            #board.setLegacyPattern(True)
            #print('\n marker corners \n', marker_corners, '\n marker ids \n', marker_ids)
            charuco_retval, charuco_corners, charuco_ids = cv2.aruco.interpolateCornersCharuco(marker_corners, marker_ids, image, board)
            #print('retval', charuco_retval, 'charuco ids length', charuco_ids)
            drawDetectedCornersCharuco(image_copy, charuco_corners,
                                   charuco_ids)
            cv2.imwrite("detectedMarkersDrawn/"+image_file[21:-4]+".png", image_copy)
            print('done drawing')
            if charuco_retval:
                all_charuco_corners.append(charuco_corners)
                all_charuco_ids.append(charuco_ids)
                every_charuco_ids_len.append(len(charuco_ids))
    good_images=[]
    for i in range(len(image_files)):
        if(every_charuco_ids_len[i]>=70):
            good_images.append(image_files[i])
    
    sns.barplot({"image": list(map(lambda x:x[len(PATH_TO_YOUR_IMAGES+"/"): -4],image_files)), "number of corners detected": every_charuco_ids_len}, x="image", y="number of corners detected")
    plt.show()
    # Calibrate camera
    #print("\n All ChAruCo ids \n", all_charuco_ids, "\n All ChArUco corners \n", all_charuco_corners)
    retval, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.aruco.calibrateCameraCharuco(all_charuco_corners, all_charuco_ids, board, image.shape[:2], None, None)
    json1.writeDistortion(dist_coeffs.flatten())
    project_points.JosepBosch(board, camera_matrix, dist_coeffs, rvecs, tvecs, all_charuco_corners, all_charuco_ids)
    # Save calibration data
    np.save('camera_matrix.npy', camera_matrix)
    np.save('dist_coeffs.npy', dist_coeffs)

    print("retval", retval, '\n Camera Matrix', camera_matrix, '\n', "Distortion coeff", dist_coeffs, '\n RVec', rvecs, '\n TVec', tvecs, '\n Rotation Matrix', cv2.Rodrigues(rvecs[0])[0])
    # print('Translation of the camera in reference to the Charuco', -cv2.Rodrigues(rvecs[0])[0].T @ tvecs[0])
    # print('Rotation of the camera in reference to the Charuco', cv2.Rodrigues(rvecs[0])[0].T)

    World_to_ChArUco=np.array([ [1, 0, 0,  0],
                                [0, -1, 0, 0],
                                [0, 0, -1, 0],
                                [0, 0, 0,  1]
                              ])


    assert len(rvecs) == len(tvecs), "The rotation vector and translation vector must have the same length."
    for i in range(len(rvecs)):
        print('\n', image_files[i], '\n', World_to_ChArUco[:3,:3]@Transf_to_UpLookatEye(TransfInv(rvecs[i], tvecs[i]), [[0], [-1], [0]], [[0], [0], [1]]), '\n')
        json1.writeUpLookatEye(i, World_to_ChArUco[:3,:3]@Transf_to_UpLookatEye(TransfInv(rvecs[i], tvecs[i]), [[0], [-1], [0]], [[0], [0], [1]]))
    # Iterate through displaying all the images
    for image_file in image_files:
        image = raw_to_npArray(image_file)
        undistorted_image = cv2.undistort(image, camera_matrix, dist_coeffs)
        # cv2.imshow('Undistorted Image', undistorted_image)
        # cv2.waitKey(0)
        cv2.imwrite("undistorted_images/"+image_file[21:-4]+".png", undistorted_image)

    #cv2.destroyAllWindows()
def raw_to_npArray(image_file):
    raw = rawpy.imread(image_file)
    image_rawpy = raw.postprocess()
    cv2.imwrite("unconverted"+".png", image_rawpy)
    image = cv2.cvtColor(image_rawpy, cv2.COLOR_RGB2BGR)
    cv2.imwrite("converted"+".png", image)
    return image

def compareMarkerCorners(marker_corners, marker_corners1):
    for i in range(17):
        if(np.allclose(marker_corners[i] , marker_corners1[i])):
            print('rgb and bgr gives same result')
        else:
            print('rgb and bgr gives different results')
            print('bgr gives:', marker_corners[i], '\n', 'rgb gives:', marker_corners1[i])
#calibrate_and_save_parameters()
parser = argparse.ArgumentParser(description="Camera calibration script")
parser.add_argument("--generate", action='store_true', help='generate ChArUco')
parser.add_argument("--columns", type=int)
parser.add_argument("--rows", type=int)
parser.add_argument("--square_length", type=float)
parser.add_argument("--marker_length", type=float)
parser.add_argument("--ratio", type=str)
args = parser.parse_args()
if(args.generate):
    generateCharuco(args.columns, args.rows, args.square_length, args.marker_length, args.ratio)
else:
    calibrate_and_save_parameters()