"""Compile and install the syscallreplay C extension
"""
from distutils.core import setup, Extension


SYSCALLREPLAY_MOD = Extension('syscallreplay',
                              ['syscallreplay.c'],
                              extra_compile_args=['-Wall', '--std=c11'])

setup(name='syscallreplay',
      version='0.1',
      description='Replay a system call trace through an application',
      packages=['syscallreplay'],
      ext_modules=[SYSCALLREPLAY_MOD])
