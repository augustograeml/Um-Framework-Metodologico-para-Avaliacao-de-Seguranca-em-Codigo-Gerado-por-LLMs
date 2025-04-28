from setuptools import setup, find_packages

setup(
    name='python-backup-app',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python application for saving and restoring Python objects from files.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your dependencies here, e.g., 'somepackage>=1.0.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)