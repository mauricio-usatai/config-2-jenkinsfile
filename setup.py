from setuptools import setup, find_packages

setup(
	name = 'config-2-jenkinsfile',
	version = '1.0.0',  
  entry_points = {
      'console_scripts': [
          'config-2-jenkinsfile=config_2_jenkinsfile.main:main',
      ]
  },
  packages = find_packages(),
)