# -*- coding: utf-8 -*-
"""Command Enum
======

Command枚举类
"""


from typing import Optional, Callable

from fx.command import Command
from fx.command.exit_command import ExitCommand
from fx.command.version_command import VersionCommand
from fx.core.config import config
from fx.core.pattern import Singleton
from fx.core.loader import loader


class CommandEnum(Singleton):
    """Command Enum

    命令的枚举类

    这是一个单例类
    """
    def __init__(self):
        self._members = {
            "EXIT": ExitCommand,
            "VERSION": VersionCommand,
        }
        conf = config.root()
        scripts = conf.get('scripts')
        for _, v in scripts.items():
            imp_name = '.'.join([
                conf.get('meta').get('name'),
                'scripts',
                v.get('location'),
                v.get('entrance'),
            ])
            script_load_function = self.script(
                imp_name,
                v.get('class_name'),
            )
            self._members[v.get('command')] = script_load_function

    @property
    def members(self):
        return self._members

    def script(self,
            name: str,
            cls_name: str,
            default=None
        ) -> Callable:
        def module() -> Optional[Command]:
            _module = loader.lazy_import(name)
            if _module is None:
                return None
            return getattr(_module, cls_name, default)()
        return module

    def contains(self, expression: str) -> bool:
        return expression in self._members
    
    def get(self, expression: str) -> Optional[Command]:
        pre_output = self._members.get(expression, None)
        if callable(pre_output):
            pre_output = pre_output()
        return pre_output


command_enum = CommandEnum()


if __name__ == "__main__":
    pass
    # print(command_enum.members)
    # print(command_enum.get("TIME"))
    # print(command_enum.get("TIME"))

    # c = command_enum.script('fx.scripts.time_.main', 'TimeCommand')()
    # print(c)
    # import fx.scripts.time_.main as m

    # cmd = getattr(m, 'TimeCommand', None)
    # print(cmd)

