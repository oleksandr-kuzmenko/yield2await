from setuptools import setup


setup(
    name='yield2await',
    version='0.0.1a2',
    description='Transform your python code to use async/await (PEP 492)',
    keywords='yield from asyncio coroutines with async await',
    url='https://github.com/alxpy/yield2await',
    author='Oleksandr Kuzmenko',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=['astor==0.6.2'],
    py_modules=['yield2await'],
    python_requires='>=3.4',
    entry_points={
        'console_scripts': 'yield2await=yield2await:main',
    },
)
