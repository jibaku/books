from setuptools import setup, find_packages

setup(
    name="books",
    version="0.1.2",
    author="Fabien Schwob",
    author_email="fabien@x-phuture.com",
    description="A book management app",
    long_description="A book management app",
    license="BSD",
    url="https://hg.jibaku.net/modules/books/",
    packages=find_packages(exclude=[]),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
