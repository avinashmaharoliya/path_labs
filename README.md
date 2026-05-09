# Medical Scan FastAPI Backend

This backend exposes four upload endpoints:

- `POST /ultrasound`
- `POST /xray`
- `POST /mri2d-3d`
- `POST /ct2d-3d`

MRI and CT endpoints auto-route files:

- image files (`.png`, `.jpg`, `.jpeg`, `.bmp`, `.webp`) go to the 2D model
- NIfTI files (`.nii`, `.nii.gz`) go to the 3D placeholder function

The 3D MRI/CT model files are placeholders until those models are trained.

## Setup

Install dependencies:

```powershell
pip install -r fastapi_backend/requirements.txt
```

Create `.env` in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Run:

```powershell
uvicorn app.main:app --reload --app-dir fastapi_backend
```

Open docs:

```text
http://127.0.0.1:8000/docs
```

Health check:

```text
http://127.0.0.1:8000/health
```

## Current Loaded Models

- Ultrasound: `fastapi_backend/models/ultrasound/best_model.pth`
- X-ray: `fastapi_backend/models/xray/best_xray_model.pth`
- MRI 2D: `fastapi_backend/models/mri_2d/mri_model.pth`
- CT 2D: `fastapi_backend/models/ct_2d/ct_model.pth`

## Response Shape

Each prediction endpoint returns:

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

The response follows the structure in the root `format.json` directly. No wrapper fields are added.
