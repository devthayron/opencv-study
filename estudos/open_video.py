import cv2 as cv

# reproduzir o video
video = cv.VideoCapture("media/runners.mp4")

while True:
    check, img = video.read()
    # print(img.shape)
    img_redimencionada = cv.resize(img, (640, 420))  # redimencionar

    cv.imshow("video", img)
    if cv.waitKey(15) & 0xFF == ord("q"):
        break

video.release()
cv.destroyAllWindows()
