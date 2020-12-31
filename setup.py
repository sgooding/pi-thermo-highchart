import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pi-thermo-highchart", # Replace with your own username
    version="0.0.1",
    author="Sean",
    author_email="author@example.com",
    description="A sql, highchart, and flask example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sgooding/pi-thermo-highchart",
    packages=setuptools.find_packages(),
    include_package_data=True,    # include everything in source control
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
        use_scm_version = {
        "root": ".",
        "relative_to": __file__,
        "local_scheme": "node-and-timestamp"
    },
    setup_requires=['setuptools_scm',
                   ],
    install_requires = ['Flask',
                        'pandas',
                        'pandas_highcharts']
)