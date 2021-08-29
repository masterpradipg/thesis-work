from setuptools import setup, find_packages, Extension, dist
from sysconfig import get_config_vars
import numpy as np
import sys
import os
from ctypes.util import find_library

name = 'thesis'
version = '0.01'

npinclude = np.get_include()

(opt,) = get_config_vars('OPT')
os.environ['OPT'] = " ".join(
    flag for flag in opt.split() if flag != '-Wstrict-prototypes'
)


def extension(pkg, name) :
    ext = Extension('qubo/{}/{}'.format(pkg, name),
                    include_dirs = [npinclude],
                    libraries = ['quboc'],
                    library_dirs = ['/usr/lib', 'qubo/{}'.format(pkg)],
                    sources = ['qubo/{}/src/{}.cpp'.format(pkg, name)],
                    extra_compile_args = ['-std=c++11', '-Wno-format-security'])
    return ext

def cuda_extension(pkg, name) :
    ext = Extension('qubo/{}/{}'.format(pkg, name),
                    include_dirs = [npinclude],
                    libraries = ['quboc_cuda', 'quboc'],
                    library_dirs = ['/usr/lib', 'qubo/{}'.format(pkg)],
                    sources = ['qubo/{}/src/{}.cpp'.format(pkg, name)],
                    extra_compile_args = ['-std=c++11', '-Wno-format-security'])
    return ext

ext_modules = []
ext_modules.append(extension('cpu', 'cpu_formulas'))
ext_modules.append(extension('cpu', 'cpu_dg_annealer'))
ext_modules.append(extension('cpu', 'cpu_bg_annealer'))
if find_library('quboc_cuda') is not None :
    ext_modules.append(cuda_extension('cuda', 'cuda_device'))
    ext_modules.append(cuda_extension('cuda', 'cuda_formulas'))
    ext_modules.append(cuda_extension('cuda', 'cuda_dg_annealer'))
    ext_modules.append(cuda_extension('cuda', 'cuda_bg_annealer'))

pyver= [
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
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
    version=version,
    author=author,
    author_email=email,
    packages=find_packages(),
    install_requires=['numpy>=1.11'],
    keywords='Optimizing Budget pacing for Effective Online Ad Campaign using Quantum Accelerator models, GPU, CUDA',
    classifiers=classifiers,
    ext_modules=ext_modules
)
