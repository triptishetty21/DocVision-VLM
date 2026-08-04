from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_angle_cls=True,
    lang="en"
)

def extract_text(image_path: str):
    result = ocr.ocr(image_path)

    extracted = []

    for line in result[0]:
        box = line[0]
        text = line[1][0]
        confidence = line[1][1]

        extracted.append({
            "text": text,
            "confidence": confidence,
            "box": box
        })

    return extracted