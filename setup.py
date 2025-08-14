from distutils.core import setup
import py2exe

setup(
    console=['cleanup_gpu.py'],  # Use 'windows' instead of 'console' for GUI apps
    options={
        'py2exe': {
            'includes': ['torch', 'gc'],
            'bundle_files': 1,  # Bundle everything into one .exe
            'compressed': True
        }
    },
    zipfile=None
)