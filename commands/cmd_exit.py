# -*- coding: utf-8 -*-
"""Exit Command
======

Command的实现类 - EXIT命令类
"""


from fx.engine.abcs import Command, Response
from fx.utils.flags import FLAGS


class ExitCommand(Command):
    """Exit Command

    EXIT命令的实现类

    fx的内置命令
    """
    def execute(self, *args, **kwargs) -> Response:
        FLAGS.core_running = False
        return Response()
    
