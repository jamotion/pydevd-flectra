from setuptools import setup, find_packages

setup(
    name='pydevd-flectra',
    version='1.1',
    description='PyDev.Debugger plugin for Flectra',
    url='https://github.com/jamotion/pydevd-flectra',
    author='Jamotion',
    author_email='info@jamotion.ch',
    packages=find_packages(),
    namespace_packages=['pydevd_plugins.extensions'],
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
