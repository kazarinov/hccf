# -*- coding: utf-8 -*-

import sys
import logging

from .utils.logs import load_dict_config


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': logging.DEBUG,
        'handlers': ['console', 'app_file'],
    },
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(process)d/%(thread)d %(levelname)s %(name)s %(filename)s:%(lineno)s %(message)s',
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': logging.DEBUG,
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            "stream": sys.stdout
        },
        "app_file": {
            'level': logging.DEBUG,
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': 'ctr.log',
        },
    },
    'loggers': {
        'app': {
            'level': logging.DEBUG,
            'handlers': ['app_file'],
            'propagate': False
        }
    }
}
