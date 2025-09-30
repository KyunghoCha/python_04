# p80 No. 05
from math import sqrt

print('2025-09-23, 21114073, 차경호')

x1 = int(input('첫 번째 점의 x 좌표를 입력하세요: '))
y1 = int(input('첫 번째 점의 y 좌표를 입력하세요: '))
x2 = int(input('두 번째 점의 x 좌표를 입력하세요: '))
y2 = int(input('두 번째 점의 y 좌표를 입력하세요: '))
print(f'두 점 사이의 거리: {sqrt((x1 - x2)**2 + (y1 - y2)**2)}')