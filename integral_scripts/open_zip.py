import zipfile
import cv2
import numpy as np
# Path to the zip file and the image inside it
zip_path = 'chessboard.lf'
image_name = 'chessboard.png'

# Open the zip file and extract the image as a cv2 image
with zipfile.ZipFile(zip_path, 'r') as zf:
    with zf.open(image_name) as image_file:
        # Read the image file into a numpy array
        image_data = np.frombuffer(image_file.read(), dtype=np.uint8)
        # Decode the image data to a cv2 image
        img = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

print("Image shape:", img.shape)
imge = cv2.imread('Test.png')
cv2.imwrite('Result.png', cv2.absdiff(imge, img))