# Visão Computacional com Python

Projeto para praticar **OpenCV e visão computacional**, permitindo capturar vídeo em tempo real pela webcam do computador ou pela câmera do celular.

## Como utilizar

### Webcam

Sem informar um IP, a webcam padrão do computador será utilizada:

```python
open_camera()
```

### Celular

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

### Controle

Pressione **Q** para encerrar a captura.

## Tecnologias

* Python
* OpenCV
* IP Webcam
* python-dotenv
