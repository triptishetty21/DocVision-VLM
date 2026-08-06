from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
    lang="en",
)


def extract_text(image_path: str):

    result = list(ocr.predict(image_path))[0]

    texts = result["rec_texts"]
    scores = result["rec_scores"]
    boxes = result["dt_polys"]

    extracted = []

    for text, score, box in zip(texts, scores, boxes):
        extracted.append(
            {
                "text": text,
                "confidence": score,
                "box": box.tolist(),
            }
        )

    return extracted