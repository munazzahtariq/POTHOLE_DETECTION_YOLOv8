import os

# Base dataset path (this already points to train images folder)
train_images_path = r"C:\Users\Hp\OneDrive\Desktop\OPENCV\OPENCV PROJECTS\yolov4\DATASET_OF_YOLOv4\dataset\images\train"
val_images_path = r"C:\Users\Hp\OneDrive\Desktop\OPENCV\OPENCV PROJECTS\yolov4\DATASET_OF_YOLOv4\dataset\images\val"

# Output .txt files (save alongside image folders or wherever you prefer)
train_txt_path = r"C:\Users\Hp\OneDrive\Desktop\OPENCV\OPENCV PROJECTS\yolov4\DATASET_OF_YOLOv4\dataset\train.txt"
val_txt_path = r"C:\Users\Hp\OneDrive\Desktop\OPENCV\OPENCV PROJECTS\yolov4\DATASET_OF_YOLOv4\dataset\val.txt"

# Helper function to get image paths
def get_image_paths(folder):
    image_paths = []
    for filename in os.listdir(folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            full_path = os.path.join(folder, filename)
            image_paths.append(full_path.replace("\\", "/"))  # forward slashes for Darknet
    return image_paths

# Write train.txt
with open(train_txt_path, "w") as f:
    for path in get_image_paths(train_images_path):
        f.write(path + "\n")

# Write val.txt
with open(val_txt_path, "w") as f:
    for path in get_image_paths(val_images_path):
        f.write(path + "\n")

print("✅ train.txt and val.txt files created successfully.")
