# -*- coding: utf-8 -*-
"""Now Command
======

Command的实现类 - NOW命令类
"""


import time

from fx.engine.abcs import Command, Response


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
        
        fmt = ''
        args_fmts = list()
        args_keys = list()
        for a in args:
            if a[0] == '-':
                args_keys.append(a[1:])
            else:
                args_fmts.append(a)
        # 关键字参数会覆盖位置参数
        for k, v in kwargs.items():
            if k in ['f', 'fmt']:
                fmt = self.fmt_map.get(v, v)
            else:
                error.append(f"Unknown keyword argument: {k}")

        if not fmt:
            if any(args_keys):
                # 只有第一个正确的key生效
                final_key = 'T'
                for k in args_keys:
                    if k in self.fmt_map:
                        final_key = k
                        break
                fmt = self.fmt_map.get(final_key)
            else:
                args_fmt = []
                for i in ''.join(args_fmts):
                    if i == ' ':
                        continue
                    if i in 'yYmdHIMSaAbBcjpUwWxXZ%':
                        args_fmt.append(f"%{i}")
                    else:
                        error.append(f"Unknown argument: {i}")
            
                fmt = '-'.join(args_fmt)

        if not fmt:
            fmt = self.fmt_map.get('T')

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
    res = tc.execute(inp)
    # res = tc.execute(fmt=inp)
    print(res.code, res.message)

