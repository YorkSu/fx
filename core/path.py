# -*- coding: utf-8 -*-
"""Path
======

Path Handler
"""


import os
import sys

from fx.core.pattern import Singleton


class Path(Singleton):
    """Path Manager Class

    This is a Singleton Class
    """
    def abs(self, path):
        """os.path.abspath"""
        return os.path.abspath(path)

    def cd(self):
        """Get Current Directory"""
        return os.path.dirname(self.crf())

    def crf(self):
        """Get Current Running File path"""
        return sys.argv[0]

    def dirname(self, path):
        """os.path.dirname"""
        return os.path.dirname(path)

    def fd(self, filename):
        """Get File Directory

        Args:
            filename: Str. filename of the file
                `__file__` is Recommended
        """
        return os.path.dirname(os.path.abspath(filename))

    def rd(self):
        """Get Running Directory"""
        return os.getcwd()

    def join(self, path, *paths):
        """os.path.join"""
        return os.path.join(path, *paths)

    def exists(self, path):
        """os.path.exists"""
        return os.path.exists(path)

    def mkdir(self, path, mode=511, dir_fd=None):
        """os.mkdir"""
        if not self.exists(path):
            with self._lock:
                if not self.exists(path):
                    os.mkdir(path, mode, dir_fd)


path = Path()

