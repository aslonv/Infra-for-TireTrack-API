from setuptools import setup


requires = [
    "falcon",
    "redis",
]

dev_requires = ["pytest", "black"]

setup(
    name="Interview project",
    version="1.0",
    install_requires=requires,
    extras_require={
        "dev": dev_requires,
    },
)
