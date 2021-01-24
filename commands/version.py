# -*- coding: utf-8 -*-
"""Version Command
======

Command的实现类 - VERSION命令类
"""


import time

from fx.engine.abcs import Command, Response
from fx.utils.config import ConfigLoader


class VersionCommand(Command):
    """Version Command

    VERSION命令的实现类

    fx的内置命令
    """
    def execute(self, *args, **kwargs) -> Response:
        conf = ConfigLoader.load_root()
        version = conf['meta']['version']
        codename = conf['meta']['codename']
        date = conf['meta']['date']
        commits = conf['meta']['commits']
        # TODO: Automatically get the last modified date of the file
        latest = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        # latest = conf['meta']['latest']
        response = Response()
        
        count = '1'
        for arg in args:
            if arg in ['more', '+']:
                count = '2'

        count = str(kwargs.get('count', count))

        if count == '1':
            response.message = f"FX {version}-{commits}"
        elif count.isdigit() and int(count) > 1:
            response.message = f"FX {version}-{commits}"
            response.message += f" [{codename} {date}]"
            response.message += f" [Latest {latest}]"
        else:
            response.code = 417
            response.message = f"Version: Invalid count: {count}"

        if response.message:
            print(response.message)
        return response
    
