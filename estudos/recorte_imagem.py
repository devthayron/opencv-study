# Evitar acentos ou outros caracteres especiais no nome da janela, pois podem causar erro no Qt !

import cv2 as cv

img = cv.imread("media/farol.jpg")

# img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

nome_janela = "Selecione a area de recorte"

dimensao = cv.selectROI(nome_janela, img, fromCenter=False, showCrosshair=False)

cv.destroyWindow(nome_janela)
print("\nCoordenadas selecionadas (x, y, largura, altura):", dimensao)

x, y, w, h = dimensao

print(f"""
Imagem
┌────────────────────────────> X
│
│        (x, y)
│        ({x}, {y})
│       ┌─────────────┐
│       │             │
│       │   RECORTE   │ ↑
│       │             │ │ altura ({h})
│       └─────────────┘ ↓
│       <─ largura ───>
│            ({w})
│
↓
Y
""")


imagem_recortada = img[y : y + h, x : x + w]

# salvar imagem na pasta
cv.imwrite("media/img_recortada.jpg", imagem_recortada)

# selecionar imagem recortada
# cv.imshow("Imagem recortada", imagem_recortada)

cv.waitKey(0)

cv.destroyAllWindows()
