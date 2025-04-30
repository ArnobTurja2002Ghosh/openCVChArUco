from core import VecToso3, MatrixExp3, TransInv, RpToTrans
import numpy as np

def Rodrigues(rvec):
    rvec1=rvec.flatten()
    so3mat = VecToso3(rvec1)
    return MatrixExp3(so3mat)

def TransfInv(rvec, tvec):
    """
    Inverts a homogeneous transformation matrix

    :param rvec: A rotation vector (3x1) representing the rotation part of the transformation matrix.
    :param tvec: A translation vector (3x1) representing the translation part of the transformation matrix.
    :return: The inverse of the transformation matrix
    """
    T1=RpToTrans(Rodrigues(rvec), tvec)
    np.testing.assert_allclose([np.dot(T1[:, 0], T1[:, 1]), np.dot(T1[:, 1], T1[:, 2]), np.dot(T1[:, 2], T1[:, 0])], [0, 0, 0], atol=1e-16, err_msg="The rotation part is not valid.")
    return TransInv(T1)


def Transf_to_UpLookatEye(tmat, up_in_cameraFrame, looking_direction_in_cameraFrame):
    """
    Convert a transformation matrix to a look-at vector, an up vector and an eye vector. 
    :param tmat: The transformation matrix representing transformation of camera{c1} in reference to some frame {c2}.
    :param up_in_cameraFrame: The up vector in the camera frame {c1}.
    :param looking_direction_in_cameraFrame: The looking direction vector in the camera frame {c1}.

    :return: A 3x3 matrix where the first column is the up vector, the second column is the looking direction vector, and the third column is the eye vector, all in the reference frame {c2}.
    """
    up=tmat[:3,:3]@up_in_cameraFrame
    looking_direction=tmat[:3,:3]@looking_direction_in_cameraFrame

    np.testing.assert_almost_equal(np.dot(looking_direction.flatten(), up.flatten()), 0, err_msg="Up and looking direction are not orthogonal.")

    return np.concatenate([up, tmat[:3, 3:4]+looking_direction, tmat[:3, 3:4]], axis=1)


############### Example of the functions in action ###############
## Uncomment the following lines to see the functions in action ##
# rvec = (np.array([[0.02551187], 
#                  [-0.56615859], 
#                  [0.00412808]]),)

# tvec= (np.array([[-108.5218783], 
#                 [-97.22284861], 
#                 [1515.76607254]
#                ]),)

# World_to_ChArUco=np.array([ [1, 0, 0,  0],
#                             [0, -1, 0, 0],
#                             [0, 0, -1, 0],
#                             [0, 0, 0,  1]
#                           ])


# assert len(rvec) == len(tvec), "The rotation vector and translation vector must have the same length."
# for i in range(len(rvec)):
#     print(World_to_ChArUco[:3,:3]@Transf_to_UpLookatEye(TransfInv(rvec[i], tvec[i]), [[0], [-1], [0]], [[0], [0], [1]]), '\n')