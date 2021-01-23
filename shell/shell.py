# -*- coding: utf-8 -*-
"""Shell
======

Shell的关键类
"""


from typing import Sequence

from fx.core.config import config
from fx.core.flag import flags as F
from fx.core.response import Response
from fx.shell.parse import Parser
from fx.shell.parse import and_parser
from fx.shell.parse import command_parser
from fx.shell.parse import argument_parser


class Shell(Parser):
    """Main Shell Class

    这是Shell的关键类，其功能为交互式Shell

    这是一个单例类
    """
    def __init__(self):
        conf = config.root()
        self.hello = conf['shell']['hello']

    def parse(self, expressions: str) -> None:
        expressions = and_parser.parse(expressions)
        for expression in expressions:
            command = command_parser.parse(expression)
            args, kwargs = argument_parser.parse(expression)
            if command is None:
                print("Invalid Command: "
                     f"{command_parser.name(expression)}")
                continue
            response = command.execute(*args, **kwargs)
            if response.code != 200:
                print(f"{command} Got Code: {response.code}")

    def start(self):
        F.exit = False
        print(self.hello)
        while not F.exit:
            expression = input("==> ")
            self.parse(expression)


# shell = Shell()

