# -*- coding: utf-8 -*-
"""Main

KeepSSH 脚本的入口文件
"""


import os
import time

from fx.command import Command
from fx.core.config import config
from fx.core.response import Response
from fx.shell.shell import Shell


class KeepSSHCommand(Command):
    """KeepSSH Command
    
    KeepSSH脚本的实现类
    """
    RETRY = 0
    RETRY_TIMEOUT = 60
    SSH = config.load('keepssh').get('ssh', 'echo "no "config')

    def execute(self, *args, **kwargs) -> Response:
        response = Response()
        
        retry = int(kwargs.get('retry', self.RETRY))
        retry_timeout = int(kwargs.get('retry_timeout',
            self.RETRY_TIMEOUT))
        ssh = kwargs.get('ssh', self.SSH)

        for a in args:
            if a in ['-n']:
                retry = 1
        
        i = 0

        while not retry or i < retry:
            os.system(ssh)
            now = Shell().response("NOW")[0].message
            msg = [
               f"\n{now}"
                "\n连接中断",
               f", 将在{retry_timeout}秒后尝试重连",
                ", 停止脚本请按Ctrl-C\n"
            ]
            if retry:
                i += 1
                msg.append(f"重连次数: {i}/{retry}")
            print("".join(msg))
            try:
                time.sleep(retry_timeout)
            except KeyboardInterrupt:
                break

        response.message = "\n脚本终止"
        return response

