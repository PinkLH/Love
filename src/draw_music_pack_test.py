import turtle
import time
import pygame
import threading
import sys
import os

# 资源文件访问路径
# 变量"base_path"是绝对路径
# 变量"relative_path"是相对路径
# "sys.MEIPASS"的值就是程序运行时创建"_MEIxxxxxx"临时文件夹的绝对路径
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):       # 判断sys是否有"frozen"属性
        base_path = sys._MEIPASS            # 创建的"_MEIxxxxxx"临时文件夹的绝对路径
    else:
        base_path = os.path.abspath(".")    # 当前文件夹的绝对路径
    return os.path.join(base_path, relative_path)   # 合并绝对路径和相对路径，返回资源文件最终的路径

# 播放音乐
def music():
    filepath = resource_path("datas\music\晴天.mp3")    # 音乐文件路径
    pygame.mixer.init()                     # 初始化混音器模块
    while True:                             # 循环播放
        pygame.mixer.music.load(filepath)   # 将音乐文件导入混音器
        pygame.mixer.music.set_volume(1.0)  # 设置音量 0.0 ~ 1.0
        pygame.mixer.music.play(start=0.0)  # 从0.0秒处开始播放
        time.sleep(270)                     # 设置播放时长
        pygame.mixer.music.stop()           # 结束播放

def go_to(x, y, state):
    turtle.pendown() if state else turtle.penup()
    turtle.goto(x, y)

def draw_line(length, angle, state):
    turtle.pensize(1)
    turtle.pendown()
    turtle.setheading(angle)
    turtle.fd(length)
    turtle.bk(length) if state else turtle.penup()
    turtle.penup()

def draw_feather(size):
    angle = 30
    feather_num = size // 6
    feather_length = size // 3
    feather_gap = size // 10
    for i in range(feather_num):
        draw_line(feather_gap, angle + 180, False)
        draw_line(feather_length, angle + 145, True)
    draw_line(feather_length, angle + 145, False)
    draw_line(feather_num * feather_gap, angle, False)
    draw_line(feather_length, angle + 145 + 180, False)
    for i in range(feather_num):
        draw_line(feather_gap, angle + 180, False)
        draw_line(feather_length, angle - 145, True)
    draw_line(feather_length, angle - 145, False)
    draw_line(feather_num * feather_gap, angle, False)
    draw_line(feather_length, angle - 145 + 180, False)

def draw_heart(size):
    turtle.color('red', 'pink')
    turtle.pensize(2)
    turtle.pendown()
    turtle.setheading(150)
    turtle.begin_fill()
    turtle.fd(size)
    turtle.circle(size * -3.745, 45)
    turtle.circle(size * -1.431, 165)
    turtle.left(120)
    turtle.circle(size * -1.431, 165)
    turtle.circle(size * -3.745, 45)
    turtle.fd(size)
    turtle.end_fill()

def draw_arrow(size):
    angle = 30
    turtle.color('black')
    draw_feather(size)
    turtle.pensize(4)
    turtle.setheading(angle)
    turtle.pendown()
    turtle.fd(size * 2)
    turtle.penup()
    turtle.fd(size * 5.9)
    turtle.pendown()
    turtle.fd(size * 1.5)
    turtle.left(150)
    turtle.fd(20)
    turtle.bk(20)
    turtle.left(60)
    turtle.fd(20)

def arrow_heart(x, y, size):
    go_to(x, y, False)
    draw_heart(size * 1.15)
    turtle.setheading(-150)
    turtle.penup()
    turtle.fd(size * 2.2)
    draw_heart(size)
    turtle.penup()
    turtle.setheading(150)
    turtle.fd(size * 2.2)
    draw_arrow(size)

def draw_people(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pensize(2)
    turtle.color('black')
    turtle.setheading(0)
    turtle.circle(60, 360)
    turtle.penup()
    turtle.setheading(90)
    turtle.fd(75)
    turtle.setheading(180)
    turtle.fd(20)
    turtle.pensize(4)
    turtle.pendown()
    turtle.circle(2, 360)
    turtle.setheading(0)
    turtle.penup()
    turtle.fd(40)
    turtle.pensize(4)
    turtle.pendown()
    turtle.circle(-2, 360)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(-90)
    turtle.pendown()
    turtle.fd(20)
    turtle.setheading(0)
    turtle.fd(35)
    turtle.setheading(60)
    turtle.fd(10)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(-90)
    turtle.pendown()
    turtle.fd(40)
    turtle.setheading(0)
    turtle.fd(35)
    turtle.setheading(-60)
    turtle.fd(10)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(-90)
    turtle.pendown()
    turtle.fd(60)
    turtle.setheading(-135)
    turtle.fd(60)
    turtle.bk(60)
    turtle.setheading(-45)
    turtle.fd(30)
    turtle.setheading(-135)
    turtle.fd(35)
    turtle.penup()

def page0():
    turtle.penup()
    turtle.goto(-350, 0)
    turtle.color(0, 255, 255)
    turtle.write('给我最爱的xxx宝贝(❤ ω ❤)', font=('华文行楷', 40, 'normal'))
    time.sleep(3)

def page1():
    turtle.speed(10)
    draw_people(-250, 20)
    turtle.penup()
    turtle.goto(-150, -30)
    draw_heart(14)
    turtle.penup()
    turtle.goto(-20, -60)
    draw_heart(25)
    turtle.penup()
    turtle.goto(250, -100)
    draw_heart(45)
    turtle.hideturtle()
    time.sleep(2)

def page2():
    turtle.speed(1)
    turtle.penup()
    turtle.goto(-200, -200)
    turtle.color(0, 255, 255)
    turtle.pendown()
    turtle.write('xxx            xxx', font=('wisdom', 33, 'normal'))
    turtle.penup()
    turtle.goto(0, -180)
    draw_heart(10)
    arrow_heart(20, -60, 51)
    time.sleep(3)

def page3():
    turtle.penup()
    turtle.speed(10)
    turtle.goto(-350, 0)
    turtle.color(0, 255, 255)
    turtle.write('爱 你 哟 ❤ ❤ ❤', font=('宋体', 60, 'normal'))

def main():
    turtle.title("送给xxx宝贝")
    turtle.setup(900, 500)
    turtle.hideturtle()
    turtle.colormode(255)
    page0()
    turtle.clear()
    page1()
    turtle.clear()
    page2()
    page3()
    turtle.done()

if __name__ == '__main__':

    threading.Thread(target=music, daemon=True).start()

    try:
        main()
    except:
        print("意外退出!")