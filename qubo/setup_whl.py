from setuptools import setup, find_packages, Extension, dist
import sys

name = 'thesis_'
version = '0.01'

#https://stackoverflow.com/questions/35112511/pip-setup-py-bdist-wheel-no-longer-builds-forced-non-pure-wheels
class BinaryDistribution(dist.Distribution):
    def has_ext_modules(self):
        return True

    
if 'linux' in sys.platform :
    package_data = {'qubo.cpu' : ['*.so', 'qubo/cpu/*.so' ], 'qubo.cuda' : ['*.so', 'qubo/cuda/*.so' ] }
else :    
    package_data = {'qubo.cpu' : ['*.pyd', 'qubo/cpu/*.pyd' ], 'qubo.cuda' : ['*.pyd', 'qubo/cuda/*.pyd' ] }
    

pyver= [
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
]

email = '075mscsk013.pradip@pcampus.edu.np'
author='Pradip Bhandari'


classifiers=[
    'Operating System :: POSIX :: Linux'
]

classifiers = classifiers + pyver

with open('README.rst') as file:
    long_description = file.read()


setup(
    name=name,
    author=author,
    author_email=email,
    packages=find_packages(exclude=['tests']),
    install_requires=['numpy>=1.11'],
    keywords='Optimizing Budget pacing for Effective Online Ad Campaign using Quantum Accelerator models, GPU, CUDA',
    classifiers=classifiers,
    package_data=package_data,
    include_package_data=True,
    distclass=BinaryDistribution
)
