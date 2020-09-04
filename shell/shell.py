# -*- coding: utf-8 -*-
"""Shell
======

Shell的关键类
"""


# from fx.core.flag import flags as F
from fx.shell.parse import Parser
from fx.shell.parse import and_parser
from fx.shell.parse import command_parser
from fx.shell.parse import argument_parser


class Shell(Parser):
    """Main Shell Class

    这是Shell的关键类，其功能为交互式Shell

    这是一个单例类
    """
    def parse(self, expression: str) -> None:
        expressions = and_parser.parse(expression)
        for expression in expressions:
            command = command_parser.parse(expression)
            args, kwargs, error = argument_parser.parse(expression)
            if command is None:
                print("Invalid Command: "
                     f"{command_parser.name(expression)}")
                continue
            if error:
                for e in error:
                    print(f"Invalid Argument: {e}")
            response = command.execute(*args, **kwargs)
            print(response.message)

    def start(self):
        while True:
            expression = input("==> ")
            self.parse(expression)


# shell = Shell()

