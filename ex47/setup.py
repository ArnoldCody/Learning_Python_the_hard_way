try: 
    from setuptools import setup
except ImportError:
    from distutiles.core import setup

config = {
    'description': 'My Project',
    'author': 'Arnold YANG',
    'url': 'URL to get it al.',
    'download_url': 'Where to download it.',
    'author_email': 'arnoldyd@gmail.com',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': []
    'name': 'projectname'   
}

setup(**config)