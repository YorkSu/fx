# -*- coding: utf-8 -*-
"""Help Command
======

Command的实现类 - HELP命令类
"""


from fx.engine.abcs import Command, Response
from fx.utils.config import ConfigLoader


class HelpCommand(Command):
    """Help Command

    HELP命令的实现类

    fx的内置命令
    """
    def execute(self, *args, **kwargs) -> Response:
        response = Response()
        settings = ConfigLoader.load_root()
        commands = dict()
        scripts = dict()
        
        commands_d = settings['commands']
        for v in commands_d['list']:
            commands[v['command']] = v['aliases']

        scripts_d = settings['scripts']
        for v in scripts_d['list']:
            scripts[v['command']] = v['aliases']

        response.message = "Available Command: "
        for command in commands:
            response.message += "\n- " + command
            aliases = commands[command]
            if aliases:
                response.message += ' ['
                response.message += ', '.join(aliases)
                response.message += ']'
                
        response.message += "\nAvailable Script: "
        for script in scripts:
            response.message += "\n- " + script
            aliases = scripts[script]
            if aliases:
                response.message += ' ['
                response.message += ', '.join(aliases)
                response.message += ']'

        print(response.message)
        return response 

