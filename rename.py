import os
import argparse
PATH_TO_YOUR_IMAGES = './calibration_images'
image_files = [os.path.join(PATH_TO_YOUR_IMAGES, f) for f in os.listdir(PATH_TO_YOUR_IMAGES) if f.endswith(".nef")]
def add_extra_character(extra_character):
    for image_file in image_files:
        os.rename(image_file, image_file[:-4]+"_"+extra_character+image_file[-4:])

parser = argparse.ArgumentParser(description="Rename calibration images")
parser.add_argument("--extra_character", type=str)
args = parser.parse_args()
add_extra_character(args.extra_character)