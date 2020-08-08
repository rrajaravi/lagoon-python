  
#!/usr/bin/env python


from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from lagoon import __version__, __maintainer__, __email__, __license__
import sys

tests_require = ["pytest==6.0.1", "unittest2", "pytest-cov"]
ci_require = ["flake8", "codecov"]
if sys.version_info >= (3, 6, 0):
    ci_require.append("black")

long_description = open("README.md", "r").read()

install_requires = []


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main(["-v", "--cov=./"])
        sys.exit(errno)


setup(
    name="lagoon-python",
    version=__version__,
    author=__maintainer__,
    author_email=__email__,
    url="https://github.com/rrajaravi/lagoon-python",
    description="Client for lagoon. An inmemory and highly concurrent bloom filter service based on json-rpc.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=__license__,
    packages=find_packages(),
    zip_safe=False,
    install_requires=install_requires,
    extras_require={"test": tests_require, "ci": ci_require},
    cmdclass={"test": PyTest},
    tests_require=tests_require,
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)