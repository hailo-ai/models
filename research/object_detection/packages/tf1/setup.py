"""Setup script for object_detection with TF1.0."""
import os
from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = ['pillow==8.4.0', 'lxml==4.9.2', 'matplotlib==3.3.4', 'Cython==0.29.33',
                     'contextlib2==21.6.0', 'tf-slim==1.1.0', 'six==1.16.0', 'pycocotools==2.0.6', 'lvis==0.5.3',
                     'scipy==1.5.4', 'pandas==1.1.5']

setup(
    name='object_detection',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    packages=(
        [p for p in find_packages() if p.startswith('object_detection')] +
        find_packages(where=os.path.join('.', 'slim'))),
    package_dir={
        'datasets': os.path.join('slim', 'datasets'),
        'nets': os.path.join('slim', 'nets'),
        'preprocessing': os.path.join('slim', 'preprocessing'),
        'deployment': os.path.join('slim', 'deployment'),
        'scripts': os.path.join('slim', 'scripts'),
    },
    description='Tensorflow Object Detection Library with TF1.0',
    python_requires='>3.6',
)
