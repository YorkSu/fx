# -*- coding: utf-8 -*-
"""Version Command
======

VERSION命令的实现类
"""


import os

from fx.command import Command
from fx.core.config import config
from fx.core.response import Response


class VersionCommand(Command):
    """Version Command

    VERSION命令的实现类

    fx的内置命令
    """
    ignores = [
        '.git',
        '.vscode',
    ]

    def execute(self, *args, **kwargs) -> Response:
        conf = config.root()
        version = conf['meta']['version']
        codename = conf['meta']['codename']
        project_date = conf['meta']['project_date']
        commits = conf['meta']['commits']
        # TODO: Automatically get the last modified date of the file
        latest = conf['meta']['latest']
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
            response.message += f" [{codename} {project_date}]"
            response.message += f" [Latest {latest}]"
        else:
            response.code = 417
            response.message = f"Version: Invalid count: {count}"

        if response.message:
            print(response.message)
        return response

