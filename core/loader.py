# -*- coding: utf-8 -*-
"""Lazy Loader
======

Lazy Loader Class
"""


import importlib
from types import ModuleType
from typing import Optional

from fx.core.pattern import Singleton


class LazyLoader(Singleton):
    """Lazy Loader

    延迟加载器

    这是一个单例类
    """
    def __init__(self):
        self.__modules = {}

    def __import(self, name: str) -> dict:
        """线程安全的加载方法"""
        if name not in self.__modules:
            with self._lock:
                if name not in self.__modules:
                    module = None
                    e = ''
                    try:
                        module = importlib.import_module(name)
                    except ImportError as _e:
                        e = _e
                    self.__modules[name] = {
                        'module': module,
                        'e': e
                    }
        return self.__modules.get(name)

    def lazy_import(self, name: str) -> Optional[ModuleType]:
        """延迟加载方法"""
        _module = self.__import(name)
        if _module['e']:
            print(f"[Error] {_module['e']}")
        return _module['module']


loader = LazyLoader()

