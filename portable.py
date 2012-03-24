from distutils.core import setup
import py2exe
from glob import glob
import sys
import os
import msvcrt
sys.argv.append('py2exe')

setup(console=['HALcon.py'], data_files=[('data', glob('data/*.hal')+glob('data/*.chal'))],
      options={
        'py2exe': {'ascii': True, 'dist_dir': 'portable', 'optimize': 2,
                   'excludes': ['_ssl', 'unittest', 'doctest', 'difflib', 'inspect'],
                   },
      }
)

os.chdir('portable')
os.system('ren HALcon.exe HAL.exe')

open('python27.dll', 'wb').write(open('..\\python27.dll', 'rb').read())