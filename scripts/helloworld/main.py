# -*- coding: utf-8 -*-
"""Main

Helloworld 脚本的入口文件
"""


from fx.command import Command
from fx.core.response import Response


class HelloworldCommand(Command):
    """Helloworld Command
    
    Helloworld脚本的实现类
    """
    def execute(self, *args, **kwargs) -> Response:
        response = Response()
        response.message = "Hello, World!"
        print(response.message)
        return response

