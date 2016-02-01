# -*- coding: utf-8 -*-
"""
FLask-EnvConfig

:copyright: (c) 2014 by Lars Hansson.
:license: BSD, see LICENSE for more details.
"""

from __future__ import absolute_import
import ast
from os import environ
import sys

DEFAULT_ENV_PREFIX = 'FLASK_'
PY2 = sys.version_info[0] == 2


class EnvConfig(object):
    """Configure Flask from environment variables."""

    def __init__(self, app=None, prefix=DEFAULT_ENV_PREFIX):
        self.app = app
        if app is not None:
            self.init_app(app, prefix)

    def init_app(self, app, prefix=DEFAULT_ENV_PREFIX):
        for key, value in iteritems(environ):
            if key.startswith(prefix):
                key = key[len(prefix):]
                try:
                    value = ast.literal_eval(value)
                except (ValueError, SyntaxError):
                    pass
                app.config[key] = value


def iteritems(d):
    if PY2:
        return d.iteritems()
    else:
        return d.items()
