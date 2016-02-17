#Python Project for the sem 6 mini project
import numpy as np
import cv2
import time
from skimage.morphology import *
import mahotas

def take_img():
        #Connect to the webcamera
        #take video
        #capture some 10-30fps
        #work on it
        cam = cv2.VideoCapture(0)
        winName = "image"
        s, im = cam.read() # captures image
        cv2.imshow(winName, im) # displays captured image
        cv2.imwrite("test.bmp",im) # writes image test.bmp to disk
        #cv2.waitKey()
        i=0
        while i<3000:
                take_img()
                i=i+1
        
def main():        
        #Step 1: Read the image and convert it to greyscale
        # Load an Color Image of the Maze
        img = cv2.imread("maze2.bmp",0)
        length = img[0].size
        height = (img.size)/length
        equ = cv2.equalizeHist(img)
        #print length,height
        
        #Step 2: Blur the image to fine tune its edges
        blur = cv2.blur(equ,(5,5))
        #Blurring the Image Done.


        #Step 4: Apply Thresholding to the Image
        
        ret,thres_img = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)

        #Thresholding Done

        
        #Step 5: Apply Skeletonization to the Image
        
        median = medial_axis(thres_img).astype(np.uint8)
        ret,final2 = cv2.threshold(median,0,255,cv2.THRESH_BINARY)

        #Step 6: Prune the Image to remove the excessive Stuff

        
        
        #Pruning Done
        #prun = pruning(final2,length,height)
        #prun2= final2-prun2
        #Step 7: Display and Check Accuracy of the Detected Path
        res = np.hstack((img,equ,blur))
        res2 = np.hstack((thres_img,final2)) 
        cv2.imshow('orig,histo,blur',res)
        cv2.imshow("Threshold, skeleton",res2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        #Display Complete.
take_img()
j = 0
time1=[]
while j<20:
        start_time = time.time()
        main()
        time1.append(time.time()-start_time)        
        print(" --%s seconds-- " %(time1[j]))
        j = j+1
average = 0
for timer in time1:
        average = average + timer
print("Total Time is %s" %(average))
average = (average)/j
print("Average Time is %s seconds" %(average))

