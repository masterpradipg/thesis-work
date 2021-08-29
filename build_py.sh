#!/bin/bash


pip install numpy


make clean all
cd ../../..

python setup_whl.py bdist_wheel --plat-name manylinux1_x86_64 # --python-tag=py2
