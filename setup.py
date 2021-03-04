from setuptools import setup, find_packages
from censearch import VERSION

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="censearch",
    version=VERSION,
    author="Julia A M",
    author_email="jlearning@tuta.io",
    description="search censored tweets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sudo-julia/censearch",
    packages=find_packages(),
    modules=["censearch_args"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Topic :: Sociology",
        "Topic :: System :: Archiving :: Backup",
        "Topic :: Terminals",
    ],
    install_requires=[
        "TwitterAPI>=2.6.9",
    ],
    python_requires=">=3.7",
    entry_points={"console_scripts": ["censearch = censearch.__main__:main"]},
)
