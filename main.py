from time import time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.models import Sequential
from keras.preprocessing import image
from keras.callbacks import EarlyStopping

def plot_history(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']

    plt.figure(figsize=(20, 8))
    plt.subplot(1, 2, 1)
    plt.plot(range(len(acc)), acc, label='Training Accuracy')
    plt.plot(range(len(val_acc)), val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(range(len(loss)), loss, label='Training Loss')
    plt.plot(range(len(val_loss)), val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.show()

BATCH_SIZE = 32
IMG_HEIGHT = 64
IMG_WIDTH = 64
EPOCHS = 25
DATA_DIR_PATH = r"D:\repo\forest_detection\data_classified"

num_parameters_time = {}
num_parameters_accuracy = {}
num_parameters = {}

TRAIN_DATASET = tf.keras.utils.image_dataset_from_directory(
  DATA_DIR_PATH,
  validation_split=0.1,
  subset="training",
  seed=123,
  image_size=(IMG_HEIGHT, IMG_WIDTH),
  batch_size=BATCH_SIZE)

VALIDATION_DATASET = tf.keras.utils.image_dataset_from_directory(
  DATA_DIR_PATH,
  validation_split=0.1,
  subset="validation",
  seed=123,
  image_size=(IMG_HEIGHT, IMG_WIDTH),
  batch_size=BATCH_SIZE)

CLASS_NAMES = TRAIN_DATASET.class_names

plt.figure(figsize=(10, 10))
for images, labels in TRAIN_DATASET.take(1):
  for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(images[i].numpy().astype("uint8"))
    plt.title(CLASS_NAMES[labels[i]])
    plt.axis("off")

model = Sequential([
  layers.Rescaling(1./255, input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
  layers.Conv2D(16, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(128, activation='relu'),
  layers.Dense(len(CLASS_NAMES))
])

model.compile(optimizer='adam',
              loss= tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.summary()

start = time()

history = model.fit(
  TRAIN_DATASET,
  validation_data=VALIDATION_DATASET,
  epochs=EPOCHS
)

end = time()

elapsed_time = end - start

print(f"Elapsed Time:{elapsed_time}s")


num_parameters["Base"] = 548258
num_parameters_time["Base"] = elapsed_time
num_parameters_accuracy["Base"] = history.history["val_accuracy"][-1]

plot_history(history)

TRAIN_DATASET = tf.keras.utils.image_dataset_from_directory(
  DATA_DIR_PATH,
  validation_split=0.1,
  subset="training",
  color_mode="grayscale",
  seed=123,
  image_size=(IMG_HEIGHT, IMG_WIDTH),
  batch_size=BATCH_SIZE)

VALIDATION_DATASET = tf.keras.utils.image_dataset_from_directory(
  DATA_DIR_PATH,
  validation_split=0.1,
  subset="validation",
  color_mode="grayscale",
  seed=123,
  image_size=(IMG_HEIGHT, IMG_WIDTH),
  batch_size=BATCH_SIZE)

plt.figure(figsize=(10, 10))
for images, labels in TRAIN_DATASET.take(1):
  for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(images[i].numpy().astype("uint8"))
    plt.title(CLASS_NAMES[labels[i]])
    plt.axis("off")

