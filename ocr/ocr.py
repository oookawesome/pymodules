from typing import Optional

import pytesseract
from pathlib import Path
from PIL import Image


class OCR:
    @staticmethod
    def read(img_path: str) -> Optional[str]:
        _img_path = Path(img_path)
        if _img_path.suffix in ['.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif']:
            img = Image.open(_img_path)
            return pytesseract.image_to_string(img)
        else:
            print(f'Not supported file extension! : {_img_path}')
            return None


if __name__ == '__main__':
    # path = 'resources/sample1.pdf'
    path = 'resources/image1.jpg'
    ocr = OCR()
    print(ocr.read(path))

