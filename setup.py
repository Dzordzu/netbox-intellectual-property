from setuptools import find_packages, setup
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='netbox-licences',
    version='0.1',
    description='Provides licences for netbox',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/Dzordzu/netbox-licences',
    author='Tomasz Durda',
    license='MIT',
    install_requires=['setuptools-git'],
    packages=find_packages(),
    include_package_data=True
)
