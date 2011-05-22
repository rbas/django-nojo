# coding: utf-8
from setuptools import setup, find_packages

setup(
    name='django-nojo',
    version='0.1.0',
    author='Rbas & Rumman23',
    author_email='rbas.cz@gmial.com',
    description=('Django common tools'),
    license='BSD',
    packages=find_packages(),
    url='http://rbas@github.com/rbas/django-nojo/',
    install_requires=['setuptools'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
