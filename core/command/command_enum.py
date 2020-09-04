# -*- coding: utf-8 -*-
"""Command Enum
======

Command枚举类
"""


from enum import Enum
from typing import Optional

from fx.core.command import Command
from fx.core.command.exit_command import ExitCommand
from fx.core.command.version_command import VersionCommand


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

