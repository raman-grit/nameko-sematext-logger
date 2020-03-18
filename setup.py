from setuptools import setup

setup(
    name="nameko-sematext-logger",
    version="0.0.1",
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