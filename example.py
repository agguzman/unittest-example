# -*- coding: utf-8 -*-


import os


def rm(filename):
    if os.path.exists(filename):
        os.remove(filename)

