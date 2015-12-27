try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys
import os

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True
setup(name='MangaScrapper',
      version='0.0.1',
      install_requires=[
          r for r in open('requirements.txt', 'r').read().split('\n') if r],
      author='Rahul Zoldyck',
      author_email='rahulzoldyck@gmail.com',
      packages=['MangaScrapper', ],
      entry_points={
          'console_scripts': ['code2pdf=Code2pdf:main'],
      },
      license='GNU General Public License v3 (GPLv3)',
      url='https://github.com/RahulZoldyck/MangaScrapper/',
      description="Scraps the manga from mangafox.me using BeautifulSoup",
      long_description=open('README').read(),
      keywords=['manga', 'anime',
                'python', 'mangascrapper', 'BeautifulSoup'],
      classifiers=[
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: System :: Monitoring'
      ],
      )
