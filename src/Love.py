import turtle
import time
import pygame
import threading
import sys
import os
import tkinter

# 资源文件访问路径
# 变量"base_path"是绝对路径
# 变量"relative_path"是相对路径
# "sys.MEIPASS"的值就是程序运行时创建"_MEIxxxxxx"临时文件夹的绝对路径
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):                   # 判断sys是否有"frozen"属性
        base_path = sys._MEIPASS                        # 创建的"_MEIxxxxxx"临时文件夹的绝对路径
    else:
        base_path = os.path.abspath(".")                # 当前文件夹的绝对路径
    return os.path.join(base_path, relative_path)       # 合并绝对路径和相对路径，返回资源文件最终的路径

# 播放音乐
def music():
    filepath = resource_path("datas\music\晴天.mp3")    # 音乐文件路径
    pygame.mixer.init()                                 # 初始化混音器模块
    while True:                                         # 循环播放
        pygame.mixer.music.load(filepath)               # 将音乐文件导入混音器
        pygame.mixer.music.set_volume(1.0)              # 设置音量 0.0 ~ 1.0
        pygame.mixer.music.play(start=0.0)              # 从 0.0 秒处开始播放
        time.sleep(270)                                 # 设置播放时长
        pygame.mixer.music.stop()                       # 结束播放

# 作图
def go_to(x, y, state, turtle):
    turtle.pendown() if state else turtle.penup()
    turtle.goto(x, y)

def draw_line(length, angle, state, turtle):
    turtle.pensize(1)
    turtle.pendown()
    turtle.setheading(angle)
    turtle.fd(length)
    turtle.bk(length) if state else turtle.penup()
    turtle.penup()

def draw_feather(size, turtle):
    angle = 30
    feather_num = size // 6
    feather_length = size // 3
    feather_gap = size // 10
    for i in range(feather_num):
        draw_line(feather_gap, angle + 180, False, turtle)
        draw_line(feather_length, angle + 145, True, turtle)
    draw_line(feather_length, angle + 145, False, turtle)
    draw_line(feather_num * feather_gap, angle, False, turtle)
    draw_line(feather_length, angle + 145 + 180, False, turtle)
    for i in range(feather_num):
        draw_line(feather_gap, angle + 180, False, turtle)
        draw_line(feather_length, angle - 145, True, turtle)
    draw_line(feather_length, angle - 145, False, turtle)
    draw_line(feather_num * feather_gap, angle, False, turtle)
    draw_line(feather_length, angle - 145 + 180, False, turtle)

def draw_heart(size, turtle):
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

def draw_arrow(size, turtle):
    angle = 30
    turtle.color('black')
    draw_feather(size, turtle)
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

def arrow_heart(x, y, size, turtle):
    go_to(x, y, False, turtle)
    draw_heart(size * 1.15, turtle)
    turtle.setheading(-150)
    turtle.penup()
    turtle.fd(size * 2.2)
    draw_heart(size, turtle)
    turtle.penup()
    turtle.setheading(150)
    turtle.fd(size * 2.2)
    draw_arrow(size, turtle)

def draw_people(x, y, turtle):
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

# 第零页
def page0(turtle):
    turtle.penup()
    turtle.goto(-350, 0)
    turtle.color('#00FFFF')
    turtle.write('给我最爱的xxx宝贝(❤ ω ❤)', font=('华文行楷', 40, 'normal'))
    time.sleep(3)

# 第一页
def page1(turtle):
    turtle.speed(10)
    draw_people(-250, 20, turtle)
    turtle.penup()
    turtle.goto(-150, -30)
    draw_heart(14, turtle)
    turtle.penup()
    turtle.goto(-20, -60)
    draw_heart(25, turtle)
    turtle.penup()
    turtle.goto(250, -100)
    draw_heart(45, turtle)
    turtle.hideturtle()
    time.sleep(2)

# 第二页
def page2(turtle):
    turtle.speed(1)
    turtle.penup()
    turtle.goto(-200, -200)
    turtle.color("#00ffff")
    turtle.pendown()
    turtle.write('xxx            xxx', font=('wisdom', 33, 'normal'))
    turtle.penup()
    turtle.goto(0, -180)
    draw_heart(10, turtle)
    arrow_heart(20, -60, 51, turtle)
    time.sleep(3)

# 第三页
def page3(turtle):
    turtle.penup()
    turtle.speed(10)
    turtle.goto(-350, 0)
    turtle.color('#00FFFF')
    turtle.write('爱 你 哟 ❤ ❤ ❤', font=('宋体', 60, 'normal'))

# 作图主函数
def main(turtle):
    root.title("送给xxx宝贝")
    turtle.hideturtle()
    page0(turtle)                                           # 画第零页
    turtle.clear()                                          # 清除画布
    page1(turtle)                                           # 画第一页
    turtle.clear()                                          # 清除画布
    page2(turtle)                                           # 画第二页
    page3(turtle)                                           # 画第三页
    canva.mainloop()                                        # 窗口循环显示
    

# 主函数
if __name__ == '__main__':
    
    # 创建线程播放背景音乐
    threading.Thread(target=music, daemon=True).start()     

    # 创建一个窗口
    root = tkinter.Tk()                                     

    tk_width = 900                                          # 设置窗口的宽
    tk_height = 500                                         # 设置窗口的高

    # 窗口居中显示
    scn_width, scn_height = root.maxsize()                  # 获取屏幕宽度和高度
    cen_x = (scn_width - tk_width) / 2                      # 求窗口居中的x坐标
    cen_y = (scn_height - tk_height) / 2                    # 求窗口居中的y坐标
    size_wh = "%dx%d+%d+%d" % (tk_width, tk_height, cen_x, cen_y)   # 设置窗口居中的参数
    root.geometry(size_wh)                                  # 移动窗口到居中

    # 更换界面Logo
    ico = resource_path("datas\images\love.ico")            # 要更换的Logo文件路径
    root.iconbitmap(ico)

    # 在窗口里创建一个画布并设置宽度和高度
    canva = tkinter.Canvas(root, width=tk_width, height=tk_height)
    canva.pack()

    # 让turtle作图在创建的画布上运行
    path = turtle.RawTurtle(canva)

    # 开始作图
    try:
        main(path)
    except:
        print("意外退出!")
    
