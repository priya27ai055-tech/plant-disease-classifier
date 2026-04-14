# =============================================================
# download_model.py
# Render startup par model.onnx Google Drive se download karta hai
# =============================================================

import os
import gdown

MODEL_PATH = "model/model.onnx"
# Apna Google Drive File ID yahan daalo:
FILE_ID = "1QVitRkwVdbgpK3BNUPme3t8nboSyrq-O"

def download_model():
    # Model folder banao agar nahi hai
    os.makedirs("model", exist_ok=True)

    # Agar model pehle se downloaded hai toh skip karo
    if os.path.exists(MODEL_PATH):
        size = os.path.getsize(MODEL_PATH)
        if size > 1000000:  # 1MB se bada = valid model
            print(f"[INFO] Model already exists ({size/1024/1024:.1f} MB) — skipping download.")
            return True

    print("[INFO] Downloading model.onnx from Google Drive...")

    try:
        url = f"https://drive.google.com/uc?id={FILE_ID}"
        gdown.download(url, MODEL_PATH, quiet=False)

        if os.path.exists(MODEL_PATH):
            size = os.path.getsize(MODEL_PATH)
            print(f"[INFO] Model downloaded successfully! Size: {size/1024/1024:.1f} MB")
            return True
        else:
            print("[ERROR] Download failed — file not found after download!")
            return False

    except Exception as e:
        print(f"[ERROR] Download error: {e}")
        return False

if __name__ == "__main__":
    download_model()
