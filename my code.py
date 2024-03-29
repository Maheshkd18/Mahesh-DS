3# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 22:48:30 2023

@author: darpan
"""

import cv2 
from tracker import *

tracker = EuclideanDistTracker()

cap = cv2.VideoCapture(r'C:\Users\darpa\OneDrive\Desktop\python\classroom notes and task\74 14 jul Azur, Object tracking\object_tracking\highway.mp4')

object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

while True:
    ref, frame = cap.read()
    height, width, _ = frame.shape
    
    #Extract region of interest
    roi = frame[340: 720, 500: 800]
    
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    
    for i in contours:
        area = cv2.contourArea(i)
        
        if area>100:
            
            x, y, w, h = cv2.boundingRect(i)
            
            detections.append([x,y,w,h])
            
    # Object Tracking
    
    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2. rectangle(roi, (x,y), (x+w, y+h), (0, 255, 0), 3)
    
    cv2.imshow('roi', roi)
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    
    key = cv2.waitKey(30)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()