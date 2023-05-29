import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = "0.0.0"
REPO_NAME = "text-summarization"
AUTHOR_USER_NAME = "brijesh24bs"
SRC_REPO = "text-summarizer"
AUTHOR_EMAIL = "brijesh24.bs@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    license="MIT",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"}
)
