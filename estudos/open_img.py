import cv2 as cv

# abrir uma imagem
img = cv.imread("media/farol.jpg")
print(f"Dimensões da imagem em pixels RGB: {img.shape}")

img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
print(f"Dimensões da imagem em escala de cinza: {img_gray.shape}")

cv.imshow("imagem_farol", img_gray)
cv.waitKey(0)

# print(img)  # imprime os valores dos pixels da imagem em RGB
# print(img_gray)  # imprime os valores dos pixels da imagem em escala de cinza
cv.destroyAllWindows()
