from setuptools import setup, find_packages

setup(
    name='wolt-calculator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        
        'flask',
        'other_dependency',
    ],
    
    author='David Manning',
    author_email='david.manning@wolt.com',
    description='A simple delivery fee calculator backend script',
    url='https://github.com/ID-Mahone/wolt-calculator',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
