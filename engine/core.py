# -*- coding: utf-8 -*-
"""Core
======

Parser的实现类 - 内核类
"""


from fx.engine.abcs import Parser
from fx.engine.command_loader import CommandLoader
from fx.engine.parsers import (
    AndParser,
    CommandParser,
    ArgumentParser
)
from fx.utils.config import ConfigLoader
from fx.utils.flags import FLAGS


class Core(Parser):
    """Core

    FX交互的内核

    这是一个单例类
    """
    def __init__(self):
        self._settings = ConfigLoader.load_root()
        self._hello = self._settings['core']['hello']
        self._enter_flag = self._settings['core']['enter_flag']

    def parse(self, expressions: str) -> None:
        expressions = AndParser.parse(expressions)
        for expression in expressions:
            command = CommandParser.parse(expression)
            args, kwargs = ArgumentParser.parse(expression)
            if not command:
                continue
            command_class = CommandLoader.load(command)
            if command_class is None:
                print(f"[Core] Invalid Command, '{command}'")
                continue
            response = command_class().execute(*args, **kwargs)
            if response.code != 200:
                ...
            if not FLAGS.core_running:
                break

    def start(self) -> None:
        FLAGS.core_running = True
        if self._hello:
            print(self._hello)
        while FLAGS.core_running:
            expression = input(self._enter_flag)
            self.parse(expression)


if __name__ == '__main__':
    Core().start()

