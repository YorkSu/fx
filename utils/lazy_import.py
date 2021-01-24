# -*- coding: utf-8 -*-
"""Lazy Importer
======

Loader的实现类 - 模块延迟加载类
"""


import importlib
from types import ModuleType
from typing import Optional

from fx.engine.abcs import Loader


class LazyImporter(Loader):
    """Lazy Importer

    模块延迟加载器

    这是一个单例类
    """
    _modules = dict()

    def __import(self, name: str) -> dict:
        if name not in self._modules:
            with self._lock:
                if name not in self._modules:
                    module = None
                    e = ''
                    try:
                        module = importlib.import_module(name)
                    except ImportError as e:
                        print(e)
                    self._modules[name] = {
                        'module': module,
                        'e': e
                    }
        return self._modules.get(name)

    def load(self, name: str) -> Optional[ModuleType]:
        _module = self.__import(name)
        if _module['e']:
            print(f"[LazyImporter] {_module['e']}")
        return _module['module']


lazy_importer = LazyImporter()

