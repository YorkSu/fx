# -*- coding: utf-8 -*-
"""Clock
======

Command的实现类

Clock脚本
"""


import os
import time

from fx.engine.abcs import Command, Response


class Clock(Command):
    """Clock
    
    Clock脚本的实现类
    """
    modes = {
        "S": "%Y-%m-%d %H:%M:%S",
        "M": "%Y-%m-%d %H:%M",
    }

    def execute(self, *args, **kwargs) -> Response:
        mode = 'S'
        is_cls = False
        mute = False
        error = []
        
        for a in args:
            if a.upper() in ['MUTE', '-M']:
                mute = True
            elif a.upper() in ['CLS', '-C']:
                is_cls = True
            else:
                error.append(f"Unknown argument: {a}")
        
        for k, v in kwargs.items():
            if k.upper() in ['MODE']:
                mode = v
            else:
                error.append(f"Unknown keyword argument {k}")
        fmt = Clock.modes.get(mode, Clock.modes['S'])

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
                print('Clock停止')

        return Response()

