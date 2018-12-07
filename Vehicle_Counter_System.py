import cv2
import numpy as np
import time
import datetime


cap = cv2.VideoCapture('Relaxing Traffic.mp4')
#cap = cv2.VideoCapture(0)
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

def CarDetect():
    global count1
    global count2
    global count3
    global count4
    global count5
    
    for contour in contours:
        area = cv2.contourArea(contour)
       
        (x, y, w, h) = cv2.boundingRect(contour)
        
        cv2.rectangle(frame2,(x, y), (x + w, y + h),(0,255,0),2)
        
        centroid = get_centroid(x,y,w,h)
        centroidX = centroid[0]
        centroidY = centroid[1]

        #def countingcar(centroidX,centroidY):
        
        if(100<centroidX<200 and 480<centroidY<500):
       
            count1 = count1 + 1
            #print(count1)

        elif(300<centroidX<400 and 480<centroidY<500):
            count2 = count2 + 1
            #print(count2)

        elif(500<centroidX<600 and 480<centroidY<500):
            count3 = count3 + 1
            #print(count3)

        elif(700<centroidX<800 and 480<centroidY<500):
            count4 = count4 + 1
            #print(count4)

        elif(900<centroidX<1000 and 480<centroidY<500):
            count5 = count5 + 1
            #print(count5)

     
        
  
        cv2.line(frame2,(100,500),(200,500),(255,0,0),6)
        cv2.putText(frame2, ":{}".format(count1), (100, 500),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.line(frame2,(300,500),(400,500),(255,0,0),6)
        cv2.putText(frame2, ":{}".format(count2), (300, 500),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.line(frame2,(500,500),(600,500),(255,0,0),6)
        cv2.putText(frame2, ":{}".format(count3), (500, 500),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.line(frame2,(700,500),(800,500),(255,0,0),6)
        cv2.putText(frame2, ":{}".format(count4), (700, 500),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.line(frame2,(900,500),(1000,500),(255,0,0),6)
        cv2.putText(frame2, ":{}".format(count5), (900, 500),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
       
        


        
def get_centroid(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)

    cx = x + x1
    cy = y + y1


    return (cx, cy)
 




while True:
    _,frame1 = cap.read()
    _,frame2 = cap.read()
    grayFrame1 = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    grayFrame2 = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    gauBlur1 = cv2.GaussianBlur(grayFrame1,(21,21),0)
    gauBlur2 = cv2.GaussianBlur(grayFrame2,(21,21),0)
    difference = cv2.absdiff(gauBlur1,gauBlur2)
    ret, thresh = cv2.threshold(difference, 10, 255, cv2.THRESH_BINARY)
    thresh = cv2.dilate(thresh, None, iterations=2)
    thresh = cv2.erode(thresh,None,iterations=2)
    _,contours,hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
   

   
    frame2 = frame1
    CarDetect()
   

    
  
    

    cv2.imshow("Frame1",frame1)
    #cv2.imshow("Frame2",frame2)
    #cv2.imshow("Difference",difference)
    #cv2.imshow("Thresh",thresh)
    #cv2.imshow("blur",gauBlur1)
    #cv2.imshow("contour",contours)

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
