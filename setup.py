import setuptools


with open("README.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="secureme",
    version="0.0.4",
    author="Jainam Oswal",
    author_email="Jainamoswal@gmail.com",
    description="Developed by Developers, Contributed by Contributers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jainamoswal/secureme",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)