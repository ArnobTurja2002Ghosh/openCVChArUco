import rawpy
import cv2
def raw_to_npArray(image_file):
    raw = rawpy.imread(image_file)
    image_rawpy = raw.postprocess()
    #cv2.imwrite("unconverted"+".png", image_rawpy)
    image = cv2.cvtColor(image_rawpy, cv2.COLOR_RGB2BGR)
    #cv2.imwrite("converted"+".png", image)
    return image