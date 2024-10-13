## U-Net Model for Forest Classification and Segmentation

This repository contains the implementation of a U-Net model designed for automatic forest classification and segmentation. This project was developed during my internship at the Ministry of Defence of Azerbaijan, where the goal was to apply deep learning techniques to classify and segment forest regions from aerial imagery. 

## Project Overview
The goal of this project is to classify and segment forest regions in aerial images using a U-Net model. The U-Net architecture is well-suited for tasks involving image segmentation, where pixel-level classification is required. This project uses a custom dataset gathered specifically for this task.

## Dataset
The dataset used for training and validation consists of aerial images, annotated to mark forest regions. Each image has a corresponding mask, where each pixel indicates whether it belongs to a forested area or not.

## Training
The model is trained using:

Optimizer: Adam
Loss function: Binary Cross-Entropy
Metrics: Accuracy, Dice coefficient
During training, the model achieved:

Training Loss: 0.1472
Training Accuracy: 92.26%
Validation Loss: 0.3557
Validation Accuracy: 78.49%

These results suggest overfitting, so further fine-tuning of hyperparameters, such as learning rate and regularization techniques, could improve performance. But I wasn't able to finish the project during the time of internship. I will adjust it in the future.

## Results
The U-Net model effectively classifies and segments forest areas in aerial images. Below is a summary of the performance:

Training Accuracy: 92.26%
Validation Accuracy: 78.49%
