# =============================================================
# Quick Test Script - Test app without training a model
# File: test_app.py
# Run: python test_app.py
# =============================================================

"""
This script tests your Flask app in 'demo mode'.
It simulates a prediction so you can test the UI
before your model finishes training.
"""

import requests
import json
import os
from PIL import Image
import numpy as np

BASE_URL = "http://127.0.0.1:5000"

def test_health():
    """Test if Flask server is running."""
    print("[TEST] Health check...")
    try:
        r = requests.get(f"{BASE_URL}/health", timeout=5)
        data = r.json()
        print(f"  Status     : {data['status']}")
        print(f"  Model loaded: {data['model_loaded']}")
        print(f"  Classes    : {data['classes']}")
        print("  ✅ Server is running!\n")
        return True
    except requests.exceptions.ConnectionError:
        print("  ❌ Server not running. Start it with: python app.py\n")
        return False


def create_test_image(path="test_leaf.jpg"):
    """Create a dummy green image for testing."""
    # Create a 224x224 green image (simulating a leaf)
    arr = np.zeros((224, 224, 3), dtype=np.uint8)
    arr[:, :, 1] = 120   # Green channel
    arr[:, :, 0] = 40    # Some red
    img = Image.fromarray(arr)
    img.save(path)
    print(f"  Created test image: {path}")
    return path


def test_predict(image_path, lang="en"):
    """Test the /predict endpoint."""
    print(f"[TEST] Prediction (lang={lang})...")
    try:
        with open(image_path, "rb") as f:
            r = requests.post(
                f"{BASE_URL}/predict",
                files={"image": ("test.jpg", f, "image/jpeg")},
                data={"lang": lang},
                timeout=30
            )

        if r.status_code == 200:
            data = r.json()
            pred = data["prediction"]
            print(f"  Disease    : {pred['display_name']}")
            print(f"  Confidence : {pred['confidence']}%")
            print(f"  Severity   : {pred['severity']}")
            print(f"  Treatment  : {pred['treatment'][0][:60]}...")
            print("  ✅ Prediction successful!\n")
        else:
            print(f"  ❌ Error {r.status_code}: {r.json()}\n")

    except Exception as e:
        print(f"  ❌ Exception: {e}\n")


def test_classes():
    """Test the /classes endpoint."""
    print("[TEST] Classes endpoint...")
    try:
        r = requests.get(f"{BASE_URL}/classes")
        data = r.json()
        print(f"  Total supported classes: {data['count']}")
        if data['classes']:
            print(f"  First class: {data['classes'][0]}")
        print("  ✅ Classes endpoint OK!\n")
    except Exception as e:
        print(f"  ❌ {e}\n")


if __name__ == "__main__":
    print("=" * 50)
    print("  Plant Disease Classifier - Test Suite")
    print("=" * 50 + "\n")

    if not test_health():
        print("Start the server first: python app.py")
        exit(1)

    img_path = create_test_image()
    print()

    test_predict(img_path, lang="en")
    test_predict(img_path, lang="hi")
    test_classes()

    # Cleanup
    if os.path.exists(img_path):
        os.remove(img_path)

    print("=" * 50)
    print("All tests done! Open http://127.0.0.1:5000 in your browser.")
    print("=" * 50)
