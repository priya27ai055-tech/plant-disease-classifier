# =============================================================
# Phase 1: Data Preprocessing
# File: preprocess.py
# Description: Load, augment, and prepare PlantVillage dataset
# =============================================================

import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# ---------------------------------------------------------------
# CONFIGURATION - Edit these paths to match your dataset location
# ---------------------------------------------------------------
DATASET_PATH = "dataset/PlantVillage"   # Folder containing class subfolders
IMG_SIZE     = (224, 224)               # MobileNetV2 expects 224x224
BATCH_SIZE   = 32
VALIDATION_SPLIT = 0.2                  # 80% train, 20% validation

# ---------------------------------------------------------------
# Step 1: Data Augmentation (makes model more robust)
# Augmentation = artificially creating variations of training images
# so the model does not memorize them but learns features.
# ---------------------------------------------------------------

train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,            # Normalize pixel values from 0-255 to 0-1
    validation_split=VALIDATION_SPLIT,

    # --- Augmentation techniques ---
    rotation_range=25,            # Randomly rotate images up to 25 degrees
    width_shift_range=0.1,        # Shift image horizontally
    height_shift_range=0.1,       # Shift image vertically
    shear_range=0.1,              # Shear transformation
    zoom_range=0.2,               # Random zoom in/out
    horizontal_flip=True,         # Mirror images left-right
    fill_mode="nearest"           # Fill empty pixels after transforms
)

# Validation data: only rescale, NO augmentation
val_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    validation_split=VALIDATION_SPLIT
)

# ---------------------------------------------------------------
# Step 2: Create data generators (reads images from folders)
# Your folder structure must be:
#   dataset/PlantVillage/
#       Apple___Apple_scab/  (contains .jpg images)
#       Apple___healthy/
#       Tomato___Late_blight/
#       ... etc
# ---------------------------------------------------------------

print("[INFO] Loading training data...")
train_generator = train_datagen.flow_from_directory(
    DATASET_PATH,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",     # One-hot encoded labels
    subset="training",            # This is the training portion
    shuffle=True,
    seed=42
)

print("[INFO] Loading validation data...")
val_generator = val_datagen.flow_from_directory(
    DATASET_PATH,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="validation",          # This is the validation portion
    shuffle=False,
    seed=42
)

# ---------------------------------------------------------------
# Step 3: Save class names (we need these during prediction)
# ---------------------------------------------------------------
class_indices = train_generator.class_indices  # e.g. {'Apple___scab': 0, ...}
class_names   = {v: k for k, v in class_indices.items()}  # Reverse: {0: 'Apple___scab', ...}

# Save class names to a file so Flask app can load them later
import json
os.makedirs("model", exist_ok=True)
with open("model/class_names.json", "w") as f:
    json.dump(class_names, f, indent=2)

print(f"\n[INFO] Total classes found : {train_generator.num_classes}")
print(f"[INFO] Training samples    : {train_generator.samples}")
print(f"[INFO] Validation samples  : {val_generator.samples}")
print(f"[INFO] Class names saved to: model/class_names.json")

# ---------------------------------------------------------------
# Step 4: Visualize a sample batch (sanity check)
# ---------------------------------------------------------------
def visualize_samples(generator, n=9):
    images, labels = next(generator)
    plt.figure(figsize=(10, 10))
    for i in range(min(n, len(images))):
        plt.subplot(3, 3, i + 1)
        plt.imshow(images[i])
        label_idx = np.argmax(labels[i])
        plt.title(class_names[label_idx].replace("___", "\n"), fontsize=8)
        plt.axis("off")
    plt.suptitle("Sample Training Images (after augmentation)", fontsize=12)
    plt.tight_layout()
    plt.savefig("model/sample_images.png")
    plt.show()
    print("[INFO] Sample image saved to model/sample_images.png")

visualize_samples(train_generator)

print("\n[SUCCESS] Phase 1 Complete! Generators are ready.")
print("Run train.py next to start model training.")
