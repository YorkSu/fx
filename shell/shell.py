# -*- coding: utf-8 -*-
"""Shell
======

Shell的关键类
"""


from typing import Sequence

from fx.core.config import config
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

    def response(self, expression: str) -> Sequence[Response]:
        expressions = and_parser.parse(expression)
        responses = []
        for expression in expressions:
            command = command_parser.parse(expression)
            args, kwargs = argument_parser.parse(expression)
            if command is None:
                print("Invalid Command: "
                     f"{command_parser.name(expression)}")
                continue
            response = command.execute(*args, **kwargs)
            responses.append(response)
        return responses

    def parse(self, expression: str) -> None:
        responses = self.response(expression)
        for response in responses:
            if response.message:
                print(response.message)

    def start(self):
        print(self.hello)
        while True:
            expression = input("==> ")
            self.parse(expression)


# shell = Shell()

