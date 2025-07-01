In the line where we define a ChArUco board:
```
board = cv2.aruco.CharucoBoard((14, 7), 341.4/16, (341.4/16)*0.7, dictionary)
```
We have to input the size of a square and the size of a marker alongside other arguments. There are two ways to measure the size of a square: either measure the size of one square, or measure the size of a side of the board and divide it by the number of squares on that side. In which unit you will measure is completely your choice but just keep in mind that the translation vectors from OpenCV or the `Eye` output from the scripts in this projects will be in the same unit of measurement.
>For with the measure you use it will be measured back to you.

