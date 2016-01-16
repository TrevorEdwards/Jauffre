try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Jauffre',
    'author': 'Trevor Edwards, Jerry Jia, Elizabeth Yam',
    'url': 'TODO',
    'download_url': 'TODO',
    'author_email': 'tre23@cornell.edu',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': [
        'jauffre',
        'pyttsx'
    ],
    'scripts': [],
    'name': 'jauffre'
}

setup(**config)
