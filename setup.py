from setuptools import setup, find_packages

setup(name='Kronos',
      version='0.1',
      description='DSL tool for scheduled tasking',
      url='https://github.com/MilosSimic/Kronos',
      author='Milos Simic',
      author_email='milossimicsimo@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data= True,
      zip_safe=False,
      package_data = {
      	'':['*.tx']
      }
)