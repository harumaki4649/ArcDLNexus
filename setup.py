# Author: Kenta Nakamura <c60evaporator@gmail.com>
# Copyright (c) 2020-2021 Kenta Nakamura
# License: BSD 3 clause

from setuptools import setup
import ArcDLNexus

DESCRIPTION = "ArcDLNexus: PythonからWayback Machineのアーカイブ（サイト）をダウンロードするモジュールです。"
NAME = 'ArcDLNexus'
AUTHOR = 'ArcDLNexus'
AUTHOR_EMAIL = 'support@disnana.com'
URL = 'https://github.com/harumaki4649/PayNexus'
LICENSE = 'BSD 3-Clause'
DOWNLOAD_URL = 'https://github.com/harumaki4649/PayNexus'
VERSION = ArcDLNexus.__version__
PYTHON_REQUIRES = ">=3.9"
# Readmeのファイルパス指定
readme_path = r'C:\Users\msi-z\OneDrive\ドキュメント\GitHub\ArcDLNexus\README.md'

with open("./ArcDLNexus/requirements.txt", "r", encoding="utf-8") as f:
    INSTALL_REQUIRES = f.readlines()

EXTRAS_REQUIRE = {
}

PACKAGES = [
    'ArcDLNexus'
]

CLASSIFIERS = [
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Multimedia :: Graphics',
    'Framework :: Matplotlib',
]

with open(readme_path, 'r', encoding="utf-8") as fp:
    readme = fp.read()
long_description = readme

setup(name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description_content_type="text/markdown",
      long_description=long_description,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE,
      packages=PACKAGES,
      classifiers=CLASSIFIERS
      )
