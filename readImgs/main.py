import cv2 as cv

#Reading images

""" img = cv.imread("./imgs/img1.jpg")

cv.imshow('Cars',img)

"""

#Reading videos

capture = cv.VideoCapture('./videos/video1.mp4')

while (True):
    isTrue, frame = capture.read()
    if not isTrue:
        print("Archivo no leido")
        break
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF== ('d'):
        break

capture.release()
cv.destroyAllWindows()