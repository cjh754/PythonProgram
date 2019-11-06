import numpy as np
from skimage import io
import matplotlib.pyplot as plt

if __name__ == '__main__':
    photo_data = io.imread("sd-3layers.jpg") # 이미지불러오기
    total_rows, total_cols, total_layers = photo_data.shape # 이미지크기 및 차원알아보기
    X, Y = np.mgrid[:total_rows, :total_cols] # Broadcasting을 위한 차원 뻥튀기
    centX = int(total_rows // 2) # 중심 x좌표
    centY = int(total_cols // 2) # 중심 y좌표
    r = centX # 반지름
    d = ((centX - X) ** 2 + (centY - Y) ** 2) ** 0.5 # 각 점의 중심까지의 거리
    circular_mask = d > r # 반지름보다 큰 거리들(원의 밖)
    photo_data[circular_mask] = 255 # 원밖은 흰색으로 처리
    plt.figure(1) # 출력물1
    plt.imshow(photo_data)
    upper_half_mask = X > centX # 반보다 큰 X들
    composite_mask = np.logical_and(circular_mask, upper_half_mask) # 둘다 true인 mask
    photo_data[composite_mask] = 0 # 검은색으로
    plt.figure(2) # 출력물2
    plt.imshow(photo_data)
    plt.show()
