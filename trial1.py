"""
This is the docstring of the module trial1.py
This module is designed to perform pre-processes to the image,
return the list of co-ordinates on which the robot has to traverse
to go from the start point to the end point of the maze.
This module uses numpy, openCV and various other ready-made modules for processing
"""
import numpy as np
import cv2
import time
from skimage.morphology import *
import preprocessing as process


def prune(skel, start, end, width,height):
                current_start_pos = []
                current_start_pos.append(start[0])
                current_start_pos.append(start[1])
                startx = current_start_pos[0]
                starty = current_start_pos[1]
                endx = end[0]
                endy = end[1]
                print current_start_pos
                mask_matrix = np.array([[0,255,0],[255,255,255]])
                #Declare the background array as numpy array
                #multiply the two arrays and store its result
                #check conditions on the result array
                #Continue the entire code until no neighbouring white found
                #when no neighbour is white, check if your current position is end position, if yes, then stay there.
                #otherwise, just go back to the link place.
                
                    

j = 0
time1=[]
img = cv2.imread("flex-small2.jpg",0)   #Load the image in a grayscale format
while j<10:
        start_time = time.time()
        skeleton = process.preprocess(img)
        #print skeleton
        height, width = img.shape[:2]
        print height, width #height is y axis. width is x axis
        startpoint,endpoint = process.find_start_end(skeleton, width, height)
        print startpoint, endpoint
        #process.display_out(skeleton,"medial")
        #listOfCoOrd =
        prune(skeleton, startpoint, endpoint, width, height)
        time1.append(time.time()-start_time)        
        print(" --%s seconds-- " %(time1[j]))
        j = j+1
average = 0
for timer in time1:
        average = average + timer
print("Total Time is %s" %(average))
average = (average)/j
print("Average Time is %s seconds" %(average))

