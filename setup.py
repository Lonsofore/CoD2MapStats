from io import open
from setuptools import setup, find_packages
from os.path import join, dirname
from cod2mapstats import __version__


with open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()
    
with open('requirements.txt', encoding='utf-8') as f:
    requirements = f.read()


setup(
    # metadata
    name='cod2mapstats',
    version=__version__,
    url='https://github.com/lonsofore/cod2mapstats/',
    author='Lonsofore',
    author_email='lonsofore@yandex.ru',
    license='Apache 2.0',
    description='A lot of Call of Duty 2 statistics + program to use it.',
    long_description=readme,
    keywords='CoD2 Call of Duty 2 Python Statistics Maps',

    # options
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'cod2mapstats = cod2mapstats.start:start',
        ],
    },
)
