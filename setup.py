from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()

exec(open('izpyc/version.py').read())

setup(
    name="izpyc",
    version=__version__,
    license="MIT",
    description="Python interface for iZ-C",
    author="t.fujiwara",
    url="https://github.com/tofjw/python-iz",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    #install_requires=_requires_from_file('requirements.txt'),
    #setup_requires=["pytest-runner"],
    #tests_require=["pytest", "pytest-cov"]
)
