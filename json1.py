import json

def writeUpLookatEye(i, matrix):
    #print("writing", i, "matrix")
    with open('camShader.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    #print(json_object)
    json_object['Data']['Up'] = matrix[:, 0].tolist()
    json_object['Data']['Lookat'] = matrix[:, 1].tolist()
    json_object['Data']['Eye'] = matrix[:, 2].tolist()
    #print(json_object)
    with open('camShader_'+str(i)+'.json', 'w') as outfile:
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