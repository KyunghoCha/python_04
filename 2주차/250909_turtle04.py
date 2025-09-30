import turtle

t = turtle.Turtle()
t.shape('turtle')

# 펜을 올리고 시작 위치로 이동
t.penup()
t.goto(-200, 0)
t.pendown()

# 파란색 원
t.color('blue')
t.circle(100)

# 펜을 올리고 두 번째 원의 위치로 이동
t.penup()
t.goto(-50, 0)
t.pendown()

# 검은색 원
t.color('black')
t.circle(100)

# 펜을 올리고 세 번째 원의 위치로 이동
t.penup()
t.goto(100, 0)
t.pendown()

# 빨간색 원
t.color('red')
t.circle(100)

# 펜을 올리고 네 번째 원의 위치로 이동
t.penup()
t.goto(-125, -100)
t.pendown()

# 노란색 원
t.color('yellow')
t.circle(100)

# 펜을 올리고 다섯 번째 원의 위치로 이동
t.penup()
t.goto(25, -100)
t.pendown()

# 초록색 원
t.color('green')
t.circle(100)

turtle.done()