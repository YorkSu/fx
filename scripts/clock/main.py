# -*- coding: utf-8 -*-
"""Main

CLOCK 脚本的入口文件
"""


import os
import time

from fx.command import Command
from fx.core.response import Response


class ClockCommand(Command):
    """Clock Command
    
    CLOCK 脚本的实现类
    """
    MODE_MAP = {
        "S": "%Y-%m-%d %H:%M:%S",
        "M": "%Y-%m-%d %H:%M",
    }

    def execute(self, *args, **kwargs) -> Response:
        response = Response()
        mode = "S"
        is_cls = True
        mute = False
        error = []
        for a in args:
            if a.upper() in ['MUTE', '-M']:
                mute = True
            else:
                error.append(f"Unknown argument: {a}")
        for k, v in kwargs.items():
            if k.upper() in ['MODE']:
                mode = v
            elif k.upper() in ['CLS'] and v.upper() in ['FALSE', '0']:
                is_cls = False
            else:
                error.append(f"Unknown keyword argument {k}")
        fmt = self.MODE_MAP.get(mode, self.MODE_MAP['S'])

        if is_cls:
            os.system("cls")

        for e in error:
            print(e)

        try:
            while True:
                print(
                    '\r' + time.strftime(
                        fmt,
                        time.localtime(time.time())
                    ),
                    end='',
                    flush=True,
                )
                time.sleep(1)
        except KeyboardInterrupt:
            print('')
            if not mute:
                print('Got Ctrl-C')

        return response


if __name__ == "__main__":
    cc = ClockCommand()
    cc.execute()

