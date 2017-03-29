import sys
from setuptools import setup

setup(
    name='Flask-OrientDB',
    py_modules=['flask_orientdb'],
    version='0.1.mapcloud',
    license='BSD',
    description='A Flask extension for using OrientDB with Flask',
    long_description=__doc__,
    author='Cory Althoff',
    author_email='coryedwardalthoff@gmail.com',
    url='https://github.com/mapcloud/flask-orientdb',
    install_requires= ['Flask', 'pyorient==1.5.4'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
