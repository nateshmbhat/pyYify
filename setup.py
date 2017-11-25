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

install_requires = ['bs4' , 'urllib3' ]
# if platform.system() == 'windows':
#     install_requires = [
#         'pypiwin32'
#     ]
# elif platform.system() == 'darwin':
#     install_requires = [
#         'pyobjc>=2.4'
#     ]


setup(
    name='pyYify',
    packages = ['pyYify'] ,
    version = 'v1.5',
    py_modules =['os' , 're', 'json' , 'urllib' , 'time' , 'requests'] , 
    description = '''
    This Module is used to get the Top seeded torrents at any given time and get the entire movie details and ratings . 
    Its also useful to search for any movie using different parameters and obtain their magnet link or torrent file of any prefered quality.
''' ,
    summary = 'Yify torrenter with movie searching and top seeded torrent finding features.'  ,
    author = 'Natesh M Bhat' ,
    license='MIT', 
    url = 'https://github.com/nateshmbhat/Yify-Python',
    author_email = 'nateshmbhatofficial@gmail.com' ,
    # download_url = 'https://github.com/nateshmbhat/pyttsx3/archive/v2.6.tar.gz',
    keywords=['yify','torrent-python' , 'movie-torrent' , 'torrent' , 'pyyify' , 'Yify' , 'yify torrent' , 'yify download' , 'download yify' , 'yifyer'  , 'yifypy' , 'torrent download' , 'movie torrent' , 'movie downloader', 'movie finder'],
    classifiers = [] ,
    install_requires=install_requires
)
