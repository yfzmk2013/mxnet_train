#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import termios
import os

def press_any_key_exit(msg):
    # 获取标准输入的描述符
    fd = sys.stdin.fileno()

    # 获取标准输入(终端)的设置
    old_ttyinfo = termios.tcgetattr(fd)

    # 配置终端
    new_ttyinfo = old_ttyinfo[:]

    # 使用非规范模式(索引3是c_lflag 也就是本地模式)
    new_ttyinfo[3] &= ~termios.ICANON
    # 关闭回显(输入不会被显示)
    new_ttyinfo[3] &= ~termios.ECHO

    # 输出信息
    sys.stdout.write(msg+'\n')
    sys.stdout.flush()
    # 使设置生效
    termios.tcsetattr(fd, termios.TCSANOW, new_ttyinfo)
    # 从终端读取
    os.read(fd, 7)
    #print fd

    # 还原终端设置
    termios.tcsetattr(fd, termios.TCSANOW, old_ttyinfo)

    exit(-1)

def press_any_key_pause(msg):
    # 获取标准输入的描述符
    fd = sys.stdin.fileno()

    # 获取标准输入(终端)的设置
    old_ttyinfo = termios.tcgetattr(fd)

    # 配置终端
    new_ttyinfo = old_ttyinfo[:]

    # 使用非规范模式(索引3是c_lflag 也就是本地模式)
    new_ttyinfo[3] &= ~termios.ICANON
    # 关闭回显(输入不会被显示)
    new_ttyinfo[3] &= ~termios.ECHO

    # 输出信息
    sys.stdout.write(msg+'\n')
    sys.stdout.flush()
    # 使设置生效
    termios.tcsetattr(fd, termios.TCSANOW, new_ttyinfo)
    # 从终端读取
    os.read(fd, 7)
    #print fd

    # 还原终端设置
    termios.tcsetattr(fd, termios.TCSANOW, old_ttyinfo)

def getfilefromMode(srcDirPath, fileMode):
    L = []
    for dirpath, dirnames, filenames in os.walk(srcDirPath):
        # print dirpath
        for file in filenames:
            if os.path.splitext(file)[1] == fileMode:
                L.append(os.path.join(dirpath, file))
    return L