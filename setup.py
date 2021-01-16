from setuptools import setup
setup(
    name = 'SCA-Cloud-School-Application',
    version = '2.0.3',
    packages = ['sca-cli'],
    entry_points = {
        'console_scripts': [
            'sca-cli = sca-cli.__main__:main'
        ]
    })
