# p79 No. 03
print('2025-09-23, 21114073, 차경호')

num = int(input('4자리 정수를 입력하세요: '))
result = 0

result += num % 10
num //= 10
result += num % 10
num //= 10
result += num % 10
num //= 10
result += num % 10

print(f'각 자리수의 합: {result}')