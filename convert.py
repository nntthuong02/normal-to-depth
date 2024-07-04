import cv2
import numpy as np
import os
from sklearn.preprocessing import normalize

def normalize_normals(normals):
    magnitude = np.linalg.norm(normals, axis=2, keepdims=True)
    return normals / (magnitude + 1e-8)  # Thêm một giá trị nhỏ để tránh chia cho 0

def convert_image_to_coordinates(image_path, output_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    
    if image is None:
        print(f"Could not read the image from {image_path}")
        return

    # Swap the B and R channels
    image[..., 0], image[..., 2] = image[..., 2], image[..., 0].copy()

    # Create a mask for the background
    mask_bg = (image[..., 2] == 0)

    # Convert the image to float32
    image = image.astype(np.float32)

    # Convert the RGB values to the range [-1, 1] for x and y, and [0, 1] for z
    image[..., 0] = image[..., 0] * 2 / 255 - 1
    image[..., 1] = image[..., 1] * 2 / 255 - 1
    image[..., 2] = (image[..., 2] - 128) / 127

    # Normalize the normals
    image = normalize(image.reshape(-1, 3)).reshape(image.shape)

    # Fill the background with [0, 0, 0]
    image[mask_bg] = [0, 0, 0]

    # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the coordinates array to a .npy file
    np.save(output_path, image)

# Nhập tên file ảnh và vị trí lưu file đầu ra từ bàn phím
image_filename = input("Nhập tên file ảnh (ví dụ: scholar.png): ")
output_filename = input("Nhập đường dẫn lưu file đầu ra (ví dụ: scholar/scholar_normal): ")

# Xây dựng đường dẫn đầy đủ cho file đầu vào và đầu ra
image_path = os.path.join('image', image_filename)
output_path = os.path.join('output-normal', f"{output_filename}.npy")

# Chuyển đổi ảnh và lưu kết quả
convert_image_to_coordinates(image_path, output_path)
