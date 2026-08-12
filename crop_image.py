from pathlib import Path
from tkinter import filedialog

import cv2 as cv


def crop_selected_region(input_path, output_path=None):
    if output_path is None:
        output_path = "cropped_image.png"

    input_path = Path(input_path)
    output_path = Path(output_path)

    img = cv.imread(input_path)
    window_name = "Select crop area"

    roi = cv.selectROI(window_name, img, fromCenter=False, showCrosshair=False)

    cv.destroyWindow(window_name)

    x, y, w, h = roi

    if w == 0 or h == 0:
        raise ValueError("No area was selected.")

    cropped_image = img[y : y + h, x : x + w]

    output_path.parent.mkdir(parents=True, exist_ok=True)

    cv.imwrite(output_path, cropped_image)

    cv.waitKey(0)
    cv.destroyAllWindows()

    return cropped_image


file_path = filedialog.askopenfilename(
    title="Select an image", filetypes=[("Images", "*.jpg *.jpeg *.png")]
)

output_path = "crops/cropped_image.jpg"

cropped_image = crop_selected_region(file_path, output_path)
