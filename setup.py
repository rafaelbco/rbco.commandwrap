from setuptools import setup, find_packages
import os

version = '0.0.2'

setup(name='rbco.commandwrap',
      version=version,
      description="Provide a set of decorators to make functions that run OS commands.",
      long_description='\n'.join([
        open('README.txt').read(), 
        open('TODO.txt').read(), 
        open('HISTORY.txt').read()
      ]),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='shell os command wrapper',
      author='Rafael Oliveira',
      author_email='rafaelbco@gmail.com',
      url='http://commandwrap.googlecode.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['rbco'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'pep362>=0.6.1,<0.7'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
