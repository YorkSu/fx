# -*- coding: utf-8 -*-
"""Abstract Classes
======

各种抽象类和接口，以及部分工具类
"""


# pylint: disable=multiple-statements

import abc
import threading
from typing import Any, Optional


class SingletonMetaclass(type):
    """Metaclass for defining Singleton Classes

    Use this metaclass to create a Singleton Class.

    Usage:
    ```python
    class Singleton(metaclass=SingletonMetaclass): ...
    ```
    """
    __instance_lock = threading.RLock()
    __instance = None
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__instance_lock:
                if cls.__instance is None:
                    cls.__instance = super(SingletonMetaclass, cls).\
                        __call__(*args, **kwargs)
        return cls.__instance


class AbstractSingletonMetaclass(abc.ABCMeta, SingletonMetaclass):
    """Abstract Singleton Metaclass

    Use this metaclass to create a Abstract Singleton Class.
    """


class Singleton(metaclass=SingletonMetaclass):
    """Parent Class for a Singleton

    Inherit this class to Create a Singleton Class

    SubClasses SHALL NOTE `This is a Singleton Class`
    """
    _lock = threading.RLock()


class AbstractSingleton(metaclass=AbstractSingletonMetaclass):
    """Abstract Singleton Class

    Inherit this class to Create a Abstract Singleton Class

    SubClasses SHALL NOTE `This is an Abstract Singleton Class`
    """
    _lock = threading.RLock()


class Command(abc.ABC):
    """Command Interface
    
    命令接口
    """
    @abc.abstractmethod
    def execute(self, *args, **kwargs): ...


class Loader(AbstractSingleton):
    """Loader Interface

    Loader接口

    这是一个抽象单例类    
    """
    @abc.abstractmethod
    def load(self, name: str): ...


class Parser(AbstractSingleton):
    """Parser Interface

    Parser接口

    这是一个抽象单例类    
    """
    @abc.abstractmethod
    def parse(self, expression: str): ...


class POJO:
    def __getattribute__(self, key: str, default=None) -> Optional[Any]:
        try:
            output = super().__getattribute__(key)
        except AttributeError:
            output = default
        return output
    
    def get(self, key: str, default=None) -> Optional[Any]:
        """Get value from specified key
        
        if not found, return default
        """
        return self.__getattribute__(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set the value of specified key"""
        self.__setattr__(key, value)


# 实例类


class Response(POJO):
    def __init__(self):
        self.code = 200
        self.message = ''

    def keys(self):
        """Get the list of argument keys"""
        return list(self.__dict__.keys())

    def dict(self):
        return self.__dict__

