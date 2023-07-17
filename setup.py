from setuptools import setup, find_packages

setup(
    name="gitbook2mkdocs",
    version="0.0.2",
    description="MkDocs plugin for converting gitbook syntax to mkdocs",
    keywords="mkdocs markdown gitbook",
    url="https://github.com/pledra/gitbook2mkdocs/",
    author="Paul Catinean",
    author_email="pca@pledra.com",
    license="MIT",
    python_requires=">=3.6",
    install_requires=["mkdocs>=1.1"],
    packages=find_packages(),
    entry_points={"mkdocs.plugins": ["gitbook2mkdocs = gitbook2mkdocs.plugin:Gitbook2Mkdocs"]},
)