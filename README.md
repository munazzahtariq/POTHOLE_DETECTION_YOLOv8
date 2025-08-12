# POTHOLE_DETECTION_YOLOv8
Pothole detection using Ultralytics YOLOv8 — trained on a custom dataset.

##  Overview
A computer vision project for detecting potholes in road imagery using the **YOLOv8** object detection model.  
This system is designed for real-time performance and can be used with **images, videos, or live webcam feeds**.  
It leverages deep learning to assist in **automated road monitoring and maintenance systems**.

---

##  Model Description
This project uses the **Ultralytics YOLOv8** object detection framework, known for its speed and accuracy.

**YOLOv8 Key Improvements:**
- Reworked backbone and head architecture  
- Better performance with fewer parameters  
- Native support for training, validation, and prediction workflows  
- Support for custom dataset training using YAML configuration  

The model is trained to detect **potholes** using labeled datasets and can identify them in **real-time** across:
- Images
- Video frames
- Live webcam streams

---

##  Datasets Used
The model was trained using a combination of open-source annotated datasets:

- [michelpf/dataset-pothole](https://github.com/michelpf/dataset-pothole)  
- [jaygala24/Pothole-Detection-Dataset](https://github.com/jaygala24/pothole-detection?tab=readme-ov-file)  

These datasets include a variety of pothole images with bounding box annotations, taken in **different lighting and road conditions**.  
I combined both datasets into a single dataset and then split it into **training** and **validation** sets.

---

##  Project Structure
```plaintext
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
```
##Detection Results
The model detects potholes in images as well as in video frames with high accuracy.
A folder is provided showing detected potholes in both images and videos.

##VIDEO CREDITS
Some testing videos are sourced from [Hole Stock Videos by Vecteezy](https://www.vecteezy.com/free-videos/hole).





