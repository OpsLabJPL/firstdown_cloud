from setuptools import setup, find_packages

setup(
    name='FirstDownCloud',
    version='0.0.1',
    url='https://github.jpl.nasa.gov/mpowell/FirstDownCloud',
    license='',
    author='Mark Powell',
    author_email='Mark.W.Powell@jpl.nasa.gov',
    description='Python library for securely publishing JPL ops data to Govcloud.',

    packages=find_packages(exclude=['tests']),

    test_suite='tests',

    install_requires=['pycrypto','boto3'],

    tests_require=['moto'],

    entry_points={
        'console_scripts': [
            'fds3 = FirstDownCloud.s3:main'
        ]
    }
)
