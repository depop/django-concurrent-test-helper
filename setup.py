#!/usr/bin/env python
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)


setup(
    name='django-concurrent-test-helper',
    version='0.1.9',
    description="Helpers for executing Django app code concurrently within Django tests",
    long_description=open('README.rst').read(),
    author="Anentropic",
    author_email="ego@anentropic.com",
    url="https://github.com/depop/django-concurrent-test-helper",
    packages=['django_concurrent_tests'],
    license='MIT',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    tests_require=[
        'tox>=1.8',
    ],
    cmdclass={'test': Tox},
)