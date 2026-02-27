# 👤 Real-Time Face Detection & Blur using MediaPipe

## Overview
This project implements real-time face detection using MediaPipe and OpenCV. It detects faces from a webcam stream and optionally applies Gaussian blur to anonymize detected faces.

The system processes each video frame, identifies face bounding boxes, and allows toggling face blurring dynamically.

## Features
- Real-time face detection via webcam
- Bounding box visualization
- Optional face anonymization (Gaussian blur)
- Toggle blur on/off during execution
- Keyboard controls for interaction

## How It Works
1. Capture webcam frames using OpenCV.
2. Convert frames from BGR to RGB format.
3. Process frames using MediaPipe Face Detection.
4. Extract relative bounding box coordinates.
5. Convert to pixel coordinates.
6. Apply Gaussian blur to detected face regions (optional).
7. Display processed frame.

## Controls
- **Q** → Quit application
- **B** → Toggle face blur on/off

## Technologies Used
- Python
- OpenCV
- MediaPipe

## Applications
- Privacy-preserving video systems
- Real-time surveillance preprocessing
- Video anonymization tools
- Computer vision prototyping

## How to Run
1. Install dependencies:
