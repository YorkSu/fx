# -*- coding: utf-8 -*-
"""Config
======

Loader的实现类 - 配置加载类
"""


import json

from fx.engine.abcs import Loader
from fx.utils import path


class ConfigLoader(Loader):
    """Config Loader

    配置文件加载器
    
    这是一个单例类
    """
    @staticmethod
    def load(filepath) -> dict:
        output = dict()
        if path.exists(filepath):
            # output = json.load(open(filepath))
            try:
                output = json.load(open(filepath))
            except Exception:
                pass
        return output

    @staticmethod
    def load_root() -> dict:
        filepath = path.join(
            path.root,
            'settings.conf'
        )
        return ConfigLoader.load(filepath)
    
    @staticmethod
    def load_script(script) -> dict:
        filepath = path.join(
            path.root,
            'scripts',
            script,
            'settings.conf'
        )
        return ConfigLoader.load(filepath)


if __name__ == '__main__':
    print(ConfigLoader.load_root())

