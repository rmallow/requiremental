import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="requiremental-rmallow", # Replace with your own username
    version="0.0.1",
    author="Robert Mallow",
    author_email="mail@rmallow.com",
    description="Handle the requirements for your projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://https://github.com/rmallow/requiremental",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
