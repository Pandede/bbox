from setuptools import find_packages, setup

setup(
    name='bbox',
    version='0.1.0',
    license='MIT',
    description='A Python library for handling the 2D bounding box.',
    author='Pandede',
    url='https://github.com/Pandede/bbox',
    download_url='https://github.com/Pandede/bbox/archive/refs/tags/v0.1.0.tar.gz',
    keywords=['bbox', 'geometry', 'spatial', 'detection', 'yolo'],
    packages=find_packages(),
    install_requires=[
        "pydantic"
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)
