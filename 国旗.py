from turtle import *
setup(700 , 550 , 80 , 80)

#国旗底
penup()
fd(-160)
seth(90)
fd(115)
seth(0)
color('red' , 'red')
begin_fill()
pendown()
fd(335)
seth(-90)
fd(225)
seth(180)
fd(335)
seth(90)
fd(225)
end_fill()

#星星1
penup()
seth(0)
fd(60)
seth(-90)
fd(27)
seth(-72)
pendown()
color('yellow')
begin_fill()
for i in range(5):
    fd(63)
    right(144)
end_fill()

#小星星2
penup()
seth(0)
fd(71)
seth(-162)
pendown()
color('yellow')
begin_fill()
for i in range(5):
    fd(25)
    right(144)
end_fill()

#小星星3
penup()
seth(-90)
fd(27)
seth(18)
pendown()
color('yellow')
begin_fill()
for i in range(5):
    fd(25)
    right(144)
end_fill()

#小星星4
penup()
seth(-90)
fd(25)
seth(0)
fd(16)
seth(-78)
pendown()
color('yellow')
begin_fill()
for i in range(5):
    fd(25)
    right(144)
end_fill()

#小星星5
penup()
seth(-90)
fd(45)
seth(180)
fd(35)
seth(58)
pendown()
color('yellow')
begin_fill()
for i in range(5):
    fd(25)
    right(144)
end_fill()
penup()

ht()#隐藏箭头
