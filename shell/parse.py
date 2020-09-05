# -*- coding: utf-8 -*-
"""Parser
======

Parser接口及其部分实现类
"""


import abc
from typing import Sequence, Optional, Tuple

from fx.core.pattern import AbstractSingleton
from fx.command import Command
# from fx.command.command_enum import CommandEnum
from fx.command.command_enum import CommandEnumHandler


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
        command_enum = CommandEnumHandler.get_enum(command)
        if command_enum is None:
            return None
        return command_enum.value

    def name(self, expression: str) -> str:
        expression = expression.strip()
        command = expression.split(' ', 1)[0]
        return command.upper()


class ArgumentParser(Parser):
    """Argument Parser

    解析表达式中的位置参数和关键字参数
    
    这是一个单例类
    """
    def parse(self, expression: str) -> Tuple[list, dict, list]:
        expression = expression.strip()
        argument_e = expression.split(' ', 1)[-1]
        elements = argument_e.split(' ')
        # 移除空元素
        for i in ['', ' ']:
            if i in elements:
                elements.remove(i)

        args = []
        kwargs = {}
        error = []

        for element in elements:
            if '=' in element:  # 关键字参数
                kwarg = element.split('=')
                if len(kwarg) == 2:
                    kwargs[kwarg[0]] = kwarg[1]
                else:  # 两个或以上等号
                    error.append(element)
            else:  # 位置参数
                args.append(element)
        
        return args, kwargs, error


and_parser = AndParser()
command_parser = CommandParser()
argument_parser = ArgumentParser()


if __name__ == "__main__":
    response = CommandParser().parse("Version").execute(count=0)
    print(response.message)

