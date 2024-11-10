from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    author="Gaurav Kadyan",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    test_suite="tests",  # Directory containing test files, if tests are under a "tests" folder
)
