from setuptools import setup, find_packages

setup(
    name='python-app',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python application that dynamically loads user-provided libraries to extend its functionalities.',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here, e.g.:
        # 'some-library',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)