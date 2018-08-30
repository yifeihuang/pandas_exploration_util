import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pandas Data Exploration Utility Package",
    version="0.0.3",
    author="Yifei Huang",
    author_email="yifei.huang@gmail.com",
    description="Utility functions to help with exploratory data analysis on top the Pandas APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yifeihuang/pandas_exploration_util",
    packages=setuptools.find_packages(),
    install_requires=[
          'pandas',
          'plotly',
          'ipywidgets',
          'IPython'
      ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
