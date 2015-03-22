from setuptools import setup, find_packages
import sys, os

version = '1.0a17'

setup(name='pycurrency',
      version=version,
      description="A currency converter that uses google.com/ig/calculator",
      long_description="""\
                   get full documentation at http://pycurrency.rtfd.org
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='currency converter google api',
      author='David Bain',
      author_email='pigeonflight@gmail.com',
      url='http://pigeonflight.blogspot.com',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
