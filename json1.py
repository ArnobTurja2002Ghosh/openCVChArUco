import json
import os
import cv2
import raw
PATH_TO_YOUR_IMAGES = './calibration_images'
PATH_TO_YOUR_COLORS = './Colors'
PATH_TO_YOUR_PAIRED = './pairedImages'
def getImageFiles(calibrate):
    # Load PNG images from folder
    if(calibrate=="images"):
        image_files = [os.path.join(PATH_TO_YOUR_IMAGES, f) for f in os.listdir(PATH_TO_YOUR_IMAGES) if f.endswith(".nef")]
    elif(calibrate=="colors"):
        image_files = [os.path.join(path, name) for path, subdirs, files in os.walk(PATH_TO_YOUR_COLORS) for name in files]
    elif(calibrate=="paired"):
        image_files = [os.path.join(path, name) for path, subdirs, files in os.walk(PATH_TO_YOUR_PAIRED) for name in files if name.endswith("_0.nef")]
    image_files.sort()  # Ensure files are in order
    return image_files
def writeUpLookatEye(calibrate, i, matrix):
    image_files = getImageFiles(calibrate)
    #print("writing", i, "matrix")
    image = raw.raw_to_npArray(image_files[i])
    with open('CameraShaders/camShader.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    #print(json_object)
    json_object['Data']['Res'] = [image.shape[1], image.shape[0]]
    json_object['Data']['Up'] = matrix[:, 0].tolist()
    json_object['Data']['Lookat'] = matrix[:, 1].tolist()
    json_object['Data']['Eye'] = matrix[:, 2].tolist()
    if calibrate=="paired":
        json_object['Data']['Name']= image_files[i][len(PATH_TO_YOUR_PAIRED+"/"):image_files[i].rfind("\\")]
    else:
        json_object['Data']['Name']= image_files[i][len(PATH_TO_YOUR_IMAGES+"/"):-4]
    #print(json_object)
    with open('CameraShaders/camShader'+json_object['Data']['Name']+'.json', 'w') as outfile:
        # Writing to json file
        json.dump(json_object, outfile, indent=4)
    with open('JsonStructure.json', 'r') as openfile:
        # Reading from json file
        json_object1 = json.load(openfile)
        json_object1['cameraConfig'].append('Default\\CameraShaders\\camShader'+json_object['Data']['Name']+'.json')
    with open('JsonStructure.json', 'w') as outfile:
        # Writing to json file
        json.dump(json_object1, outfile, indent=4)

def writeDistortion(l1):
    #print("writing", i, "matrix")
    with open('CameraShaders/camShader.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    #print(json_object)
    #json_object['Data']['radialDistCoeff'] = [l1[0], l1[1], l1[-1]]
    #json_object['Data']['tangDistCoeff'] = [l1[2], l1[3]]
    json_object['Data']['radialDistCoeff'] = [0, 0, 0]
    json_object['Data']['tangDistCoeff'] = [0, 0, 0]
    #print(json_object)
    with open('CameraShaders/camShader'+'.json', 'w') as outfile:
        # Writing to json file
        json.dump(json_object, outfile, indent=4)
    with open('JsonStructure.json', 'r') as openfile:
        # Reading from json file
        json_object1 = json.load(openfile)
        json_object1['cameraConfig']=[]
    with open('JsonStructure.json', 'w') as outfile:
        # Writing to json file
        json.dump(json_object1, outfile, indent=4)