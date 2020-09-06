# -*- coding: utf-8 -*-
"""Config
======

配置的管理类
"""


import os
import json

from fx import ROOT_PATH, CONF_PATH
from fx.core.pattern import Singleton


class Config(Singleton):
    """Config

    配置的管理类
    """
    ROOT_PATH = ROOT_PATH
    CONF_PATH = CONF_PATH

    def root(self):
        return json.load(open(CONF_PATH))

    def load(self, script: str) -> dict:
        script_path = os.path.join(
            ROOT_PATH,
            'scripts',
            script,
            'conf.json'
        )
        try:
            conf = json.load(open(script_path))
        except Exception as e:
            print(e)
            conf = {}
        return conf


config = Config()

