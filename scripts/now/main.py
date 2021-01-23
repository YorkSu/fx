# -*- coding: utf-8 -*-
"""Main

NOW 脚本的入口文件
"""


import time

from fx.command import Command
from fx.core.response import Response


class NowCommand(Command):
    """Now Command
    
    NOW 脚本的实现类
    """
    def __init__(self):
        self.fmt_map = {
            "D": "%Y-%m-%d",
            "date": "%Y-%m-%d",
            "T": "%Y-%m-%d %H:%M:%S",
            "time": "%Y-%m-%d %H:%M:%S",
        }

    def execute(self, *args, **kwargs) -> Response:
        response = Response()
        error = []
        args_fmt = []
        for i in ''.join(args):
            if i == ' ':
                continue
            if i in 'yYmdHIMSaAbBcjpUwWxXZ%':
                args_fmt.append(f"%{i}")
            else:
                error.append(f"Unknown argument: {i}")
        
        fmt = '-'.join(args_fmt) or "%Y-%m-%d %H:%M:%S"

        # 关键字参数会覆盖位置参数
        for k, v in kwargs.items():
            if k in ['fmt']:
                fmt = self.fmt_map.get(v, v)
            else:
                error.append(f"Unknown keyword argument: {k}")

        try:
            response.message = time.strftime(fmt, time.localtime(time.time()))
        except Exception as e:
            response.code = 417
            response.message = e  # 不合法的时间格式
        
        if response.code == 200 and error:
            response.code = 206

        for e in error:
            response.message += f'\n{e}'

        if response.message:
            print(response.message)

        return response


if __name__ == "__main__":
    tc = NowCommand()
    inp = input('==> ')
    # res = tc.execute(inp)
    res = tc.execute(fmt=inp)
    print(res.code, res.message)

