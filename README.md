# POTHOLE_DETECTION_YOLOv8
Pothole detection with Ultralytics YOLOv8 — trained on custom data.

#  Pothole Detection using YOLOv8

A computer vision project for detecting potholes in road imagery using the YOLOv8 object detection model. This system is designed for real-time performance and can be used with images, videos, or live webcam feeds. It leverages deep learning to assist in automated road monitoring and maintenance systems.

---

##  Model Description

This project uses the **Ultralytics YOLOv8** object detection framework, known for its speed and accuracy. YOLOv8 improves upon previous versions with:

- A reworked backbone and head architecture
- Better performance with fewer parameters
- Native support for training, validation, and prediction workflows
- Support for custom dataset training using YAML configuration

The model is trained to detect **potholes** using labeled datasets and can identify them in real-time across multiple formats (images, videos, webcam streams).

---

##  Datasets Used

I trained the model using a combination of open-source annotated datasets:

- [michelpf/dataset-pothole](https://github.com/michelpf/dataset-pothole)  
- [jaygala24/Pothole-Detection-Dataset](https://github.com/jaygala24/pothole-detection?tab=readme-ov-file)

These datasets include a variety of pothole images with bounding box annotations, taken in different lighting and road conditions.
I created the dataset by combining both of these datasets into single dataset and then split it into training and validation sets
---

##  Project Structure
POTHOLE_DETECTION_YOLOv8/
├── dataset/
│   ├── images/
│   │   ├── train/
│   │   └── val/
│   ├── labels/
│   │   ├── train/
│   │   └── val/
├── runs/
    └── detect/






