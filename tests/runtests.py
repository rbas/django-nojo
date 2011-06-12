#!/usr/bin/env python
# coding: utf-8

import sys
sys.path.append('..')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.test.simple import run_tests

if __name__ == "__main__":
    failures = run_tests(['nojo',], verbosity=1)
    if failures:
        sys.exit(failures)
