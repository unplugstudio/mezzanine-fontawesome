import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='mezzanine-fontawesome',
    version='0.2.4',
    packages=['mezzanine_fontawesome'],
    description='A Mezzanine/Django app that provides an IconField to associate \
                 fontawesome icons with model instances.',
    url='https://gitlab.com/tigris-webdev/mezzanine-fontawesome',
    author='Eduardo Vela',
    author_email='eduardo3vela@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)
