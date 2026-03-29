# 🌿 Plant Disease Classifier
### B.Tech AI & Data Science Project | CNN + Transfer Learning + Flask

---

## 📁 Project Folder Structure

```
plant_disease_project/
│
├── 📄 app.py               ← Flask backend (main API server)
├── 📄 train.py             ← Model training (Phase 2)
├── 📄 preprocess.py        ← Data exploration (Phase 1)
├── 📄 disease_info.py      ← Disease database (EN + HI)
├── 📄 setup_dataset.py     ← Setup check & folder creator
├── 📄 test_app.py          ← Test your running server
├── 📄 requirements.txt     ← Python dependencies
│
├── 📁 dataset/
│   └── PlantVillage/       ← PUT DATASET HERE
│       ├── Apple___Apple_scab/
│       ├── Apple___healthy/
│       ├── Tomato___Late_blight/
│       └── ... (38 folders total)
│
├── 📁 model/
│   ├── plant_disease_model.h5   ← Saved model (after training)
│   └── class_names.json         ← Class label mapping
│
├── 📁 templates/
│   └── index.html          ← Frontend UI
│
├── 📁 static/              ← CSS/JS files (optional)
├── 📁 uploads/             ← Temporary upload storage
└── 📁 logs/                ← TensorBoard logs
```

---

## ⚡ Quick Start (Step by Step)

### Step 1 — Install Python dependencies

```bash
# Open VS Code terminal (Ctrl + `)
# Navigate to project folder
cd plant_disease_project

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt
```

### Step 2 — Setup folder structure

```bash
python setup_dataset.py
```

### Step 3 — Download dataset

1. Go to: https://www.kaggle.com/datasets/emmarex/plantdisease
2. Sign in with a free Kaggle account
3. Click "Download" → get `plantdisease.zip`
4. Extract and place inside `dataset/PlantVillage/`
5. Run again to verify: `python setup_dataset.py`

### Step 4 — Explore data (Phase 1)

```bash
python preprocess.py
```
This shows sample images and saves `model/class_names.json`

### Step 5 — Train the model (Phase 2)

```bash
python train.py
```
⏱️ Training takes **30–90 minutes** depending on your hardware.
Model will be saved to `model/plant_disease_model.h5`

### Step 6 — Start Flask server (Phase 3)

```bash
python app.py
```

### Step 7 — Open the app

Open your browser and go to: **http://127.0.0.1:5000**

---

## 🧪 Testing Without Training

You can test the Flask app immediately using **demo mode**
(returns a simulated prediction before your model is trained):

```bash
# Terminal 1: Start server
python app.py

# Terminal 2: Run tests
python test_app.py
```

---

## 🎯 Model Architecture

```
Input (224×224×3)
      ↓
MobileNetV2 (Pre-trained on ImageNet, 1.2M images)
[154 layers frozen in Phase 1, last 30 unfrozen in Phase 2]
      ↓
GlobalAveragePooling2D
      ↓
BatchNormalization
      ↓
Dense(512, ReLU) → Dropout(0.4)
      ↓
Dense(256, ReLU) → Dropout(0.3)
      ↓
Dense(38, Softmax) ← Output: 38 disease classes
```

**Expected accuracy: 92–97%** with PlantVillage dataset

---

## 🌐 API Endpoints

| Method | Endpoint   | Description                      |
|--------|------------|----------------------------------|
| GET    | `/`        | Frontend UI                      |
| POST   | `/predict` | Predict disease from image       |
| GET    | `/health`  | Check if server is running       |
| GET    | `/classes` | List all supported plant classes |

### POST /predict — Request Format

```
Content-Type: multipart/form-data
Fields:
  image: <image file>  (JPG/PNG/WEBP, max 10MB)
  lang:  "en" or "hi"  (optional, default: "en")
```

### POST /predict — Response Format

```json
{
  "success": true,
  "prediction": {
    "class_name": "Tomato___Late_blight",
    "display_name": "Tomato Late Blight",
    "confidence": 94.3,
    "severity": "Critical",
    "severity_color": "#B71C1C",
    "description": "Caused by Phytophthora infestans...",
    "treatment": ["Apply copper fungicides...", "..."],
    "prevention": "Use certified disease-free seeds..."
  },
  "alternatives": [
    {"name": "Tomato Early Blight", "confidence": 3.2},
    {"name": "Tomato healthy", "confidence": 1.1}
  ],
  "language": "en"
}
```

---

## 💡 Accuracy Improvement Tips

1. **Use more augmentation** (already included in train.py)
2. **Train longer** — increase `EPOCHS_PHASE2` to 30-40
3. **Reduce learning rate** — already uses ReduceLROnPlateau
4. **Class weighting** — add `class_weight='balanced'` to fit()
5. **Try EfficientNetB0** for even higher accuracy:
   ```python
   from tensorflow.keras.applications import EfficientNetB0
   base_model = EfficientNetB0(include_top=False, weights='imagenet')
   ```

---

## 🐛 Debugging Common Errors

| Error | Fix |
|-------|-----|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `Could not load model` | Check `model/plant_disease_model.h5` exists |
| `OOM (Out of Memory)` | Reduce `BATCH_SIZE` to 16 or 8 in train.py |
| `No such file: dataset/PlantVillage` | Download dataset from Kaggle |
| `Port 5000 in use` | Change `port=5001` in app.py |
| `Keras version mismatch` | Load model with `compile=False` parameter |

---

## 🌍 Multi-Language Support

The app supports **English** and **Hindi** with:
- Language toggle button in the UI header
- All disease names, descriptions, and treatments translated
- `lang` parameter in the API (`"en"` or `"hi"`)
- Frontend UI text switches instantly on toggle

To add more languages, edit `disease_info.py` and add new language keys.

---

## 🚀 Optional Deployment

### Local Network (share with classmates on same WiFi)

```bash
python app.py
# App will be at: http://YOUR_IP:5000
# Find your IP: ipconfig (Windows) or ifconfig (Mac/Linux)
```

### Render.com (Free Cloud Deployment)

1. Push project to GitHub
2. Create account at render.com
3. New → Web Service → connect GitHub repo
4. Build command: `pip install -r requirements.txt`
5. Start command: `python app.py`
6. Done! Get a public URL

---

## 🌿 Supported Plants & Diseases (38 Classes)

| Plant | Diseases |
|-------|----------|
| Apple | Apple Scab, Black Rot, Cedar Rust, Healthy |
| Blueberry | Healthy |
| Cherry | Powdery Mildew, Healthy |
| Corn | Gray Leaf Spot, Common Rust, Northern Blight, Healthy |
| Grape | Black Rot, Esca, Leaf Blight, Healthy |
| Orange | Haunglongbing |
| Peach | Bacterial Spot, Healthy |
| Pepper | Bacterial Spot, Healthy |
| Potato | Early Blight, Late Blight, Healthy |
| Raspberry | Healthy |
| Soybean | Healthy |
| Squash | Powdery Mildew |
| Strawberry | Leaf Scorch, Healthy |
| Tomato | Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria, Spider Mite, Target Spot, TYLCV, Mosaic Virus, Healthy |

---

*Built by a B.Tech AI & Data Science student using TensorFlow, Flask, and MobileNetV2*
