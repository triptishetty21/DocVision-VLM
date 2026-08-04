# DocVision-VLM

DocVision-VLM is a modular document intelligence backend that processes PDF documents and scanned files through OCR and natural language processing pipelines. The system extracts text, structures document content into searchable chunks, generates semantic embeddings, and is designed to support Retrieval-Augmented Generation (RAG) for intelligent document question answering.

The project is being developed with a production-oriented architecture that emphasizes modularity, scalability, and maintainability.

---

## Features

### Current

- PDF document upload
- File validation and storage
- Multi-page PDF processing
- OCR-based text extraction using PaddleOCR
- Document chunking
- Semantic embedding generation
- Modular FastAPI backend
- Service-oriented architecture

### Planned

- Qdrant vector database integration
- Semantic similarity search
- Retrieval-Augmented Generation (RAG)
- Question answering using Qwen2-VL
- Dockerized deployment
- Batch document processing
- Multi-document support
- Authentication and authorization
- Metadata filtering

---

## Architecture

```
                     Client
                        │
                        ▼
                  FastAPI Backend
                        │
                        ▼
                 Upload API Endpoint
                        │
                        ▼
                File Processing Service
                        │
                        ▼
                 PDF Processing Service
                        │
                        ▼
                  Page Image Generation
                        │
                        ▼
                  PaddleOCR Extraction
                        │
                        ▼
                Structured Text Output
                        │
                        ▼
                 Document Chunking
                        │
                        ▼
             Embedding Generation
                        │
                        ▼
             (Future) Qdrant Database
                        │
                        ▼
          (Future) Semantic Retrieval
                        │
                        ▼
          (Future) Qwen2-VL Generation
```

---

## Technology Stack

### Backend

- Python
- FastAPI
- Uvicorn

### Document Processing

- PyMuPDF
- PaddleOCR

### NLP

- Sentence Transformers
- all-MiniLM-L6-v2

### Vector Database (Planned)

- Qdrant

### Large Language Model (Planned)

- Qwen2-VL

### Deployment

- Docker (Planned)

---

## Project Structure

```
docvision-vlm/
│
├── app/
│   ├── api/
│   │   ├── qa.py
│   │   └── upload.py
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── services/
│   │   ├── chunk_service.py
│   │   ├── embedding_service.py
│   │   ├── file_service.py
│   │   ├── ocr_service.py
│   │   └── pdf_service.py
│   │
│   ├── models/
│   ├── schemas/
│   ├── utils/
│   └── main.py
│
├── data/
│   └── uploads/
│
├── requirements.txt
└── README.md
```

---

## Processing Pipeline

Current implementation:

```
Upload Document
      │
      ▼
Validate File
      │
      ▼
Store Document
      │
      ▼
Convert PDF to Images
      │
      ▼
OCR Extraction
      │
      ▼
Text Chunking
      │
      ▼
Embedding Generation
```

Target pipeline:

```
Upload Document
      │
      ▼
OCR
      │
      ▼
Chunking
      │
      ▼
Embeddings
      │
      ▼
Qdrant
      │
      ▼
Semantic Retrieval
      │
      ▼
Qwen2-VL
      │
      ▼
Generated Answer
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/triptishetty21/DocVision-VLM.git
cd DocVision-VLM
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the environment.

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
uvicorn app.main:app --reload
```

The API will be available at

```
http://127.0.0.1:8000
```

Interactive API documentation

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Upload Document

```
POST /upload
```

Uploads a PDF document, extracts text using OCR, chunks the extracted content, and generates semantic embeddings.

---

### Question Answering

```
POST /qa
```

Endpoint reserved for document question answering functionality.

---

## Design Principles

- Modular service-oriented architecture
- Separation of API and business logic
- Independent processing services
- Extensible AI pipeline
- Replaceable OCR and embedding models
- Production-ready project organization

---

## Current Status

Implemented

- FastAPI backend
- Upload API
- OCR pipeline
- PDF processing
- Document chunking
- Embedding generation

In Progress

- Vector database integration
- Retrieval pipeline
- Question answering

Planned

- Vision Language Model integration
- Docker deployment
- Multi-document indexing
- Production deployment

---

## Roadmap

- Integrate Qdrant
- Implement semantic search
- Complete Retrieval-Augmented Generation pipeline
- Integrate Qwen2-VL
- Add Docker support
- Implement authentication
- Add automated tests
- Deploy to cloud infrastructure

---

## Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.