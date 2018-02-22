'''
Created on 22 Feb 2018

@author: Anna
'''
from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for COMP30670",
      author="Anna Ryzova",
      author_email="anna.ryzova@ucdconnect.ie",
      license="GPL3",
      packages=['systeminfo'],
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
          }
 )