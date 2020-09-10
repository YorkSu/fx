# -*- coding: utf-8 -*-
"""Exit Command
======

EXIT命令的实现类
"""


# import os

from fx.command import Command
from fx.core.flag import flags as F
from fx.core.response import Response


class ExitCommand(Command):
    """Exit Command

    EXIT命令的实现类

    fx的内置命令
    """
    def execute(self, *args, **kwargs) -> Response:
        F.exit = True
        return Response()

