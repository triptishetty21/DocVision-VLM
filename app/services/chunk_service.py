from langchain_text_splitters import RecursiveCharacterTextSplitter


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
)


def chunk_document(ocr_document: list):
    full_text = []

    for page in ocr_document:
        for item in page:
            full_text.append(item["text"])

    document = " ".join(full_text)

    chunks = text_splitter.split_text(document)

    return chunks