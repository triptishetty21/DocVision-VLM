def chunk_document(ocr_document: list, chunk_size: int = 500):
    full_text = []

    for page in ocr_document:
        for item in page:
            full_text.append(item["text"])

    full_text = " ".join(full_text)

    chunks = []

    for i in range(0, len(full_text), chunk_size):
        chunks.append(full_text[i:i + chunk_size])

    return chunks