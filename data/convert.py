import cv2
import numpy as np
import os

# Đường dẫn đến tệp hình ảnh đầu vào
input_image_path = 'data/scholar.png'

# Đường dẫn để lưu tệp .npy đầu ra
output_npy_path = 'data/test/scholar_output_depth.npy'

# Tạo thư mục đích nếu chưa tồn tại
os.makedirs(os.path.dirname(output_npy_path), exist_ok=True)

# Đọc hình ảnh sử dụng OpenCV
image = cv2.imread(input_image_path)

# Kiểm tra xem hình ảnh có được đọc thành công không
if image is not None:
    # Chuyển đổi hình ảnh sang định dạng numpy array
    image_array = np.array(image)

    # Lưu numpy array vào tệp .npy
    np.save(output_npy_path, image_array)
    print(f"Hình ảnh đã được chuyển đổi và lưu thành công tại {output_npy_path}")
else:
    print("Không thể đọc được hình ảnh từ đường dẫn đã cung cấp.")
