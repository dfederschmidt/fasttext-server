from distutils.core import setup
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

setup(name='fasttext-server',
      version='0.1',
      description='Deploy fasttext models',
      author='Daniel Federschmidt',
      author_email='daniel@federschmidt.xyz',
      url='https://federschmidt.xyz',
      packages=['ft_server', 'test']
      )
