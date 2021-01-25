# -*- coding: utf-8 -*-
"""Command Loader
======

Loader的实现类 - 命令加载类
"""


from difflib import SequenceMatcher
from typing import Optional, Sequence

from fx.engine.abcs import Command, Loader
from fx.utils.config import ConfigLoader
from fx.utils.lazy_import import lazy_importer


class CommandLoader(Loader):
    """Command Loader

    命令加载类
    
    这是一个单例类
    """
    _members = dict()
    _imports = dict()
    _commands = dict()

    @staticmethod
    def _lazy_map() -> None:
        imports = dict()
        commands = dict()
        settings = ConfigLoader.load_root()

        # commands
        commands_d = settings['commands']
        for v in commands_d['list']:
            name = v['command']
            commands[name] = name
            for n in v['aliases']:
                commands[n] = name
            imports[name] = dict()
            imports[name]['imp'] = '.'.join([
                settings['meta']['name'],
                commands_d['location'],
                v['location']
            ])
            imports[name]['class_name'] = v['class_name']

        # scripts
        scripts_d = settings['scripts']
        for v in scripts_d['list']:
            name = v['command']
            if name in imports:
                print(f"[CommandLoader] The script's commands conflict with the built-in commands, '{name}'")
                continue
            commands[name] = name
            for n in v['aliases']:
                if n in commands:
                    print(f"[CommandLoader] The script's aliases conflict with the exists commands, '{name}', '{n}'")
                    continue
                commands[n] = name
            imports[name] = dict()
            imports[name]['imp'] = '.'.join([
                settings['meta']['name'],
                scripts_d['location'],
                v['location']
            ])
            imports[name]['class_name'] = v['class_name']
        
        CommandLoader._imports = imports
        CommandLoader._commands = commands

    @staticmethod
    def load(command) -> Optional[Command]:
        command = command.upper()
        command = CommandLoader._commands.get(command, '')
        if not command:
            return None
        if command not in CommandLoader._members:
            imps = CommandLoader._imports[command]
            _module = lazy_importer.load(imps['imp'])
            if _module is None:
                print(f"[CommandLoader] module failed to load, '{command}'")
                CommandLoader._members[command] = None
            else:
                CommandLoader._members[command] = getattr(
                    _module,
                    imps['class_name'],
                    None
                )
        return CommandLoader._members.get(command)

    @staticmethod
    def match(command) -> Sequence[str]:
        settings = ConfigLoader.load_root()
        threshold = settings['core']['like_threshold']
        outputs = list()
        for c in CommandLoader._commands:
            matcher = SequenceMatcher(None, command, c)
            ratio = matcher.quick_ratio()
            if ratio >= threshold:
                outputs.append(c)
        return outputs


CommandLoader._lazy_map()


if __name__ == '__main__':
    print(CommandLoader._imports)
    hello = CommandLoader.load('hello')
    print(hello)
    CommandLoader.load('hello')().execute()

