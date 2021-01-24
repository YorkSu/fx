# -*- coding: utf-8 -*-
"""Parser
======

Parser接口及其部分实现类
"""


import re
from typing import Sequence, Tuple

from fx.engine.abcs import Parser


class AndParser(Parser):
    """And Parser

    解析表达式中的 `&` 符号

    这是一个单例类
    """
    @staticmethod
    def parse(expression: str) -> Sequence[str]:
        expression = expression.strip()
        expressions = expression.split('&')
        return expressions


class CommandParser(Parser):
    """Command Parser
    
    解析表达式中的命令

    这是一个单例类
    """
    @staticmethod
    def parse(expression: str) -> str:
        expression = expression.strip()
        command = expression.split(' ', 1)[0]
        command = command.upper()
        return command


class ArgumentParser(Parser):
    """Argument Parser

    解析表达式中的位置参数和关键字参数
    
    这是一个单例类
    """
    @staticmethod
    def parse(expression: str) -> Tuple[list, dict]:
        expression = expression.strip()
        expressions = expression.split(' ', 1)
        if len(expressions) <= 1:
            return [], {}
        
        argument = expressions[-1]
        strings = re.findall(r'\S*=\"[^\"]+\"|\"[^\"]+\"', argument)  # match `key="xxx"` or `"xxx"`
        for string in strings:
            argument = argument.replace(string, '')
        argv = argument.split(' ') + strings

        args = []
        args_key = []
        kwargs = {}

        for item in argv:
            if not item:
                continue
            if '=' in item:
                element = item.split('=', 1)
                if not all(element):
                    continue
                k = element[0]
                v = re.sub(r'\"', '', element[1])
                kwargs[k] = v
            elif item[0] == '-':
                args_key.append(re.sub(r'\"', '', item))
            else:
                args.append(re.sub(r'\"', '', item))

        return args + args_key, kwargs

