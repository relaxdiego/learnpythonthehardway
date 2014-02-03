try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ex47',
    'author': 'Mark Maglana',
    'url': '',
    'download_url': '',
    'author_email': 'mmaglana@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'license': 'MIT',
    'packages': ['ex47', 'bin'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)