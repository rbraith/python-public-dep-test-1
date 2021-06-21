from setuptools import setup, find_packages
import pathlib

root_dir = pathlib.Path(__file__).parent.resolve()

def get_long_description()->str:
    return (root_dir / "README.md").read_text(encoding="utf-8")

def get_version()->str:
    version_file = (root_dir / "src" / "rbraith" / "version.py")
    version_text = version_file.read_text(encoding="utf-8").split("\n")
    for line in version_text:
        if line.startswith("__version__"): return line.split("\"")[1]

setup(
    name="public-python-test-1",
    version=get_version(),
    description="Public github dependency test.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown", 
    author="Richard Braithwaite",
    author_email="r.braithwaite@live.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    # install_requires = [],
    # include_package_data=True,
    # entry_points = {"console_scripts":[], "gui_scripts":[]},
)
