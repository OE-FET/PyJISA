from setuptools import setup

setup(
    name='pyjisa',
    version='1.0',
    description='JISA Python wrapper',
    url='https://github.com/OE-FET/PyJISA.git',
    author='William Wood',
    author_email='waw31@cam.ac.uk',
    license='unlicense',
    packages=['pyjisa'],
    install_requires=['jpype1','install-jdk'],
    include_package_data=True,
    zip_safe=False
)
