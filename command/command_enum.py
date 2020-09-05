# -*- coding: utf-8 -*-
"""Command Enum
======

Command枚举类
"""


from enum import Enum
from typing import Optional

from fx.command import Command
from fx.command.exit_command import ExitCommand
from fx.command.version_command import VersionCommand
from fx.core.config import config


class CommandEnum(Enum):
    """Command Enum

    这是一个枚举类，包含命令的枚举
    """
    EXIT = ExitCommand()
    VERSION = VersionCommand()

    @classmethod
    def contains(cls, expression: str) -> bool:
        return expression in cls.__members__.keys()

    @classmethod
    def get(cls, expression: str) -> Optional[Command]:
        target = cls.__members__.get(expression, None)
        if target is None:
            return target
        return target.value


class CommandEnumHandler:
    def __init__(self):
        conf = config.root()
        scripts = conf.get('scripts')
        for script in scripts:
            pass

    @classmethod
    def contains(cls, expression: str) -> bool:
        return expression in CommandEnum.__members__.keys()

    @classmethod
    def get_enum(cls, expression: str) -> Enum:
        target = CommandEnum.__members__.get(expression, None)
        return target

