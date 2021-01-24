# -*- coding: utf-8 -*-
"""Path
======

处理路径相关的模块
"""


import os
import sys

from fx import ROOT as root


abs = os.path.abspath
dir = os.path.dirname
cwd = os.getcwd
join = os.path.join
exists = os.path.exists


def crf():
    return sys.argv[0]


def cd():
    return os.path.dirname(sys.argv[0])


def fd(filename):
    return os.path.dirname(os.path.abspath(filename))


def mkdir(path, mode=511, dir_fd=None):
    if not os.path.exists(path):
        os.mkdir(path, mode, dir_fd)

