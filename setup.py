import setuptools

REQUIRES = [
    'aiohttp>=3.9.1',
]

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name='sanix',
    version='1.0.0',
    description=
    'Python wrapper for getting measurements data from Sanix devices.',
    long_description=long_description,
    url='https://github.com/tomaszsluszniak/sanix_py',
    license='MIT',
    packages=['sanix'],
    install_requires=REQUIRES,
    python_requires='>=3.10.0',
    author='Tomasz Słuszniak',
    author_email='tomasz.sluszniak@gmail.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    test_suite='tests',
)