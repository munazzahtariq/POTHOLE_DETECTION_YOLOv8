import os
import random
import shutil

# Set seed for reproducibility
random.seed(42)

# Paths
base_path = r"C:\Users\Hp\OneDrive\Desktop\OPENCV\OPENCV PROJECTS\yolov4\DATASET_OF_YOLOv4\dataset-pothole-main"
images_path = os.path.join(base_path, "images")
labels_path = os.path.join(base_path, "labels")

# Output folders
for split in ['train', 'val']:
    os.makedirs(os.path.join(images_path, split), exist_ok=True)
    os.makedirs(os.path.join(labels_path, split), exist_ok=True)

# List all image files
image_files = [f for f in os.listdir(images_path) if f.endswith((".jpg", ".png"))]

# Shuffle and split
random.shuffle(image_files)
split_index = int(len(image_files) * 0.8)
train_files = image_files[:split_index]
val_files = image_files[split_index:]

# Function to move image-label pairs
def move_pairs(file_list, split):
    for img_file in file_list:
        label_file = os.path.splitext(img_file)[0] + ".txt"

        # Source paths
        src_img = os.path.join(images_path, img_file)
        src_lbl = os.path.join(labels_path, label_file)

        # Dest paths
        dst_img = os.path.join(images_path, split, img_file)
        dst_lbl = os.path.join(labels_path, split, label_file)

        # Move files
        if os.path.exists(src_img) and os.path.exists(src_lbl):
            shutil.move(src_img, dst_img)
            shutil.move(src_lbl, dst_lbl)

# Move files
move_pairs(train_files, "train")
move_pairs(val_files, "val")

print("✅ Dataset successfully split into train and val folders.")
