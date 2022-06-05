# Love

* *Author*:&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**黎宏**
* *Themes*:&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;**“示爱” “试爱” “似爱” “是爱” “誓爱”**
* *Expectations*:&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;**“钟于” “忠于” “衷于” “终于”**
* *Introduction*:&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;**一个基于Python Turtle库的画图程序，下文是实现步骤**
* *Programming Languages*:&emsp;**Python**

## 目录

1. [环境准备](#一环境准备)
2. [动画图案](#二动画图案)
3. [背景音乐](#三背景音乐)
4. [合并功能](#四合并功能)
5. [源码打包](#五源码打包)
6. [功能优化](#六功能优化)

&emsp;&emsp;6.1 [功能缺点](#功能缺点)

&emsp;&emsp;6.2 [优化方案](#优化方案)

7. [最终功能](#七最终功能)

## 一、环境准备
&emsp;安装好 **Python** 以及库:**`pygame`**,**`pyinstaller`**,**`pipenv`**.

**&emsp;Python**官网：[https://www.python.org/](https://www.python.org/)

&emsp;安装好 **Python** 后安装库(_在终端输入_)：
```cmd
pip install pygame
pip install pyinstaller
pip install pipenv
```

## 二、动画图案

**&emsp;原理：**
利用 **`turtle`**,**`time`** 库作出动画图案主体

&emsp;作图测试([**_draw_test.py_**](https://github.com/PinkLH/Love/blob/main/src/draw_test.py))：
```python
import turtle
import time

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
    turtle.write('给我最爱的豆豆宝贝(❤ ω ❤)', font=('STCaiyun', 40, 'normal'))
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
    turtle.write('黎 宏                 杜运熙', font=('STCaiyun', 33, 'normal'))
    turtle.penup()
    turtle.goto(0, -180)
    draw_heart(10)
    arrow_heart(20, -60, 51)
    time.sleep(3)

def page3():
    turtle.penup()
    turtle.speed(10)
    turtle.goto(-300, 0)
    turtle.color(0, 255, 255)
    turtle.write('爱 你 哟 ❤ ❤ ❤', font=('STCaiyun', 60, 'normal'))

def main():
    turtle.title("送给豆豆宝贝")
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
    try:
        main()
    except:
        print("意外退出!")
```

## 三、背景音乐
**&emsp;原理：**
创建一个线程用于 **`pygame`** 播放音乐，以达到利用 **`turtle`** 作图的同时播放音乐的目的

&emsp;音乐测试([**_music_test.py_**](https://github.com/PinkLH/Love/blob/main/src/music_test.py))：
```python
import pygame
import time
import threading

def music():
    filepath = "datas\music\晴天.mp3"       # 音乐文件路径
    pygame.mixer.init()                     # 初始化混音器模块
    while True:                             # 循环播放
        pygame.mixer.music.load(filepath)   # 将音乐文件导入混音器
        pygame.mixer.music.set_volume(1.0)  # 设置音量 0.0 ~ 1.0
        pygame.mixer.music.play(start=0.0)  # 从0.0秒处开始播放
        time.sleep(270)                     # 设置播放时长
        pygame.mixer.music.stop()           # 结束播放

if __name__ == '__main__':

    threading.Thread(target=music).start()  # 创建线程并启动
```

## 四、合并功能
&emsp;将以上功能合并得到源码 [**_draw_music_test.py_**](https://github.com/PinkLH/Love/blob/main/src/draw_music_test.py)


## 五、源码打包
&emsp;**原理：**
利用 **`pyinstaller`** 打包源码，使其变为exe运行文件，让任意windows电脑都能运行。

&emsp;**方法**：准备一个 **`ico_test.ico`** 的图标放在源码的文件夹，安装好 **`pyinstaller`** 后在终端进入源码所在的文件夹并输入 

```cmd
pyinstaller -F -w -i ico_test.ico draw_music_test.py
```
&emsp;然后就会在源码文件夹找到名为 **dist** 的文件夹，此文件夹里就是打包好的exe文件。

## 六、功能优化
### &emsp;功能缺点

&emsp;&emsp;**1**：利用第五步的方法打包成exe文件，它会把电脑上 **Python** 安装的所有的库都打包到exe文件中，如果电脑上的 **Python** 安装了很多的库，那么打包成的exe文件将非常大。

&emsp;&emsp;**2**：打包成exe文件后，必须把要用到的资源文件放在正确路径上才能运行，不能做到直接点击exe文件就直接运行的目的。

&emsp;&emsp;**3**：作图时，左上方的Logo是 **`turtle`** 库画板的默认Logo，不能将其更换成自己喜欢的Logo。



### &emsp;优化方案

&emsp;&emsp;**1：利用虚拟的 Python 环境打包**

&emsp;&emsp;**原理**：利用 **`pipenv`** 库创建一个虚拟的 **Python** 环境，再将要打包的源码所用到的库导入其中，最后再在此虚拟环境中利用 **`pyinstaller`** 进行打包。这样可以避免不需要的库也被打包到exe文件中，从而减小exe文件的大小。

&emsp;&emsp;**方法**：安装好 **`pipenv`** 库后在终端进入源码所在的文件夹并输入以下代码，创建一个虚拟的 **Python** 环境并进入。
```cmd
pipenv shell
```
&emsp;&emsp;此时该文件夹中会多出一个名为"**Pipfile**"的文件。接着运用 **`pip`** 命令在虚拟环境下安装需要用到的库。
```cmd
pip install pyinstaller
pip install pygame
```

&emsp;&emsp;最后在虚拟环境下用第五步的方法打包，在虚拟环境下输入。
```cmd
pyinstaller -F -w -i ico_test.ico draw_music_test.py
```

&emsp;&emsp;**2：将资源文件和源文件一起打包**

&emsp;&emsp;**原理**：**`pyinstaller`** 库在打包的时候会在 **sys** 模块中添加一个 "**frozen**" 属性，并且打包后的exe文件运行时会在电脑里创建一个名为 "**_MEIxxxxxx**" 的临时文件夹，此文件夹的路径在 **`C:\Users\用户名\AppData\Local\Temp`**，里面存放着一些运行此exe文件需要的并且已经编译好的文件。因此，要想达到只通过exe文件就直接运行的目的，就必须将资源文件和源文件一起打包。这样在运行exe文件后，资源文件就会出现在这个临时文件夹里。现在只需要在源码中判断 **sys** 模块是否有 "**frozen**" 属性，从而选择出资源文件正确的路径。


&emsp;&emsp;**方法**：在源码中加入以下函数
```python
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
```
&emsp;&emsp;源码中要用到路径的地方，统统利用此函数求。例如，求音乐文件的路径
```Python
filepath = resource_path("datas\music\晴天.mp3")    # 音乐文件路径
```

&emsp;&emsp;得到源码([**_draw_music_pack_test.py_**](https://github.com/PinkLH/Love/blob/main/src/draw_music_pack_test.py))。然后在打包的时候加上几个步骤。按照以上的步骤第一次打包后，删除打包时产生的其它的文件，只保留 _.spec_ 文件，然后打开 _.spec_ 文件，将其中的 "**datas**" 属性修改为要打包的资源文件的路径。将 "**icon**" 属性修改为exe文件图标的路径。_.spec_ 文件如下([**_draw_music_pack_test.spec_**](https://github.com/PinkLH/Love/blob/main/src/draw_music_pack_test.spec)):
```python
# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['draw_music_pack_test.py'],                   # 源码文件名称
             pathex=['E:\\Git\\Love\\src'],       # 源码文件路径
             binaries=[],
             datas=[('datas','datas')],                     # 资源文件的路径(两个都要填，两个都填一样的路径)
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='draw_music_pack_test',                              # exe文件名称
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='datas/images/love.ico')    # exe文件图标的路径
```

&emsp;&emsp;然后在虚拟的 Python 环境的终端输入以下代码进行打包。
```cmd
pyinstaller draw_music_pack_test.spec
```

&emsp;&emsp;至此，打包出来的exe文件就可以直接运行。以后要打包，就直接修改 _.spec_ 文件里的属性值就可以了。

&emsp;&emsp;**3：更换界面Logo**

&emsp;&emsp;**原理**：由于 **`turtle`** 库没有自带的换logo的方法，只有用 **`tkinter`** 库创建一个GUI窗口来作为 **`turtle`** 的画布，并利用 **`tkinter`** 库的`iconbitmap()`方法将此窗口的logo改为自己的logo。

&emsp;&emsp;**方法**：先在主函数创建一个窗口并设置一些属性。

```python
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
```

&emsp;&emsp;然后利用 **`tkinter`** 库的`iconbitmap()`方法更换界面Logo。

```python
# 更换界面Logo
ico = resource_path("datas\images\love.ico")            # 要更换的Logo文件路径
root.iconbitmap(ico)
```

&emsp;&emsp;然后在窗口里创建一个画布并设置宽度和高度。

```python
# 在窗口里创建一个画布并设置宽度和高度
canva = tkinter.Canvas(root, width=tk_width, height=tk_height)
canva.pack()
```

&emsp;&emsp;让 **turtle** 作图在创建的画布上运行。

```python
# 让turtle作图在创建的画布上运行
path = turtle.RawTurtle(canva)
```

&emsp;&emsp;然后将 **path** 变量作为 **turtle** 传入主函数，并在每个函数上加上一个 **turtle ** 形参。

```python
# 开始作图
try:
    main(path)
except:
	print("意外退出!")
```

&emsp;&emsp;最后修改作图主函数的标题和显示方式。

```python
# 作图主函数
def main(turtle):
    root.title("送给豆豆宝贝")	# 这是把turtle.title()改为root.title()，表示窗口标题
    turtle.hideturtle()
    page0(turtle)				# 画第零页
    turtle.clear()				# 清除画布
    page1(turtle)				# 画第一页
    turtle.clear()				# 清除画布
    page2(turtle)				# 画第二页
    page3(turtle)				# 画第三页
    canva.mainloop()			# 这里把turtle.done()改为canva.mainloop()，表示窗口循环显示
```


## 七、最终功能
&emsp;**源码([_Love.py_](https://github.com/PinkLH/Love/blob/main/src/Love.py)):**
```python
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
    turtle.write('给我最爱的豆豆宝贝(❤ ω ❤)', font=('STCaiyun', 40, 'normal'))
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
    turtle.write('黎 宏                 杜运熙', font=('STCaiyun', 33, 'normal'))
    turtle.penup()
    turtle.goto(0, -180)
    draw_heart(10, turtle)
    arrow_heart(20, -60, 51, turtle)
    time.sleep(3)

# 第三页
def page3(turtle):
    turtle.penup()
    turtle.speed(10)
    turtle.goto(-300, 0)
    turtle.color('#00FFFF')
    turtle.write('爱 你 哟 ❤ ❤ ❤', font=('STCaiyun', 60, 'normal'))

# 作图主函数
def main(turtle):
    root.title("送给豆豆宝贝")
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
```
&emsp;**打包:**

&emsp;&emsp;用上面的方法打包，得到 **[_Love.exe_](https://github.com/PinkLH/Love/releases/download/Love_releases_v1.0.0/Love_releases_v1.0.0.exe)** 。

（最后说一句：希望你喜欢这个小程序😊，爱你哟，熙子😘😘😘）
