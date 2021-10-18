'''
Created on 18 окт. 2021 г.

@author: Alex
'''
import cv2

image = cv2.imread("C:\Users\Alex\Desktop\python\openCV\testFaces.jpg")
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()