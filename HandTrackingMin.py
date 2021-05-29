# -*- coding: utf-8 -*-
"""
Created on Sat May 29 12:50:12 2021

@author: Admin
"""

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    
    cv2.imshow("Image",img)
    cv2.waitKey(1)