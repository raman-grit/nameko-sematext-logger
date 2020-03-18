from setuptools import setup, find_packages

setup(
    name="nameko-sematext-logger",
    version="0.0.2",
    packages=find_packages(exclude=["test", "test.*"]),
    description="Nameko extension for sematext logging",
    long_description=open("README.md").read(),
    author="Raman Damodar Shahdadpuri",
    author_email="raman@gritfirst.com",
    url="https://bitbucket.org/gritfirst/nameko-sematext-logger",
    install_requires=["nameko>=2.7.0"],
    dependency_links=[],
    zip_safe=True,
    license="GritFirst"
)