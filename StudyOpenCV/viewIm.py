'''
Created on 18 окт. 2021 г.

@author: Alex
'''
import settings
import cv2

#===============================================================================
# image = cv2.imread(r"C:\Users\Alex\Desktop\python\openCV\testFaces.jpg")
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#===============================================================================

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = settings.getFromSetting('image_path')
path_filter = settings.getFromSetting('path_filter')
face_cascade = cv2.CascadeClassifier(path_filter)
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor= 1.1,
    minNeighbors= 5,
    minSize=(10, 10)
)
faces_detected = r"Лиц обнаружено: " + format(len(faces))
print(faces_detected)
# Рисуем квадраты вокруг лиц
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
viewImage(image,faces_detected)