try: 
    from setuptools import setup
except ImportError:
    from distutiles.core import setup

config = {
    'description': 'this is a test file of learnig Python ex51',
    'author': 'Arnold YANG',
    'url': 'N/A',
    'download_url': 'N/a',
    'author_email': 'arnoldyd@gmail.com',
    'version': '1.0',
    'install_requires': ['nose','web'],
    'packages': ['NAME'],
    'scripts': []
    'name': 'ex51_exercise'   
}

setup(**config)