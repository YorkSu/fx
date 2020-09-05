# -*- coding: utf-8 -*-
"""Command
======

Command接口
"""


import abc


class Command(abc.ABC):
    """Command Interface
    
    命令接口
    """
    @abc.abstractmethod
    def execute(self, *args, **kwargs): ...

