try: 
    from setuptools import setup
except ImportError:
    from distutiles.core import setup

config = {
    'description': 'final test of leraning python',
    'author': 'Arnold YANG',
    'url': 'N/A',
    'download_url': 'N/a',
    'author_email': 'arnoldyd@gmail.com',
    'version': '1.0',
    'install_requires': ['nose','web'],
    'packages': ['gothonweb'],
    'scripts': []
    'name': 'gothonweb'   
}

setup(**config)