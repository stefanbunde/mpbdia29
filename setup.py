from setuptools import setup, find_packages

from mptbia2901 import __version__


setup(
    name='mptbia2901',
    version=__version__,

    author='Stefan Bunde',
    author_email='stefanbunde+git@posteo.de',

    packages=find_packages(),

    scripts=['bin/run_flask_app.sh'],

    install_requires=[
        'flask',
        'requests',
    ],
    extras_require={
        'uwsgi': [
            'uwsgi',
        ],
    },
)
