from setuptools import setup, find_packages
from typing import List

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


__version__ = "0.0.4"
REPO_NAME = "start_python_pkg"
PKG_NAME = "MongoConnect"
AUTHOR_USER_NAME = "TejaswiniT167"
AUTHOR_EMAIL = "tejaswini3477@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=["pymongo", "pymongo[srv]", "dnspython", "pandas", "numpy", "ensure", "pytest"]
)
