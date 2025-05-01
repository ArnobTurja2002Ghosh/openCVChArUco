import json
import os
PATH_TO_YOUR_IMAGES = './calibration_images'
image_files = [os.path.join(PATH_TO_YOUR_IMAGES, f) for f in os.listdir(PATH_TO_YOUR_IMAGES) if f.endswith(".nef")]
image_files.sort()  # Ensure files are in order
def writeUpLookatEye(i, matrix):
    #print("writing", i, "matrix")
    with open('camShader.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    #print(json_object)
    json_object['Data']['Up'] = matrix[:, 0].tolist()
    json_object['Data']['Lookat'] = matrix[:, 1].tolist()
    json_object['Data']['Eye'] = matrix[:, 2].tolist()
    json_object['Data']['Name']= image_files[i][len(PATH_TO_YOUR_IMAGES+"/"):-4]
    #print(json_object)
    with open('camShader'+json_object['Data']['Name']+'.json', 'w') as outfile:
        # Writing to json file
        json.dump(json_object, outfile, indent=4)

def writeDistortion(l1):
    #print("writing", i, "matrix")
    with open('camShader.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    #print(json_object)
    json_object['Data']['radialDistCoeff'] = [l1[0], l1[1], l1[-1]]
    json_object['Data']['tangDistCoeff'] = [l1[2], l1[3]]
    #print(json_object)
    with open('camShader'+'.json', 'w') as outfile:
        # Writing to json file
        json.dump(json_object, outfile, indent=4)