# 🧠 openCVChArUco

`openCVChArUco` is an open-source Python project built with OpenCV that focuses on detecting and calibrating cameras using ChArUco markers — a hybrid of ArUco and chessboard markers. The goal is to make it easy for others to learn about marker-based camera calibration, pose estimation, and 3D vision techniques using real-world tools.

This project is intended both for self-learning and to help others understand and experiment with OpenCV's ChArUco tools. Contributions are welcome!

---

## 📸 Features

- Detect ChArUco boards using OpenCV's `cv2.aruco` module
- Calibrate cameras using ChArUco board detection
- Visualize marker corners and IDs on live video
- Compare behavior of ArUco and ChArUco boards
- Save and load camera calibration parameters for reuse

---

## 📦 Dependencies

- Python 3.8+
- OpenCV 4.8.1 (`opencv-contrib-python`)
- NumPy

Install with:

```bash
pip install opencv-contrib-python==4.8.1.78 numpy
```

---

## 🚀 Getting Started
Work on this section is in progress.
1. Create a folder called `calibration_images` which contains all the raw Nikon photos, with nef extension, of a 14*7 ChArUco board to be used used for camera calibration.
2. Run calibration
```bash
python calibrate.py --calibrate images
```
The above command tells the script to calibrate using the images in the `calibration_images` folder. Another possible argument for the calibrate can be:
```bash
python calibrate.py --calibrate colors
```
which tells the script to calibrate using the png images in the [Colors directory](https://github.com/ArnobTurja2002Ghosh/openCVChArUco/tree/main/Colors).
If the script runs successfully, you will see two folders:
1. `detectedMarkersDrawn` containing images with detected markers, corners and axes drawn
2. `undistorted_images` containing undistorted images

## 🔧 Configuration

Check [calibrate.py](https://github.com/ArnobTurja2002Ghosh/openCVChArUco/blob/main/calibrate.py) to modify:
- ChArUco board size (number of squares)
- Marker size vs square size 
- ArUco dictionary (`DICT_4X4_50`, `DICT_5X5_100`, etc.). For now it is hard-coded to `cv2.aruco.DICT_4X4_250`.

---

## 🤝 Contributing

Contributions are welcome!

If you're interested in adding features (Refer to the [Issues](https://github.com/ArnobTurja2002Ghosh/openCVChArUco/issues) for bugs and prospective features in this project), improving usability, or expanding documentation, feel free to open a pull request. Keep the educational purpose in mind: code clarity and comments are appreciated.

Any question regarding this project (even if it is an ELI5 question) can be shot to arnobg2002@gmail.com via email or [Arnob1](https://www.linkedin.com/in/arnob1/) via LinkedIn.

---

## 📄 License

This project is licensed under the **GNU General Public License (GPL-3.0)**.

That means:
- ✅ You can use, modify, and share the code freely.
- ✅ You must credit the original source.
- ❌ If you distribute modified versions, they must also be open-sourced under the same license.
- ❌ You cannot make it closed-source or proprietary.

This helps ensure that all versions of the project remain open and accessible to the community.

---

## 🙋‍♂️ Acknowledgements

This project was built with the help of the following articles, guides, and community answers:

- [Rotation vector vs Rotation matrices](https://medium.com/@sim30217/rotation-vector-vs-rotation-matrices-2b7ab7287b47)
- [Mastering 3D spaces in OpenCV / COLMAP](https://medium.com/red-buffer/mastering-3d-spaces-a-comprehensive-guide-to-coordinate-system-conversions-in-opencv-colmap-ef7a1b32f2df)
- [Reprojection error in OpenCV calibration](https://alphapixeldev.com/opencv-tutorial-part-1-camera-calibration/)
- [Nikon 18-55mm Lens Review](https://photographylife.com/reviews/nikon-18-55mm-dx-vr-af-p/2)
- [Using ChArUco boards in OpenCV](https://medium.com/@ed.twomey1/using-charuco-boards-in-opencv-237d8bc9e40d)
- [argparse Python Tutorial](https://docs.python.org/3/howto/argparse.html#combining-positional-and-optional-arguments)
- [Reading Nikon NEF raw images with rawpy vs imageio](https://stackoverflow.com/questions/60941891/reading-nikon-raw-nef-images-with-rawpy-vs-imageio-in-python)
- [cv2.interpolateCornersCharuco estimation issue](https://stackoverflow.com/questions/73829313/opencv-interpolatecornerscharuco-giving-bad-estimation-when-board-is-partially)
- [Meaning of the retval in cv2.calibrateCamera](https://stackoverflow.com/questions/29628445/meaning-of-the-retval-return-value-in-cv2-calibratecamera)
- [Interpreting reprojection error in OpenCV calibration](https://stackoverflow.com/questions/43878684/interpreting-the-reprojection-error-from-camera-calibration)
- [Discussion of reprojection error discrepancies](https://answers.opencv.org/question/216925/python-ret-value-vastly-different-from-reprojection-error/)
  - Also discussed [here](https://forum.opencv.org/t/false-computation-of-reprojection-error-in-python-camera-calibration-tutorial/7981/5)
- [Calculating Field of View from camera matrix](https://stackoverflow.com/questions/39992968/how-to-calculate-field-of-view-of-the-camera-from-camera-intrinsic-matrix)
- [Sign of k1 and k2 in lens distortion](https://stackoverflow.com/questions/45038476/sign-of-k1-and-k2-of-lens-radial-distortion)
- [Modern Robotics](https://github.com/NxRLab/ModernRobotics/blob/master/packages/Python/modern_robotics/core.py)  
    - Licensed under the MIT License  
    - Copyright (c) 2019 NxRLab 
    - [MIT License Text](https://github.com/NxRLab/ModernRobotics/blob/master/LICENSE)
- [Understanding Lens Distortion](https://learnopencv.com/understanding-lens-distortion/)
- [Camera Calibration Intro Theory](https://euratom-software.github.io/calcam/html/intro_theory.html)
---

Happy learning and posing! 🎯
