import os
import shutil

# Correct source path — points directly to where images and .txt files are
source_path = r"C:\Users\Hp\OneDrive\Desktop\OPENCV\OPENCV PROJECTS\yolov4\DATASET_OF_YOLOv4\Pothole Dataset"

# Destination folders (will be created inside the 'dataset-pothole-main' folder)
base_path = r"C:\Users\Hp\OneDrive\Desktop\OPENCV\OPENCV PROJECTS\yolov4\DATASET_OF_YOLOv4\dataset-pothole-main"
images_folder = os.path.join(base_path, "images")
labels_folder = os.path.join(base_path, "labels")
os.makedirs(images_folder, exist_ok=True)
os.makedirs(labels_folder, exist_ok=True)

# Move files from train folder to 'images' and 'labels'
for filename in os.listdir(source_path):
    full_path = os.path.join(source_path, filename)
    if os.path.isfile(full_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            shutil.move(full_path, os.path.join(images_folder, filename))
        elif filename.lower().endswith('.txt'):
            shutil.move(full_path, os.path.join(labels_folder, filename))

print("✅ Dataset successfully split into 'images' and 'labels' folders.")
