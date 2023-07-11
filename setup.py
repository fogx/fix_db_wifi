from setuptools import setup, find_packages

setup(
    name='fix_db_wifi',
    version='0.1.0',
    author="Leon Wolf",
    description="A tool to fix IP conflicts between Deutsche Bahn WIFI and Ubuntu/Docker",
    url="github.com/fogx/fix_db_wifi",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'fix-db-wifi=fix_db_wifi.main:main',
        ],
    },
)
