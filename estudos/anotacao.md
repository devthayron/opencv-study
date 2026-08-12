# Estudos de OpenCV

## Importação

```python
import cv2 as cv
```

---

## Dimensões da imagem

O atributo `.shape` retorna as dimensões da imagem.

```python
IMG_PATH = "../media/farol.jpg"

img = cv.imread(IMG_PATH)

print(f"Dimensões da imagem: {img.shape}")
```

Resultado:

```text
(640, 960, 3)
```

A ordem é:

```text
(altura, largura, canais)
   640     960      3
```

* `640` → altura em pixels
* `960` → largura em pixels
* `3` → canais de cor

> **Importante:** o `cv.imread()` carrega a imagem no formato **BGR**, e não RGB.

---

## Escala de cinza

Para converter a imagem para escala de cinza:

```python
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

print(f"Dimensões da imagem em escala de cinza: {img_gray.shape}")
```

Resultado:

```text
(640, 960)
```

A imagem passa a ter apenas dois valores:

```text
(altura, largura)
```

Cada pixel possui um valor entre `0` e `255`:

```text
0   → preto
255 → branco
```

---

## Exibindo a imagem

```python
cv.imshow("imagem_farol", img)
cv.waitKey(0)
```

Para visualizar a imagem em escala de cinza:

```python
cv.imshow("imagem_farol", img_gray)
cv.waitKey(0)
```

O `cv.waitKey(0)` mantém a janela aberta até uma tecla ser pressionada.

Sim. Eu reduziria para algo nesse nível — suficiente para entender o funcionamento sem transformar a anotação em documentação da API:

---

## Exibindo vídeo

O OpenCV trata um vídeo como uma sequência de **frames (quadros)**. Cada frame é uma imagem que pode ser processada individualmente.

O `cv.VideoCapture()` pode receber diferentes fontes:

```python
# Arquivo de vídeo
VIDEO_PATH = "../media/runners.mp4"
video = cv.VideoCapture(VIDEO_PATH)

# Webcam padrão
video = cv.VideoCapture(0)
```

- `VIDEO_PATH` → abre um vídeo existente.
- `0` → acessa a webcam padrão do computador.

### Lendo os frames

O método `.read()` obtém o próximo frame:

```python
check, img = video.read()
```

* `check` → indica se o frame foi lido corretamente.
* `img` → contém o frame como um array NumPy.

Como o vídeo possui vários frames, utilizamos um loop:

```python
while True:
    check, img = video.read()

    if not check:
        break
    
    # Apenas para deixar o video menor, poderia passar o img direto
    img_redimensionada = cv.resize(img, (640, 420))

    cv.imshow("video", img_redimensionada)

    if cv.waitKey(15) & 0xFF == ord("q"):
        break
```

O `cv.waitKey(15)` permite controlar a atualização da janela e verificar se uma tecla foi pressionada. Nesse caso, `Q` encerra a reprodução.

Ao finalizar, liberamos o vídeo e fechamos as janelas:

```python
video.release()
cv.destroyAllWindows()
```

> O vídeo é processado frame a frame, o que permite aplicar técnicas de visão computacional individualmente em cada imagem.

# Seleção de área da imagem

O `cv.selectROI()` permite selecionar uma região da imagem utilizando o mouse.

```python
nome_janela = "Selecione a area de recorte"

cv.namedWindow(nome_janela, cv.WINDOW_NORMAL)
cv.imshow(nome_janela, img)

dimensao = cv.selectROI(nome_janela, img, fromCenter=False, showCrosshair=False)

print(dimensao)

cv.destroyAllWindows()
```

O retorno possui quatro valores:

```text
(x, y, largura, altura)
```

Exemplo:

```text
(120, 80, 300, 200)
```

Representação:

```text
Imagem
┌──────────────────────────────> X
│
│       (x, y)
│        (120, 80)
│       ┌──────────────┐
│       │              │
│       │    IMAGEM    │ ↑
│       │              │ │ altura = 200
│       └──────────────┘ ↓
│       ← largura = 300 →
│
↓
Y
```

### Parâmetros do `selectROI()`

```python
nome_janela = "Selecione a area de recorte"
cv.selectROI(nome_janela, img, fromCenter=False, showCrosshair=False)
```

* `nome_janela` → nome da janela onde a seleção será feita.
* `img` → imagem utilizada.
* `fromCenter=False` → o retângulo começa no ponto onde o mouse foi pressionado.
* `showCrosshair=False` → não exibe a cruz auxiliar.

### Observação sobre o `nome_janela`

Evitar acentos ou outros caracteres especiais no nome da janela, pois podem causar erros no Qt.

```python
# Evitar:
nome_janela = "Selecione a área de recorte"

# Preferir:
nome_janela = "Selecione a area de recorte"
```

Durante a seleção, o OpenCV também pode exibir informações do pixel sob o cursor:

* `X` → coordenada horizontal.
* `Y` → coordenada vertical.
* `BGR` → valores das componentes de cor do pixel.

> O OpenCV utiliza **BGR** como ordem padrão dos canais.

---

## Recortando a imagem

Podemos recortar uma região da imagem utilizando o **slicing do NumPy**.

```python
recorte = img[285:522, 127:398]
#             Y[início:fim], X[início:fim]
```

A estrutura é:

```text
img[Y[início:fim], X[início:fim]]
```

Neste exemplo:

```text
Y → 285 até 522
X → 127 até 398
```

> O valor final não é incluído. Portanto, `285:522` seleciona as posições de `285` até `521`.

### Visualização

```text
Imagem
┌────────────────────────────────> X
│
│     X: 127            X: 398
│       ↓                 ↓
│       ┌─────────────────┐
│       │                 │
│       │     RECORTE     │
│       │                 │
│       └─────────────────┘
│       ↑                 ↑
│     Y: 285            Y: 522
│
↓
Y
```

### Utilizando o `selectROI()`

Em vez de informar as coordenadas manualmente, podemos obtê-las através do `cv.selectROI()`:

```python
x, y, w, h = dimensao

recorte = img[y:y+h, x:x+w]

cv.imshow("imagem_recortada", recorte)

cv.waitKey(0)
cv.destroyAllWindows()
```

O `selectROI()` retorna:

```text
(x, y, largura, altura)
```

Enquanto o slicing utiliza:

```text
[y:y+altura, x:x+largura]
```

Ou seja:

```text
selectROI()
    ↓
(x, y, w, h)
    ↓
img[y:y+h, x:x+w]
    ↓
recorte
```

> Embora chamemos de "imagem", o OpenCV representa a imagem como um array NumPy. O recorte acima é, portanto, um slicing desse array.

---

# Problema com fontes do OpenCV/Qt

Ao utilizar funções gráficas do OpenCV, como `cv.selectROI()`, o Qt apresentou:

```text
QFontDatabase: Cannot find font directory .../cv2/qt/fonts
```

## Causa

As fontes já estavam instaladas no sistema, mas o Qt utilizado pelo OpenCV procurava as fontes dentro da pasta do próprio `cv2`:

```text
venv/lib/python3.12/site-packages/cv2/qt/fonts
```

As fontes do sistema estavam em:

```text
/usr/share/fonts/truetype/dejavu
```

Foi possível confirmar com:

```bash
fc-match -v DejaVuSans | grep file
```

## Solução

Criar a pasta que o Qt esperava e criar links para as fontes do sistema:

```bash
mkdir -p venv/lib/python3.12/site-packages/cv2/qt/fonts

ln -s /usr/share/fonts/truetype/dejavu/* \
venv/lib/python3.12/site-packages/cv2/qt/fonts/
```

Depois disso, o aviso deixou de aparecer e os elementos da interface gráfica passaram a ser exibidos corretamente.

## Resumo

As fontes já existiam no sistema. O problema era que o Qt do OpenCV não conseguia encontrá-las no diretório esperado.

A criação dos links permitiu que o Qt encontrasse as fontes utilizadas pela interface gráfica.
