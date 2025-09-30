# [LAB 07]
print('2025-09-23, 21114073, 차경호')

scores = []

score = int(input(f'1번 학생의 성적을 입력하세요: '))
scores.append(score)
score = int(input(f'2번 학생의 성적을 입력하세요: '))
scores.append(score)
score = int(input(f'3번 학생의 성적을 입력하세요: '))
scores.append(score)
score = int(input(f'4번 학생의 성적을 입력하세요: '))
scores.append(score)
score = int(input(f'5번 학생의 성적을 입력하세요: '))
scores.append(score)

max_score = max(scores)
min_score = min(scores)

print(f'최고 성적: {max_score}')
print(f'최저 성적: {min_score}')



# print('학생 5명의 성적을 입력하세요: ')
# for i in range(5):
#     score = int(input(f'{i + 1}번 학생의 성적을 입력하세요: '))
#     scores.append(score)