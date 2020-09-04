# -*- coding: utf-8 -*-
"""Exit Command
======

EXIT命令的实现类
"""


import os

from fx.core.command import Command


class ExitCommand(Command):
    """Exit Command

    EXIT命令的实现类

    fx的内置命令
    """
    def execute(self, *args, **kwargs) -> None:
        os._exit(0)

