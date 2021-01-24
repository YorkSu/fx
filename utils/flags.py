# -*- coding: utf-8 -*-
"""Flag
======

全局变量管理类
"""


from fx.engine.abcs import Singleton, POJO


class Flags(Singleton, POJO):
    """Flags

    管理全局变量的类

    这是一个单例类
    """
    ...


FLAGS = Flags()

