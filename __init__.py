# -*- coding: utf-8 -*-
"""FX
======

useful python scripts
"""


__author__ = "York Su"
__version__ = "0.1.0"


import os as _os

ROOT_PATH = _os.path.dirname(_os.path.abspath(__file__))
CONF_PATH = _os.path.join(ROOT_PATH, 'conf.json')

del _os

