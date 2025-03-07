import numpy as np
import matplotlib.pyplot as plt

# 도트 그림을 그릴 데이터 생성
# 예를 들어, 10x10 크기의 도트 그림을 생성
data = np.zeros((30, 30))

# 도트 위치 설정 (임의로 몇 개의 도트를 설정)
data[2, 10:20] = 1
data[3, 8:10] = 1
data[3, 20:22] = 1
data[4, 5] = 1
data[6, 7] = 1
data[8, 1] = 1

# 도트 그림 그리기
plt.imshow(data, cmap='gray', interpolation='nearest')
plt.title('Dot Plot')
plt.show()