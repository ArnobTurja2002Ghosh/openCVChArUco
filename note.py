import os
less_than_2= ['./detectedMarkersDrawn\\0_5.png', './detectedMarkersDrawn\\15_5.png',
               './detectedMarkersDrawn\\16_5.png', './detectedMarkersDrawn\\18_5.png', 
                './detectedMarkersDrawn\\1_5.png', './detectedMarkersDrawn\\2_4.png', 
                './detectedMarkersDrawn\\3_3.png', './detectedMarkersDrawn\\4.png',
                './detectedMarkersDrawn\\4_3.png', './detectedMarkersDrawn\\4_4.png', 
                './detectedMarkersDrawn\\4_5.png', './detectedMarkersDrawn\\5_4.png', 
                './detectedMarkersDrawn\\5_5.png', './detectedMarkersDrawn\\6_5.png', 
                './detectedMarkersDrawn\\7_4.png', './detectedMarkersDrawn\\7_5.png', 
                './detectedMarkersDrawn\\8_2.png', './detectedMarkersDrawn\\8_4.png', 
                './detectedMarkersDrawn\\9_2.png', './detectedMarkersDrawn\\9_3.png', 
                './detectedMarkersDrawn\\9_4.png']
PATH_TO_YOUR_IMAGES = './calibration_images'
for i,j in enumerate(less_than_2):
    less_than_2[i] = j[23:-4]+".nef"
less_than_2 = [os.path.join(PATH_TO_YOUR_IMAGES, f) for f in less_than_2]
less_than_2.sort()
for i in range(len(less_than_2)):
    os.rename(less_than_2[i], os.path.join("./lessThan2RPE",less_than_2[i][21:]))