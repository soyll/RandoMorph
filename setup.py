from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='RandoMorph',
  version='0.0.8',
  author='soyll',
  author_email='soyll@vk.com',
  description='A simple Python library for generating random data of various types, including strings, names, addresses, numbers, and more.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/soyll/RandoMorph',
  packages=find_packages(),
  install_requires=[
            'pandas~=2.1.1',
            'dataframe_image~=0.2.2',
            'openpyxl~=3.1.2',
  ],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='test python generate random randomorph',
  project_urls={
    'GitHub': 'https://github.com/soyll'
  },
  python_requires='>=3.6'
)