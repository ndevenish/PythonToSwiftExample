"""
This is a setup.py script to create a py2app plugin bundle

Usage:
    python setup.py py2app
"""

from setuptools import setup


APP = ['Bridge.py']
OPTIONS = {
  # Any local packages to include in the bundle should go here.
  # See the py2app documentation for more.
  "includes": [], 
}

setup(
    plugin=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=['pyobjc'],
)