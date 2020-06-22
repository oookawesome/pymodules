from pathlib import Path
from typing import Optional, List, Any

import pdf2image


class FileConverter:
    @staticmethod
    def pdf_to_img(pdf_path: str) -> Optional[List[Any]]:
        _pdf_path = Path(pdf_path)
        return pdf2image.convert_from_path(_pdf_path)

    def pdf_to_img_files(self, pdf_path: str, dst_dir: str) -> Optional[str]:
        _dst_dir = Path(dst_dir)
        if not _dst_dir.exists():
            _dst_dir.mkdir(exist_ok=True)

        _pdf_path = Path(pdf_path)
        if _pdf_path.exists():
            images = self.pdf_to_img(pdf_path)
            for idx, image in enumerate(images):
                img_name = _pdf_path.stem + '_' + str(idx) + '.jpg'
                img_path = _dst_dir / _pdf_path.with_name(img_name).name
                with open(img_path, mode='wb') as f:
                    image.save(f)
            return _dst_dir
        else:
            print(f'PDF file does not exist! : {_pdf_path}')
            return None


if __name__ == '__main__':
    path = 'resources/sample1.pdf'
    fc = FileConverter()
    # fc.pdf_to_img(path)
    fc.pdf_to_img_files(path, 'result')
