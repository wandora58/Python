try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='sample_package',
    version='1.0.0',
    packages=['package'],
    # if you could install setuptools
    # packages=find_packages()
    url='https://www.wandora58.com',
    license='Free',
    author='nakajima',
    author_email='',
    description='sample package'
)