# -*- coding: utf-8 -*-
"""Echo Command
======

Command的实现类 - ECHO命令类
"""


from fx.engine.abcs import Command, Response


class EchoCommand(Command):
    """Echo Command

    ECHO命令的实现类

    fx的内置命令
    """
    def execute(self, *args, **kwargs) -> Response:
        response = Response()
        response.message = "\n".join(args)
        print(response.message)
        return response 

