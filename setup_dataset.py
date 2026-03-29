"""
=============================================================
Dataset Setup Helper
File: setup_dataset.py
Description: Instructions + optional Kaggle download helper
=============================================================

HOW TO GET THE PLANTVILLAGE DATASET:
======================================

OPTION 1 (Recommended - Kaggle):
1. Go to: https://www.kaggle.com/datasets/emmarex/plantdisease
2. Click "Download" (you need a free Kaggle account)
3. Unzip the downloaded file
4. Move/rename so the folder structure is:
   plant_disease_project/
       dataset/
           PlantVillage/
               Apple___Apple_scab/
               Apple___Black_rot/
               Apple___healthy/
               Tomato___Late_blight/
               ... (38 folders total)

OPTION 2 (Kaggle API - run from terminal):
If you have kaggle CLI installed:
    pip install kaggle
    kaggle datasets download -d emmarex/plantdisease
    unzip plantdisease.zip -d dataset/
    mv dataset/PlantVillage dataset/PlantVillage

OPTION 3 (Google Colab - if local RAM is limited):
Upload this project to Google Drive, train on Colab,
download the saved .h5 model file, place in model/ folder.
"""

import os
import sys

def check_dataset():
    """Check if dataset exists and print structure info."""
    dataset_path = "dataset/PlantVillage"

    if not os.path.exists(dataset_path):
        print("❌ Dataset not found at:", dataset_path)
        print("\nPlease download it from Kaggle:")
        print("   https://www.kaggle.com/datasets/emmarex/plantdisease")
        print("\nThen extract it so the structure looks like:")
        print("   dataset/PlantVillage/Apple___Apple_scab/  (and 37 other folders)")
        return False

    classes = [d for d in os.listdir(dataset_path)
               if os.path.isdir(os.path.join(dataset_path, d))]

    if len(classes) == 0:
        print("❌ Dataset folder is empty!")
        return False

    print(f"✅ Dataset found! {len(classes)} classes detected.\n")
    print("Classes found:")
    total_images = 0
    for cls in sorted(classes):
        cls_path = os.path.join(dataset_path, cls)
        imgs = [f for f in os.listdir(cls_path)
                if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        print(f"   {cls:<45} {len(imgs):>5} images")
        total_images += len(imgs)

    print(f"\nTotal images: {total_images:,}")
    print("✅ Dataset is ready for training!\n")
    return True

def create_folder_structure():
    """Create all required project folders."""
    folders = [
        "dataset/PlantVillage",
        "model",
        "logs",
        "uploads",
        "templates",
        "static"
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    print("✅ Project folder structure created.\n")
    for folder in folders:
        print(f"   📁 {folder}/")

if __name__ == "__main__":
    print("=" * 55)
    print("  Plant Disease Classifier - Setup Check")
    print("=" * 55)
    print()
    create_folder_structure()
    print()
    check_dataset()
