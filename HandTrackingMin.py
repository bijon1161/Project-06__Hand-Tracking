# -*- coding: utf-8 -*-
"""
Created on Sat May 29 12:50:12 2021

@author: Admin
"""

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    cv2.imshow("Image",img)
    cv2.waitKey(1)