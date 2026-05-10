# 🧬 PathLabs — Medical Scan Analysis API

A FastAPI backend that accepts medical imaging scans (Ultrasound, X-Ray, MRI, CT) and returns structured AI-generated diagnostic reports using deep learning models and Groq LLM inference.

---

## 🚀 Features

- **Multi-modality support** — Ultrasound, X-Ray, 2D MRI, and 2D CT scan analysis
- **Smart routing** — MRI and CT endpoints auto-detect file type and route to the appropriate model (2D image vs. 3D NIfTI)
- **Structured reports** — Every prediction returns a standardized JSON report with classifier results, combined assessment, recommended next steps, and a patient-friendly explanation
- **Groq LLM integration** — Uses Groq API for fast language model inference
- **Interactive API docs** — Auto-generated Swagger UI via FastAPI

---

## 📁 Project Structure

```
path_labs/
├── app/                        # FastAPI application
│   └── main.py                 # Entry point, route definitions
├── uploads/                    # Temporary upload storage
├── requirements.txt            # Python dependencies
└── README.md
```

> Model weights are expected under `models/` (not committed to the repo):
> - `models/ultrasound/best_model.pth`
> - `models/xray/best_xray_model.pth`
> - `models/mri_2d/mri_model.pth`
> - `models/ct_2d/ct_model.pth`

---

## 🛠️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/avinashmaharoliya/path_labs.git
cd path_labs
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

---

## 🌐 API Endpoints

| Method | Endpoint       | Description                        |
|--------|----------------|------------------------------------|
| `GET`  | `/health`      | Health check                       |
| `POST` | `/ultrasound`  | Analyze an ultrasound image        |
| `POST` | `/xray`        | Analyze a chest X-ray image        |
| `POST` | `/mri2d-3d`    | Analyze an MRI scan (2D or 3D)     |
| `POST` | `/ct2d-3d`     | Analyze a CT scan (2D or 3D)       |

### File Format Routing (MRI & CT)

| File Extension               | Routed To       |
|------------------------------|-----------------|
| `.png`, `.jpg`, `.jpeg`, `.bmp`, `.webp` | 2D model |
| `.nii`, `.nii.gz`            | 3D placeholder  |

> ⚠️ 3D NIfTI model support is currently a placeholder pending model training.

---

## 📄 Response Schema

All prediction endpoints return a consistent JSON structure:

```json
{
  "report_title": "string",
  "scan_type": "xray",
  "uploaded_image_review": {},
  "classifier_result": {},
  "combined_assessment": {},
  "recommended_next_steps": [],
  "patient_friendly_explanation": "string",
  "technical_limitations": []
}
```

---

## 📦 Dependencies

| Package            | Purpose                              |
|--------------------|--------------------------------------|
| `fastapi`          | Web framework                        |
| `uvicorn`          | ASGI server                          |
| `python-multipart` | File upload handling                 |
| `python-dotenv`    | Environment variable loading         |
| `groq`             | Groq LLM API client                  |
| `torch`            | Deep learning inference              |
| `torchvision`      | Image transforms and pretrained models |
| `timm`             | Model architectures (e.g. EfficientNet, ViT) |
| `pillow`           | Image loading and preprocessing      |

---

## 📖 API Docs

Once the server is running, open:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

---

## ⚠️ Disclaimer

PathLabs is a research and educational project. It is **not intended for clinical use**. Always consult a licensed medical professional for diagnosis and treatment decisions.

---

## 👤 Author

**Avinash Maharoliya** — [GitHub](https://github.com/avinashmaharoliya)
