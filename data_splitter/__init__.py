"""
data-splitter - Split large datasets efficiently

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import DataSplitter, split, process, main

__all__ = ["DataSplitter", "split", "process", "main"]
