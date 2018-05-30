from setuptools import setup

setup(
    name='firstdown_cloud',
    version='0.0.1',
    url='https://github.jpl.nasa.gov/mpowell/FirstDownCloud',
    license='',
    author='Mark Powell',
    author_email='Mark.W.Powell@jpl.nasa.gov',
    description='Python library for securely publishing JPL ops data to Govcloud.',

    packages=['firstdown_cloud'],

    test_suite='tests',

    install_requires=['pycrypto','boto3'],

    tests_require=['moto'],

    entry_points={
        'console_scripts': [
            'fds3 = firstdown_cloud.s3:main'
        ]
    }
)
