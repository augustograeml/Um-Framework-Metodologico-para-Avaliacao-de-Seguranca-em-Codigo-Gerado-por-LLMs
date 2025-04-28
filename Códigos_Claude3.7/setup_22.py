from setuptools import setup, find_packages

setup(
    name='config-system',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A configuration management system for loading and saving configuration files in various formats.',
    packages=find_packages(),
    install_requires=[
        'PyYAML',  # For YAML serialization
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)