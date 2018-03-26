from distutils.core import setup

setup(name='fasttext-server',
      version='0.1.10',
      description='Deploy fasttext models',
      author='Daniel Federschmidt',
      author_email='daniel@federschmidt.xyz',
      url='https://federschmidt.xyz',
      packages=['ft_server', 'test'],
      install_requires=["click", "flask"],
      data_files=[("config.py", ["config.py"])]
      )
