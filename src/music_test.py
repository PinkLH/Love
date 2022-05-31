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
