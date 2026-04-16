from setuptools import setup, find_packages
setup(
    name="logwatch",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "logwatch = logwatch.logwatch:main"
        ]
    },
    install_requires=[],
    version="0.1",
    author="Luka Mamrikishvili",
    author_email="lukamamrik@proton.me",
    description="Log File Analyzer")
