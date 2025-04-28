from setuptools import setup, find_packages

setup(
    name='config-system',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A configuration system for loading and saving serialized configuration files.',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)