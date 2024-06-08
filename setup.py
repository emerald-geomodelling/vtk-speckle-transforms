import setuptools
import distutils.command.build
import distutils.command.sdist
import os

setuptools.setup(
    name='vtk-speckle-transforms',
    version='0.0.1',
    description='Tools to transform VTK file into Speckle-compatible formats',
    long_description='experimental repository for transforming Visualization Toolkit (vtk) files and meshes, the main format used by ParaView, into fils that can be read into speckle',
    long_description_content_type="text/markdown",
    author='Craig W. Christensen, Joost Gevaert',
    author_email='cch@emrld.no',
    url='https://github.com/emerald-geomodelling/vtk-speckle-transforms',
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'pycharm',
    ],
)
