from pathlib import Path

import torch


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

UPLOAD_DIR = PROJECT_ROOT / "fastapi_backend" / "uploads"
MODEL_DIR = PROJECT_ROOT / "fastapi_backend" / "models"

GROQ_MODEL_NAME = "meta-llama/llama-4-scout-17b-16e-instruct"

REPORT_SCHEMA_TEXT = """
{
  "report_title": "string",
  "scan_type": "ultrasound | xray | mri_2d | mri_3d | ct_2d | ct_3d",
  "uploaded_image_review": {
    "modality_observed": "string",
    "image_quality": "string",
    "general_observations": ["string"],
    "limitations_of_visual_review": ["string"]
  },
  "classifier_result": {
    "ai_model": "string",
    "predicted_class": "string",
    "confidence_percent": 0,
    "probabilities": [
      {
        "class_name": "string",
        "probability_percent": 0,
        "meaning": "string"
      }
    ]
  },
  "combined_assessment": {
    "summary": "string",
    "risk_level": "low | moderate | high | uncertain",
    "what_this_may_indicate": "string",
    "what_this_does_not_confirm": "string"
  },
  "recommended_next_steps": ["string"],
  "patient_friendly_explanation": "string",
  "technical_limitations": ["string"]
}
"""

MODEL_CONFIGS = {
    "ultrasound": {
        "kind": "timm",
        "model_name": "efficientnet_b4",
        "weights": MODEL_DIR / "ultrasound" / "best_model.pth",
        "classes": ["benign", "malignant", "normal"],
        "ai_model": "EfficientNet-B4 breast ultrasound classifier",
        "scan_type": "ultrasound",
    },
    "xray": {
        "kind": "timm",
        "model_name": "efficientnet_b0",
        "weights": MODEL_DIR / "xray" / "best_xray_model.pth",
        "classes": ["NORMAL", "PNEUMONIA"],
        "ai_model": "EfficientNet-B0 pneumonia X-ray classifier",
        "scan_type": "xray",
    },
    "mri_2d": {
        "kind": "resnet18",
        "weights": MODEL_DIR / "mri_2d" / "mri_model.pth",
        "classes": ["glioma", "meningioma", "notumor", "pituitary"],
        "ai_model": "ResNet18 brain tumor MRI 2D classifier",
        "scan_type": "mri_2d",
    },
    "ct_2d": {
        "kind": "resnet18",
        "weights": MODEL_DIR / "ct_2d" / "ct_model.pth",
        "classes": ["Hemorrhagic", "NORMAL"],
        "ai_model": "ResNet18 brain CT hemorrhage 2D classifier",
        "scan_type": "ct_2d",
    },
}

THREE_D_SCAN_TYPES = {"mri_3d", "ct_3d"}
