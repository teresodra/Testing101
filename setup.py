try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages
    
setup(
    name="compare_lists",
    version="0.1",
    packages=find_packages(),
    install_requires=[]
)
