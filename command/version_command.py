# -*- coding: utf-8 -*-
"""Version Command
======

VERSION命令的实现类
"""


from fx.command import Command
from fx.core.config import config
from fx.core.response import Response


class VersionCommand(Command):
    """Version Command

    VERSION命令的实现类

    fx的内置命令
    """
    def execute(self, *args, **kwargs) -> Response:
        conf = config.root()
        version = conf['meta']['version']
        codename = conf['meta']['codename']
        project_date = conf['meta']['project_date']
        response = Response()
        
        count = '1'
        for arg in args:
            if arg in ['more', '+']:
                count = '2'
        if 'count' in kwargs:
            count = str(kwargs.pop('count'))

        if count == '1':
            response.message = f"FX {version}"
        elif count.isdigit() and int(count) > 1:
            response.message = f"FX {version} [{codename} {project_date}]"
        else:
            response.code = 417
            response.message = f"Version: Invalid count: {count}"

        return response

