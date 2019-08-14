#!/usr/bin/env python

# Execute with
# $ python -m civ6_hooks_matrix

import sys

if __package__ is None and not hasattr(sys, 'frozen'):
    # direct call of __main__.py
    import os.path
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))


import civ6_hooks_matrix

if __name__ == '__main__':
    civ6_hooks_matrix.main()
