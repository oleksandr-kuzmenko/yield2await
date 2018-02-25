from setuptools import setup


with open('requirements.txt') as f:
    install_requires = f.read().split()


with open('README.rst') as f:
    long_description = f.read()


setup(
    name='yield2await',
    version='0.0.1a3',
    description='Transform your python code to use async/await (PEP 492)',
    long_description=long_description,
    keywords='yield from asyncio coroutines with async await',
    url='https://github.com/alxpy/yield2await',
    author='Oleksandr Kuzmenko',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=install_requires,
    py_modules=['yield2await'],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': 'yield2await=yield2await:main',
    },
)
