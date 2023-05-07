from setuptools import find_packages, setup

PACKAGE_NAME = "dates"

INSTALL_REQUIRES = ["pytest", "pre-commit"]

setup(
    name=PACKAGE_NAME,
    version="0.1",
    description="Computing the absolute number of days between two dates using Python builtins.",
    author="Louis Quinn",
    author_email="louisquinn@gmail.com",
    url="https://github.com/louisquinn/dates",
    license="MIT License",
    install_requires=INSTALL_REQUIRES,
    packages=([p for p in find_packages() if p.startswith(PACKAGE_NAME)]),
    python_requires=">=3.8",
    entry_points={"console_scripts": ["dates=dates.main:main"]},
)
