from pathlib import Path
import fitz

def pdf_to_images(pdf_path: str) -> list[str]:
    pdf = fitz.open(pdf_path)

    output_dir = Path(pdf_path).parent / Path(pdf_path).stem
    output_dir.mkdir(exist_ok=True)

    image_paths = []

    for page_number in range(len(pdf)):
        page = pdf.load_page(page_number)

        pix = page.get_pixmap(dpi=200)

        image_path = output_dir / f"page_{page_number + 1}.png"

        pix.save(image_path)

        image_paths.append(str(image_path))

    pdf.close()

    return image_paths