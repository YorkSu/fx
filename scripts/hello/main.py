# -*- coding: utf-8 -*-
"""Hello
======

Command的实现类

Helloworld脚本
"""


from fx.engine.abcs import Command, Response


class Hello(Command):
    """Hello
    
    Helloworld脚本的实现类
    """
    def execute(self, *args, **kwargs) -> Response:
        response = Response()
        response.message = "Hello, World!"
        print(response.message)
        return response

