# -*- coding: utf-8 -*-
"""Flag
======

Global Argument Manager
"""


from typing import Any, Optional

from fx.core.pattern import Singleton


class Flags(Singleton):
    """Global Argument Manager
    
    This is a Singleton Class
    """
    def __setattr__(self, key: str, value: Any) -> None:
        super(Flags, self).__setattr__(key, value)

    def __getattribute__(self, key: str, default=None) -> Optional[Any]:
        try:
            output = super(Flags, self).__getattribute__(key)
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


flags = Flags()

