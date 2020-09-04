# -*- coding: utf-8 -*-
"""Version Command
======

VERSION命令的实现类
"""


from fx import __version__, __codename__, __project_date__
from fx.core.command import Command
from fx.core.response import Response


class VersionCommand(Command):
    """Version Command

    VERSION命令的实现类

    fx的内置命令
    """
    def execute(self, *args, **kwargs) -> None:
        response = Response()
        count = 1
        for arg in args:
            if arg in ['more', '+']:
                count = 2
        if 'count' in kwargs:
            count = int(kwargs.pop('count'))
        
        if count < 1:
            response.message = f"Version: Invalid count: {count}"
        elif count == 1:
            response.message = f"FX {__version__}"
        else:
            response.message = f"FX {__version__}"\
                f" [{__codename__} {__project_date__}]"
        return response

