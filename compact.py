from distutils.core import setup
import py2exe
from glob import glob
import sys
import os
import msvcrt
sys.argv.append('py2exe')

setup(console=['compact_entry.py'], data_files=[('data', glob('data/*.hal')+glob('data/*.chal')), ('espeak', glob('espeak/*'))],
      options={
        'py2exe': {'ascii': False, 'dist_dir': 'compact', 'optimize': 2,
                   'excludes': ['_ssl', 'unittest', 'doctest', 'inspect'],
                   },
      }
)

os.chdir('compact')
os.system('ren compact_entry.exe HAL.exe')

open('python27.dll', 'wb').write(open('..\\python27.dll', 'rb').read())
