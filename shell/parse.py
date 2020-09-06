# -*- coding: utf-8 -*-
"""Parser
======

Parser接口及其部分实现类
"""


import abc
import argparse
import re
from typing import Sequence, Optional, Tuple

from fx.core.pattern import AbstractSingleton
from fx.command import Command
from fx.command.command_enum import command_enum


class Parser(AbstractSingleton):
    """Parser Interface

    Parser接口

    这是一个抽象单例类    
    """
    @abc.abstractmethod
    def parse(self, expression: str): ...


class AndParser(Parser):
    """And Parser

    解析表达式中的 `&` 符号

    这是一个单例类
    """
    def parse(self, expression: str) -> Sequence[str]:
        expression = expression.strip()
        expressions = expression.split('&')
        return expressions


class CommandParser(Parser):
    """Command Parser
    
    解析表达式中的命令

    这是一个单例类
    """
    def parse(self, expression: str) -> Optional[Command]:
        expression = expression.strip()
        command = expression.split(' ', 1)[0]
        command = command.upper()
        return command_enum.get(command)

    def name(self, expression: str) -> str:
        expression = expression.strip()
        command = expression.split(' ', 1)[0]
        return command.upper()


class ArgumentParser(Parser):
    """Argument Parser

    解析表达式中的位置参数和关键字参数
    
    这是一个单例类
    """
    def __init__(self):
        self.parser = argparse.ArgumentParser()


    def parse(self, expression: str) -> Tuple[list, dict]:
        expression = expression.strip()
        expressions = expression.split(' ', 1)
        if len(expressions) == 1:
            return [], {}
        argument = expressions[-1]
        argv = re.findall(r'[\w=]*\"[^\"]+\"|[\w=]+', argument)

        args = []
        kwargs = {}

        for item in argv:
            if '=' in item:
                element = item.split('=', 1)
                k = element[0]
                v = re.sub(r'\"', '', element[1])
                kwargs[k] = v
            else:
                args.append(re.sub(r'\"', '', item))

        return args, kwargs


and_parser = AndParser()
command_parser = CommandParser()
argument_parser = ArgumentParser()


if __name__ == "__main__":
    response = CommandParser().parse("Version").execute(count=0)
    print(response.message)

