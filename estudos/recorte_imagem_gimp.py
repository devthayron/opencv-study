import cv2 as cv

img = cv.imread("media/farol.jpg")

# verificar o tamanho da img
print(img.shape)

# selecionei Área com o "GIMP"
recorte = img[285:522, 127:398]  # -> Y[inicio,fim] e X[inicio,fim]
print(recorte)

cv.imshow("imagem_farol", img)
cv.imshow("imagem_farol", recorte)
cv.waitKey(0)
cv.destroyAllWindows()
