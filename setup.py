"""
This is a setup.py script to create a py2app plugin bundle

Usage:
    python setup.py py2app
"""

from setuptools import setup


APP = ['Bridge.py']
OPTIONS = {
  "includes": ["bridge", "ocr"]
}

setup(
    plugin=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=['pyobjc'],
)