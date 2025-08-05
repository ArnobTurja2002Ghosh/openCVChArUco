import cv2
import numpy as np
import integral_to_quilt
import gridMaker
import argparse
n = 81

def random_colors():
    # Make an image: one row of color blocks
    colors = np.random.randint(256, size=(81, 3)) #[tuple(random.randint(0, 255) for _ in range(3)) for _ in range(n)]
    img = np.zeros((455, 66339, 3), dtype=np.uint8)
    for i in range(img.shape[1]):
        img[:, i, :] = np.array(colors[i%81][:3]) # Convert to RGB and scale to 0-255
        
    # Save the image
    cv2.imwrite("random_colors.png", img)
    final_img=integral_to_quilt.convert("random_colors.png", 819, 81) # Convert the image to a quilt
    final_img.save('converted_quilt.png')
    gridMaker.convert(81, 9, 9, "converted_quilt") # Create a grid from the quilt
#print(np.random.randint(256, size=(4, 6, 3), dtype=np.uint8))
def random_images():
    img= np.random.randint(256, size=(455, 66339, 3), dtype=np.uint8)
    cv2.imwrite("random_image.png", img)
    final_img=integral_to_quilt.convert("random_image.png", 819, 81) # Convert the image to a quilt
    final_img.save('converted_quilt.png')
    gridMaker.convert(81, 9, 9, "converted_quilt") # Create a grid from the quilt
parser = argparse.ArgumentParser(description="Integral Image to quilt script")
parser.add_argument("--random", type=str, default="color")
args = parser.parse_args()
if args.random == "color":
    random_colors()
elif args.random == "image":
    random_images()