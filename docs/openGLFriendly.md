 OpenCV uses a translation vector (tvec) and rotation vector (rvec) to represent a pose but in the json files in this project you will not find any tvec or rvec. This is because in OpenGL after a matrix is initialized (identity matrix), the viewing transformation can be specified in several ways and rvecs/tvecs is not one of the ways (well... unless you create your own utility routine). A way to manufacture a viewing transformation is to use the Utility Library routine **gluLookAt()** to define a line of sight. This routine encapsulates a series of rotation and translation commands.The arguments for this command indicate
    - where the camera (or eye position) is placed
    - where it is aimed
    - which way is up
    
Often, programmers construct a scene around the origin or some other convenient location and then want to look at it from an arbitrary point to get a good view of it. As its name suggests, the **gluLookAt()** utility routine is designed for just this purpose. It takes three sets of arguments, which specify the location of the viewpoint, define a reference point toward which the camera is aimed, and indicate which direction is up.
    
<table>
      <tr>
        <th> From OpenGL </th>
        <th> From our json </th>
      </tr>
      <tr>
        <td>
          void gluLookAt(	GLdouble eyeX, 
                         	GLdouble eyeY,
                         	GLdouble eyeZ, <br/>
                         	GLdouble centerX,
                         	GLdouble centerY,
                         	GLdouble centerZ, <br/>
                         	GLdouble upX,
                         	GLdouble upY,
                         	GLdouble upZ);
        </td>
        <td>
          "Eye": [
              eyeX,
              eyeY,
              eyeZ
          ], <br/>
          "Lookat": [
              centerX,
              centerY,
              centerZ
          ], <br/>
          "Up": [
              upX,
              upY,
              upZ
          ],
        </td>
      </tr>
</table>
    
- The desired viewpoint is specified by eyeX, eyeY, and eyeZ
- The centerX, centerY, and centerZ arguments specify any point along the desired line of sight
- The upX, upY, and upZ arguments indicate which direction is up

Information about OpenGL in this documentation have been taken from chapter-3 of [this book](https://www.amazon.ca/OpenGL%C2%AE-Programming-Guide-Official-Learning/dp/0201604582)
