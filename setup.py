from setuptools import setup, find_packages

setup(
    name="SmartSparsity",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Efficiently run large language models on various platforms using smart sparsity and offloading techniques.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/SmartSparsity",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "kivy==2.1.0",
        "psutil==5.8.0",
        "torch==1.9.0",
        "transformers==4.9.2",
    ],
    extras_require={
        "dev": [
            "pyinstaller==4.5.1",
            "unittest2==1.1.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "smartsparsity=app:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)