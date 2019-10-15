from setuptools import setup, find_packages

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setup(
    name="amazon-scraper",
    version="0.0.1",
    author="Taha Sadiki",
    author_email="tahasadiki.pro@gmail.com",
    description="A tool to scrap amazon product data",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    entry_points="""
      [console_scripts]
      amazon-scraper=amazon_scraper:main
      """,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)