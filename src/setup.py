from setuptools import setup, find_packages


requires = [
    "falcon",
    "redis",
]

dev_requires = ["pytest", "black"]

setup(
    name="Interview project",
    version="1.0",
    packages=find_packages(),
    package_dir={'':'.'},
    install_requires=requires,
    extras_require={
        "dev": dev_requires,
    },
)
