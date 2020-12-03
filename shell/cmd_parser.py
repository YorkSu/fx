# -*- coding: utf-8 -*-
"""Parser
======

Parser接口及其部分实现类
"""


import argparse
import os

from fx.core.flag import flags as F
from fx.shell.parse import Parser
from fx.shell.shell import Shell


class CmdParser(Parser):
    """Command-Line Parser

    解析命令行输入
    
    这是一个单例类
    """
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter,
            add_help=False,
        )
        self.group = self.parser.add_mutually_exclusive_group()
        self.parser.add_argument(
            "-h",
            "--help",
            action="help",
            help="打印帮助信息并退出",
        )
        self.parser.add_argument(
            'expression',
            nargs="*",
            help="表达式",
        )
        self.group.add_argument(
            '-c',
            '--clean',
            action='count',
            help="启动FX的同时清空打印台",
        )
        self.group.add_argument(
            '-V',
            '--version',
            action="count",
            help="输出版本号并退出\n"
                 "如果输入两次则打印更多信息",
        )
        self.parser.add_argument(
            '-y',
            '--yes',
            action='store_true',
            help="当需要输入[y/n]时，默认输入y",
        )
        self.args = self.parser.parse_args()

    def parse(self) -> None:
        """解析接收到的命令行输入"""
        F.set("expression", ' '.join(self.args.expression))
        F.set("yes", self.args.yes)
        F.set("clean", self.args.clean)
        if self.args.clean:
            os.system("cls")
        if F.expression:
            Shell().parse(F.expression)
        elif self.args.version:
            Shell().parse(f"VERSION count={self.args.version} & EXIT")
        else:
            Shell().start()
        if isinstance(self.args.clean, int) and self.args.clean > 1:
            os.system("cls")

