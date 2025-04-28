from setuptools import setup, find_packages

setup(
    name='aws-server-config',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A server configuration system for initializing AWS services.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'boto3',
        'pytest',  # Add any other dependencies as needed
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)