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
    def root(self):
        config = json.load(open(CONF_PATH))
        return config

    def load(self, script: str) -> dict:
        script_path = os.path.join(
            ROOT_PATH,
            'scripts',
            script,
            'conf.json'
        )
        try:
            config = json.load(open(script_path))
        except Exception as e:
            print(e)
            config = {}
        return config


config = Config()

