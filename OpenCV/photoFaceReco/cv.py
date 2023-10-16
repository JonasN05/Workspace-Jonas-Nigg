import cv2


cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


img = cv2.imread("face.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = cascade.detectMultiScale(img_gray)
for x,y, width, height in faces:
    cv2.rectangle(img ,(x,y),(x+width,y+height), color=(255,0,0), thickness=5)
cv2.imshow("Kamera", img)

cv2.waitKey(0)
cv2.destroyWindow()