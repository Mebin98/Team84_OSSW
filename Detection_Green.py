import cv2
import numpy as np

def detect_green(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_green = np.array([50, 100, 100])
    upper_green = np.array([70, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)

    green_output = cv2.bitwise_and(image, image, mask=mask)
    return green_output



