#!/usr/bin/env python
# -*- encoding:utf-8 -*-
"""
codebox.manage
~~~~~~~~~~~~~~

:copyright: (c) 2011 DISQUS.
:license: Apache License 2.0, see LICENSE for more details.
"""
import os, os.path
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir))

from flaskext.actions import Manager

from codebox.app import create_app

app = create_app()
manager = Manager(app)

if __name__ == "__main__":
    manager.run()