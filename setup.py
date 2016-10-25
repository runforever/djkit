# coding: utf-8

from setuptools import setup

setup(
    name='djkit',
    version='0.2',
    description='django starter kit',
    url='https://github.com/BurnishTechCN/djkit',
    author='runforever',
    author_email='c.chenchao.c@gmail.com',
    license='WTFPL',
    packages=['djkit'],
    install_requires=[
        'virtualenv',
        'click',
    ],
    scripts = ['bin/djkit'],
    zip_safe=False,
)
