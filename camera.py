import os

import cv2 as cv
from dotenv import load_dotenv

load_dotenv()

camera_ip = os.getenv("CAMERA_IP")


def open_camera(ip=None):
    """
    Abre a câmera do celular ou a webcam do computador.

    Se o IP não for informado:
    - A webcam do computador será utilizada.

    Para utilizar o celular:
    - Baixar o app "IP Webcam" na Play Store.
    - Informar o IP exibido pelo aplicativo.
    - Clicar em "Start server".
    - O "Start server" precisa estar rodando para funcionar.

    Para encerrar a captura:
    - Pressionar a tecla "Q".
    """

    if not ip:
        video = cv.VideoCapture(0)
        window_name = "Webcam"

    else:
        url = f"http://{ip}:8080/video"
        video = cv.VideoCapture(url)
        window_name = "Cellphone"

    if not video.isOpened():
        raise ConnectionError("Não foi possível conectar à câmera.")
    try:
        while True:
            check, frame = video.read()

            if not check:
                print("Não foi possível receber o vídeo.")
                break

            # Redimensiona o frame para 480p 16:9.
            resized_frame = cv.resize(frame, (854, 480))

            cv.imshow(window_name, resized_frame)

            if cv.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        video.release()
        cv.destroyAllWindows()


# acessa o ip da camera do celular
open_camera(ip=camera_ip)
