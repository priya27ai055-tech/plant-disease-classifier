# =============================================================
# Phase 2: Model Training with Transfer Learning (MobileNetV2)
# File: train.py
# Description: Build, train, and save CNN model
# =============================================================

import os
import json
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import (Dense, GlobalAveragePooling2D,
                                     Dropout, BatchNormalization)
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import (ModelCheckpoint, EarlyStopping,
                                        ReduceLROnPlateau, TensorBoard)
from tensorflow.keras.preprocessing.image import ImageDataGenerator

print(f"[INFO] TensorFlow version: {tf.__version__}")
print(f"[INFO] GPU available: {tf.config.list_physical_devices('GPU')}")

# ---------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------
DATASET_PATH     = "dataset/PlantVillage"
IMG_SIZE         = (224, 224)
BATCH_SIZE       = 32
EPOCHS_PHASE1    = 10     # Train only new top layers (frozen base)
EPOCHS_PHASE2    = 20     # Fine-tune top layers of MobileNetV2
VALIDATION_SPLIT = 0.2
LEARNING_RATE    = 1e-3
MODEL_SAVE_PATH  = "model/plant_disease_model.h5"

os.makedirs("model", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# ---------------------------------------------------------------
# Step 1: Recreate data generators (same as preprocess.py)
# ---------------------------------------------------------------
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    validation_split=VALIDATION_SPLIT,
    rotation_range=25,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest"
)
val_datagen = ImageDataGenerator(rescale=1.0 / 255, validation_split=VALIDATION_SPLIT)

train_gen = train_datagen.flow_from_directory(
    DATASET_PATH, target_size=IMG_SIZE, batch_size=BATCH_SIZE,
    class_mode="categorical", subset="training", shuffle=True, seed=42
)
val_gen = val_datagen.flow_from_directory(
    DATASET_PATH, target_size=IMG_SIZE, batch_size=BATCH_SIZE,
    class_mode="categorical", subset="validation", shuffle=False, seed=42
)

NUM_CLASSES = train_gen.num_classes
print(f"[INFO] Number of classes: {NUM_CLASSES}")

# Save class names
class_indices = train_gen.class_indices
class_names = {str(v): k for k, v in class_indices.items()}
with open("model/class_names.json", "w") as f:
    json.dump(class_names, f, indent=2)
print("[INFO] Class names saved.")

# ---------------------------------------------------------------
# Step 2: Build the Model using Transfer Learning
#
# WHAT IS TRANSFER LEARNING?
# MobileNetV2 is a model pre-trained on ImageNet (1.2M images).
# Instead of training from scratch, we:
#   1. Take MobileNetV2 (without its top classification layer)
#   2. Freeze it (don't update its weights initially)
#   3. Add our own layers on top for plant disease classification
#   4. Train only our top layers first
#   5. Then "unfreeze" some MobileNetV2 layers and fine-tune
# ---------------------------------------------------------------

print("\n[INFO] Building model...")

# Load MobileNetV2 pre-trained on ImageNet
base_model = MobileNetV2(
    input_shape=IMG_SIZE + (3,),   # (224, 224, 3)
    include_top=False,              # Don't include ImageNet classifier
    weights="imagenet"              # Use pre-trained weights
)

# Freeze all layers of the base model
base_model.trainable = False
print(f"[INFO] Base model layers: {len(base_model.layers)} (all frozen)")

# Add custom classification head
x = base_model.output
x = GlobalAveragePooling2D()(x)        # Reduce spatial dimensions
x = BatchNormalization()(x)            # Normalize activations
x = Dense(512, activation="relu")(x)  # Fully connected layer
x = Dropout(0.4)(x)                   # Prevent overfitting (40% dropout)
x = Dense(256, activation="relu")(x)  # Second FC layer
x = Dropout(0.3)(x)
predictions = Dense(NUM_CLASSES, activation="softmax")(x)  # Output layer

model = Model(inputs=base_model.input, outputs=predictions)

# ---------------------------------------------------------------
# Step 3: Phase 1 Training - Train only the new top layers
# ---------------------------------------------------------------
print("\n[PHASE 1] Training top layers (base model frozen)...")

model.compile(
    optimizer=Adam(learning_rate=LEARNING_RATE),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

callbacks_phase1 = [
    ModelCheckpoint(
        "model/best_phase1.h5",
        monitor="val_accuracy",
        save_best_only=True,
        verbose=1
    ),
    EarlyStopping(
        monitor="val_accuracy",
        patience=5,
        restore_best_weights=True,
        verbose=1
    ),
    ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.5,
        patience=3,
        min_lr=1e-6,
        verbose=1
    )
]

history1 = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=EPOCHS_PHASE1,
    callbacks=callbacks_phase1,
    verbose=1
)

# ---------------------------------------------------------------
# Step 4: Phase 2 Training - Fine-tune top layers of MobileNetV2
#
# After phase 1, the new top layers are trained well.
# Now we unfreeze the top layers of MobileNetV2 and fine-tune
# the entire network with a VERY LOW learning rate.
# ---------------------------------------------------------------
print("\n[PHASE 2] Fine-tuning - unfreezing top MobileNetV2 layers...")

# Unfreeze last 30 layers of MobileNetV2
base_model.trainable = True
for layer in base_model.layers[:-30]:
    layer.trainable = False

trainable_count = sum(1 for l in model.layers if l.trainable)
print(f"[INFO] Trainable layers now: {trainable_count}")

# Recompile with a much lower learning rate
model.compile(
    optimizer=Adam(learning_rate=1e-4),   # 10x smaller LR for fine-tuning
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

callbacks_phase2 = [
    ModelCheckpoint(
        MODEL_SAVE_PATH,
        monitor="val_accuracy",
        save_best_only=True,
        verbose=1
    ),
    EarlyStopping(
        monitor="val_accuracy",
        patience=7,
        restore_best_weights=True,
        verbose=1
    ),
    ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.3,
        patience=4,
        min_lr=1e-7,
        verbose=1
    ),
    TensorBoard(log_dir="logs/", histogram_freq=1)
]

history2 = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=EPOCHS_PHASE2,
    callbacks=callbacks_phase2,
    verbose=1
)

# ---------------------------------------------------------------
# Step 5: Evaluate and plot results
# ---------------------------------------------------------------
print(f"\n[INFO] Model saved to: {MODEL_SAVE_PATH}")

val_loss, val_acc = model.evaluate(val_gen, verbose=0)
print(f"[RESULT] Final Validation Accuracy : {val_acc * 100:.2f}%")
print(f"[RESULT] Final Validation Loss     : {val_loss:.4f}")

# Combine histories
def combine_histories(h1, h2, key):
    return h1.history[key] + h2.history[key]

acc      = combine_histories(history1, history2, "accuracy")
val_acc  = combine_histories(history1, history2, "val_accuracy")
loss     = combine_histories(history1, history2, "loss")
val_loss = combine_histories(history1, history2, "val_loss")

plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
plt.plot(acc,     label="Train Accuracy",      color="#4CAF50")
plt.plot(val_acc, label="Val Accuracy",        color="#2196F3")
plt.axvline(x=EPOCHS_PHASE1, color="red", linestyle="--", label="Fine-tuning starts")
plt.title("Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(loss,     label="Train Loss",  color="#FF5722")
plt.plot(val_loss, label="Val Loss",    color="#9C27B0")
plt.axvline(x=EPOCHS_PHASE1, color="red", linestyle="--", label="Fine-tuning starts")
plt.title("Model Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("model/training_curves.png", dpi=150)
plt.show()
print("[INFO] Training curves saved to model/training_curves.png")
print("\n[SUCCESS] Phase 2 Complete! Model is ready.")
