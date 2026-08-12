import cv2 as cv

video = cv.VideoCapture(0)

video.set(cv.CAP_PROP_FRAME_WIDTH, 640)  # largura
video.set(cv.CAP_PROP_FRAME_HEIGHT, 480)  # altura
video.set(cv.CAP_PROP_BRIGHTNESS, 200)  # brilho da camera

while True:
    check, img = video.read()

    cv.imshow("video", img)
    if cv.waitKey(15) & 0xFF == ord("q"):
        break

video.release()
cv.destroyAllWindows()
