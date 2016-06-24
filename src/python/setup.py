# python setup.py py2exe => cd dist => malware.exe

from distutils.core import setup
import py2exe

setup(console=['malware.py'])
