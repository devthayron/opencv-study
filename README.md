# Visão Computacional com Python

Projeto desenvolvido para praticar **OpenCV e visão computacional**, explorando captura de vídeo, processamento e manipulação de imagens.

O repositório reúne **estudos, experimentos e pequenos utilitários** desenvolvidos ao longo do aprendizado.

A pasta `estudos/` contém os experimentos práticos e a documentação dos conceitos estudados em [`anotacao.md`](estudos/anotacao.md).

Atualmente, os principais utilitários são o `camera.py`, para **captura de vídeo pela webcam ou celular**, e o `crop_image.py`, para **recorte de imagens utilizando ROI**.

## Como utilizar e o que fazem

### Captura de vídeo

O `camera.py` permite capturar vídeo pela webcam do computador ou pela câmera de um celular.

#### Webcam

Sem informar um IP, a webcam padrão do computador será utilizada:

```python
open_camera()
```

#### Celular

Para utilizar a câmera do celular:

1. Instale o aplicativo **IP Webcam** no Android.
2. Abra o aplicativo e clique em **Start server**.
3. Copie o IP exibido pelo aplicativo.
4. Informe o IP no arquivo `.env`:

```env
CAMERA_IP=seu_ip
```

O projeto possui um arquivo `.env.example` como modelo.

> O **Start server** precisa permanecer ativo durante a captura. O IP pode mudar conforme a rede utilizada.

Pressione **Q** para encerrar a captura.

### Recorte de imagem

O `crop_image.py` permite selecionar uma região da imagem utilizando o mouse e salvar o recorte em um novo arquivo.

A imagem de entrada pode ser informada diretamente pelo caminho do arquivo ou selecionada através da interface padrão de seleção de arquivos do sistema.

O caminho da imagem de saída também pode ser informado manualmente. Caso não seja definido, a função utiliza o caminho padrão configurado em seu parâmetro.

A seleção da região utiliza o conceito de **ROI (Region of Interest)** do OpenCV.

#### Exemplo

Informando os caminhos manualmente:

```python
crop_selected_region(
    "media/farol.jpg",
    "crops/cropped_image.jpg",
)
```

Também é possível abrir a interface de seleção de arquivos para escolher a imagem:

```python
file_path = filedialog.askopenfilename(
    title="Selecione uma imagem",
    filetypes=[("Imagens", "*.jpg *.jpeg *.png")],
)

crop_selected_region(file_path)
```

Nesse caso, o caminho de saída não é informado e a função utiliza o valor padrão definido em `output_path`.

---

## Tecnologias

* Python
* OpenCV
* NumPy
* Tkinter
* IP Webcam
* python-dotenv
