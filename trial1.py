#Python Project for the sem 6 mini project
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
        ret,thres_img = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)   #Threshold image is saved in thres_img

        mid = medial_axis(thres_img).astype(np.uint8)        #Perform Skeletonization of the threshold image, using Medial Axis Theorem
        ret,mid = cv2.threshold(mid,0,255,cv2.THRESH_BINARY)

        return mid

        #OUTPUT STAGES
        
        #prun = pruning(final2,length,height)
        #prun2= final2-prun2
        #Step 7: Display and Check Accuracy of the Detected Path
        #cv2.imshow("orig",img)
        #cv2.imshow("blur", blur)
        #cv2.imshow("thres_img",thres_img)
        #cv2.imshow("final skel using median axis", final2)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        #Display Complete.

        
j = 0
time1=[]
while j<20:
        start_time = time.time()
        img = cv2.imread("flex-small3.jpg",0)   #Load the image in a grayscale format
        skeleton = preprocess(img)
        time1.append(time.time()-start_time)        
        print(" --%s seconds-- " %(time1[j]))
        j = j+1
average = 0
for timer in time1:
        average = average + timer
print("Total Time is %s" %(average))
average = (average)/j
print("Average Time is %s seconds" %(average))

