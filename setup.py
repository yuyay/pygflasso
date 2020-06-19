from setuptools import setup, find_packages

setup(
    name="pygflasso",
    version="0.1",
    install_requires=[
        "numpy", "scipy", "scikit-learn", "matplotlib", "jupyter", "ipython"],
    packages=find_packages(
        exclude=('examples', 'docs', '.vscode', 'docker', 'scripts', 'experiments', 'data')),
)