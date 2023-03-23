"""
Author: Xsarz

Enjoy using!
"""

from .utils import exceptions, headers, objects, requester
from .client import Client


from os import system as s
__title__ = 'stationhead'
__author__ = 'Xsarz'
__license__ = 'MIT'
__copyright__ = 'Copyright 2023 Xsarz'
__version__ = '1.0'


__newest__ = "1.0"
if __version__ != __newest__:
	s('cls || clear')
	print(f'\033[38;5;214m{__title__} made by {__author__}\nPlease update the library. Your version: {__version__}  A new version:{__newest__}\033[0m')