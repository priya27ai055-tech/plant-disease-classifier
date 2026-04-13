# 🌿 Plant Disease Classifier
### B.Tech AI & Data Science Project | CNN + Transfer Learning + Flask

![Python](https://img.shields.io/badge/Python-3.11-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.12-orange)
![Flask](https://img.shields.io/badge/Flask-2.3-green)
![Accuracy](https://img.shields.io/badge/Accuracy-97.72%25-brightgreen)

---

## 📌 Project Overview

A deep learning web application that detects plant diseases from leaf images using **MobileNetV2 Transfer Learning**. Upload a leaf photo and get instant diagnosis with treatment recommendations in **English and Hindi**.

---

## 🎯 Model Performance

| Metric | Value |
|--------|-------|
| **Validation Accuracy** | **97.72%** |
| **Training Epochs** | 30 (Phase 1: 10 + Phase 2: 20) |
| **Model Architecture** | MobileNetV2 + Custom Head |
| **Training Platform** | Google Colab (T4 GPU) |
| **Dataset** | PlantVillage (subset) |

---

## 🌱 Supported Plants & Diseases (15 Classes)

| Plant | Diseases |
|-------|----------|
| **Pepper (Bell)** | Bacterial Spot, Healthy |
| **Potato** | Early Blight, Late Blight, Healthy |
| **Tomato** | Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Mosaic Virus, Healthy |

---

## 🛠️ Tech Stack

- **Deep Learning**: TensorFlow 2.12, Keras, MobileNetV2
- **Backend**: Flask, ONNX Runtime
- **Frontend**: HTML5, CSS3, JavaScript
- **Training**: Google Colab (T4 GPU)
- **Language Support**: English + Hindi (हिंदी)

---

## 📁 Project Structure

```
plant_disease_project/
├── app.py                  ← Flask backend
├── train.py                ← Model training
├── preprocess.py           ← Data preprocessing
├── disease_info.py         ← Disease database (EN + HI)
├── setup_dataset.py        ← Setup helper
├── requirements.txt        ← Dependencies
├── model/
│   ├── model.onnx          ← Trained model (ONNX format)
│   └── class_names.json    ← Class labels
└── templates/
    └── index.html          ← Frontend UI
```

---

## ⚡ Quick Start

```bash
# 1. Clone repository
git clone https://github.com/priya27ai055-tech/plant-disease-classifier.git
cd plant-disease-classifier

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt
pip install onnxruntime==1.15.0

# 4. Run the app
python app.py

# 5. Open browser
# http://127.0.0.1:5000
```

---

## 🌐 Features

- ✅ Real-time plant disease detection
- ✅ 97.72% model accuracy
- ✅ Treatment recommendations
- ✅ Severity indicators (None/Moderate/High/Critical)
- ✅ Multi-language support (English + Hindi)
- ✅ Prevention tips
- ✅ Top-3 prediction alternatives
- ✅ Beautiful responsive UI
- ✅ Before/After Tracker 

---

## 👥 Team Members

| Name | GitHub |
|------|--------|
| Priya | [@priya27ai055-tech](https://github.com/priya27ai055-tech) |
| Aishwary | [@AishwaryB-SATI](https://github.com/AishwaryB-SATI) |
| Anshika | [@Anshika-Jain446](https://github.com/Anshika-Jain446) |
| Nilima | [@Nilima620](https://github.com/Nilima620) |
| Rajshree | [@Rajshree609](https://github.com/Rajshree609) |

---

*Built by B.Tech AI & Data Science students using TensorFlow, Flask, and MobileNetV2*
