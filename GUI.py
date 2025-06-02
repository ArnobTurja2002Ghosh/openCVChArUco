import numpy as np
import cv2
import seaborn as sns
import matplotlib.pyplot as plt
import math
class GUI:
    def __init__(self):
        self.__image_file = None
        self.__image_no = None
        self.__newly_added = False
        self.__gui =np.full((200*3, 200*7, 3), 45, dtype=np.uint8) 
        self.__scatterDF = None
        self.__ax = None
    def add_image(self, image_file, image_no):
        self.__image_file = image_file
        self.__image_no = image_no
        self.__newly_added = True
    def add_scatter(self, scatterDF):
        self.__scatterDF = scatterDF
        
    def create_window(self):
        # Placeholder for window creation logic
        self.window = f"Window with title: {self.title}"
        return self.window
    def reset(self):
        self.__image_file = None
        self.__image_no = None
        self.__newly_added = False
        self.__gui = np.full((200*3, 200*7, 3), 45, dtype=np.uint8)
        self.__scatterDF = None
    def getImageFile(self):
        return self.__image_file
    def getScatterDF(self):
        return self.__scatterDF
    def show(self):
        while(self.__image_file is not None):
            if(self.__newly_added):
                self.__newly_added = False
                image_file = self.__image_file
                col = self.__image_no%7
                row= self.__image_no//7
                image = cv2.imread(image_file)
                self.__gui[row*200:row*200+image.shape[0], col*200:col*200+image.shape[1]] = image
            cv2.imshow(self.__image_file[self.__image_file.index("./")+1: self.__image_file.index("\\")], self.__gui)
            cv2.waitKey(2000)
        cv2.destroyAllWindows() 

    def pltshow(self): 
        self.__ax=sns.scatterplot(data=self.__scatterDF, x="total_points", y="tot_error")
        for i, txt in enumerate(self.__scatterDF["image_files"]):
            if self.__scatterDF["tot_error"][i] < math.ceil(min(self.__scatterDF["tot_error"])):
                self.__ax.annotate(txt[txt.rindex("\\"):], (self.__scatterDF["total_points"][i], self.__scatterDF["tot_error"][i]))
        while self.__scatterDF is not None:
            plt.show(block=False)
            plt.pause(1)
        plt.close()
    def pltclose(self):
        plt.close()
        