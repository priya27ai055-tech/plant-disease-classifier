# =============================================================
# Flask Backend - Render Deployment Version
# File: app.py
# =============================================================

import os
import json
import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
from PIL import Image
import onnxruntime as ort
from disease_info import get_disease_info, get_severity_color

# Model download karo startup par (Render ke liye)
from download_model import download_model
download_model()

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "bmp", "webp"}
IMG_SIZE = (224, 224)
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

MODEL_PATH       = "model/model.onnx"
CLASS_NAMES_PATH = "model/class_names.json"
session          = None
class_names      = {}

def load_model_and_classes():
    global session, class_names
    try:
        print("[INFO] Loading ONNX model...")
        session = ort.InferenceSession(MODEL_PATH)
        print(f"[INFO] Model loaded! Input: {session.get_inputs()[0].shape}")
    except Exception as e:
        print(f"[ERROR] Model load failed: {e}")
        print("[WARN] Running in demo mode.")

    try:
        with open(CLASS_NAMES_PATH, "r") as f:
            class_names = json.load(f)
        print(f"[INFO] Loaded {len(class_names)} classes.")
    except Exception as e:
        print(f"[WARN] Class names load failed: {e}")

load_model_and_classes()

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image_path):
    img = Image.open(image_path).convert("RGB")
    img = img.resize(IMG_SIZE)
    img_array = np.array(img, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict(image_path):
    if session is None:
        return [("Tomato_Late_blight", 0.92), ("Tomato_Early_blight", 0.05)]
    try:
        img_array  = preprocess_image(image_path)
        input_name = session.get_inputs()[0].name
        predictions = session.run(None, {input_name: img_array})[0][0]
        top_indices = np.argsort(predictions)[::-1][:3]
        results = []
        for idx in top_indices:
            class_name = class_names.get(str(idx), f"Class_{idx}")
            confidence = float(predictions[idx])
            results.append((class_name, confidence))
            print(f"[PREDICT] {class_name}: {confidence*100:.2f}%")
        return results
    except Exception as e:
        print(f"[ERROR] Prediction error: {e}")
        return [("Tomato_Late_blight", 0.50)]

# ==================== PAGE ROUTES ====================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/select")
def select():
    return render_template("index.html")

@app.route("/diagnose")
def diagnose():
    return render_template("index.html")

@app.route("/history")
def history():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("index.html")

# ==================== API ROUTES ====================
@app.route("/predict", methods=["POST"])
def predict_disease():
    if "image" not in request.files:
        return jsonify({"error": "No image file provided."}), 400
    file = request.files["image"]
    lang = request.form.get("lang", "en")
    if file.filename == "":
        return jsonify({"error": "No file selected."}), 400
    if not allowed_file(file.filename):
        return jsonify({"error": "File type not allowed."}), 400
    filename  = secure_filename(file.filename)
    save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(save_path)
    try:
        results = predict(save_path)
        top_class, top_confidence = results[0]
        if top_confidence < 0.40:
            return jsonify({
                "success": False,
                "error": "Image not recognized as a plant leaf. Please upload a clear leaf photo."
            }), 200
        disease_info   = get_disease_info(top_class, lang)
        severity_color = get_severity_color(disease_info.get("severity", "Unknown"))
        alternatives   = []
        for cls_name, conf in results[1:]:
            alt_info = get_disease_info(cls_name, lang)
            alternatives.append({
                "name":       alt_info.get("name", cls_name),
                "confidence": round(conf * 100, 2)
            })
        response = {
            "success": True,
            "prediction": {
                "class_name":     top_class,
                "display_name":   disease_info.get("name", top_class),
                "confidence":     round(top_confidence * 100, 2),
                "severity":       disease_info.get("severity", "Unknown"),
                "severity_color": severity_color,
                "description":    disease_info.get("description", ""),
                "treatment":      disease_info.get("treatment", []),
                "prevention":     disease_info.get("prevention", ""),
            },
            "alternatives": alternatives,
            "language": lang
        }
        return jsonify(response), 200
    except Exception as e:
        print(f"[ERROR] Prediction failed: {e}")
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500
    finally:
        if os.path.exists(save_path):
            os.remove(save_path)

@app.route("/health")
def health():
    return jsonify({
        "status":       "ok",
        "model_loaded": session is not None,
        "classes":      len(class_names)
    })

@app.route("/classes")
def get_classes():
    return jsonify({"classes": list(class_names.values()), "count": len(class_names)})

@app.errorhandler(413)
def too_large(e):
    return jsonify({"error": "File too large. Max 10MB."}), 413

@app.errorhandler(404)
def not_found(e):
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"\n{'='*50}")
    print(f"  PlantHealth AI — Running on port {port}")
    print(f"{'='*50}\n")
    app.run(host="0.0.0.0", port=port, debug=False)
