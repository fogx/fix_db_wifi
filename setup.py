from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="fix_db_wifi",
    version="0.1.2",
    author="Leon Wolf",
    author_email="fogxdev@gmail.com",
    description="A tool to fix IP conflicts between Deutsche Bahn WIFI and Ubuntu/Docker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fogx/fix_db_wifi",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "fix-db-wifi=fix_db_wifi.main:main",
        ],
    },
)
