#!/usr/bin/env python

from distutils.core import setup

setup(name="escpos",
      version="1.0",
      author="Fivestars Inc.",
      author_email="dev@fivestarscard.com",
      description="Support for ESC/POS Thermic Printer",
      url="https://github.com/fivestars/python-escpos.git",
      packages=["escpos"],
      requires=[
          "pyusb (>= 1.0)",
          "PIL (>= 1.1.7)",
        ]
      )
