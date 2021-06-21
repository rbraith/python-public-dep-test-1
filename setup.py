from setuptools import setup, find_packages

setup(
    name="public-python-test-1",
    version="0.1.0",
    description="Public github dependency test.",
    author="Richard Braithwaite",
    author_email="r.braithwaite@live.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
