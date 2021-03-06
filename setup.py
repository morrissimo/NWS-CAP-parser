from distutils.core import setup
import glob

setup(name='nwscapparser',
      version='1.0.2',
      description='NWS CAP Parser',
      author='Robert Morris (morrissimo)',
      author_email='robert@emthree.com',
      url='https://github.com/morrissimo/NWS-CAP-parser/',
      packages=['nwscapparser'],
      data_files=[('',glob.glob('*.xml')),
        ('',['demo.py','readme.md','LICENSE'])]
     )