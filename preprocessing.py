import numpy as np
import cv2
import time
from skimage.morphology import *


def preprocess(img):        
		'''
		This function will process the passed image and return the skeleton of the image.
		The function consists of 1 parameter
		'''
		blur = cv2.blur(img,(5,5))      #Blurring the Image Done.
		ret3,thres_img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) #Threshold image is saved in thres_img. Threshold Value used is stored in ret
		mid = medial_axis(thres_img).astype(np.uint8)        	#Perform Skeletonization of the threshold image, using Medial Axis Theorem
		ret,mid = cv2.threshold(mid,0,255,cv2.THRESH_BINARY)	#Convert the obtained skeleton to the binary form.
		return mid

def display_out(img,title):
                '''
		This function will display the image 'img' in the window as created using OpenCV function imshow.
		The title of the window is also passed using string 'title' '''
                cv2.imshow(title,img)
                #cv2.waitKey(0)
                cv2.destroyAllWindows()



def find_start_end(skel,width,length):              #length is y axis. width is x axis
                '''
                This function will process the skeleton of the original captured image.
                The result of this function would be a pruned image, which would essentially be the path to be traversed by the bot on the maze.
                '''
                x_ax= 0
                flag = 0
                start = []
                while flag == 0:
                    for i in range(0,length - 1):
                        if skel[i][x_ax] == 255:    #image is iterated through pixel position "x_ax, y_ax" thus we need to rotate the image 
                            flag = 1
                            if ((skel[i+1][x_ax] == 255) or(skel[i-1][x_ax] == 255) or(skel[i+1][x_ax+1] == 255) or\
                                (skel[i-1][x_ax+1] == 255) or(skel[i][x_ax+1] == 255) or(skel[i-1][x_ax-1] != 255) or\
                                (skel[i][x_ax-1] != 255) or(skel[i+1][x_ax-1] != 255)):
                                start = [x_ax, i]
                            else:
                                flag = 0
                                
                    if flag == 0:
                        x_ax = x_ax + 1
                        
                            
                x_ax = 0
                end = []
                flag = 0
                while flag == 0:
                    for i in range(0,length-1):
                        if skel[i][width - (x_ax+1)] == 255:
                            flag = 1
                            end = [width-x_ax,i]
                    if flag == 0:
                        x_ax = x_ax +1
                return start, end
                        

