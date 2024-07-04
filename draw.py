import numpy as np
import matplotlib.pyplot as plt

# Đọc và hiển thị bản đồ độ sâu của các đỉnh
depth_filename = input("Enter the depth file name (e.g., scholar): ")
depth_path = depth_filename + "_output_depth.npy"
vertex_depth_map = np.load(depth_path)  # Thay 'output_name.npy' bằng tên tệp đầu ra thực tế
plt.imshow(vertex_depth_map, cmap='gray')  # Sử dụng cmap='gray' để hiển thị ảnh đen trắng
plt.title('Vertex Depth Map')
plt.show()


# import numpy as np
# import matplotlib.pyplot as plt

# # Đọc và hiển thị bản đồ độ sâu của các đỉnh
# vertex_depth_map = np.load('output_name_depth.npy')  # Thay 'output_name_depth.npy' bằng tên tệp đầu ra thực tế

# # Xác định ngưỡng thích hợp dựa trên dữ liệu độ sâu
# threshold = np.mean(vertex_depth_map)  # Sử dụng ngưỡng là giá trị trung bình của độ sâu
# binary_depth_map = np.where(vertex_depth_map > threshold, 1, 0)

# # Hiển thị bản đồ độ sâu nhị phân (màu đen và trắng)
# plt.imshow(binary_depth_map, cmap='binary')
# plt.colorbar()
# plt.title('Binary Depth Map (Black and White)')
# plt.show()
