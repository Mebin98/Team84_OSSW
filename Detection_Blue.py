import cv2
import numpy as np

def detect_blue(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    blue_output = cv2.bitwise_and(image, image, mask=mask)
    return blue_output


