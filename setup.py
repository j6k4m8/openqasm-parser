from setuptools import find_packages, setup

setup(
    name="openqasmparser",
    author="Eddie Schoute",
    author_email="",
    description="",
    packages=find_packages("openqasm"),
    package_dir={"": "openqasm"},
    python_requires=">=3.6.0",
)
