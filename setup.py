from setuptools import find_packages, setup

setup(
    name='netbox-licences',
    version='0.1',
    description='Provides licences, supports, etc.',
    url='https://github.com/Dzordzu/netbox-licences',
    author='Tomasz Durda',
    license='MIT',
    install_requires=['setuptools-git'],
    packages=find_packages(),
    package_data= {
       '': ['*.html', '*.htm', "*.py"],
    },
    # include_package_data=True
)
