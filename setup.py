'''MIT License

Copyright (c) 2017 nateshmbhat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import platform
from setuptools import setup

install_requires = ['bs4' , 'urllib3', 'urllib'  , 'requests']

with open("README.rst"  ,"r") as f:
    long_description = f.read() ; 
    long_description.replace('\r' ,'') ;

setup(
    name='pyYify',
    packages = ['pyYify'] ,
    version = 'v1.9.0',
    py_modules =['os' , 're', 'json' , 'urllib' , 'time' , 'requests'] , 
    description = 'This Module is used to get the Top seeded torrents at any given time and get the entire movie details and ratings . Its also useful to search for any movie using different parameters and obtain their magnet link or torrent file of any prefered quality.'
     ,
    long_description =  long_description , 
    summary = 'Yify torrenter with movie searching and top seeded torrent finding features.'  ,
    author = 'Natesh M Bhat' ,
    license='MIT', 
    url = 'https://github.com/nateshmbhat/pyYify',
    author_email = 'nateshmbhatofficial@gmail.com' ,
    keywords=['yify','torrent-python' , 'movie-torrent' , 'torrent' , 'pyyify' , 'Yify' , 'yify torrent' , 'yify download' , 'download yify' , 'yifyer'  , 'yifypy' , 'torrent download' , 'movie torrent' , 'movie downloader', 'movie finder'],
    classifiers = [ 
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Intended Audience :: System Administrators',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'License :: OSI Approved :: MIT License' , 
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7'
    ] ,
    install_requires=install_requires
)
