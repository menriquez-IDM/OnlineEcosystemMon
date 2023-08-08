from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
    pkg_name = 'sysmonlib'
with open("requirements.txt", "r") as requirements_file:
    requirements = requirements_file.read().split("\n")
    
setup(
    name=pkg_name,
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # List any dependencies your package requires (if any). This should eventually be replaced with the 'requirements' variable.
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Minerva Enriquez',
    author_email='minerva.enriquez@gatesfoundation.org',
    description='Functions for monitoring system resources',
    url='https://github.com/menriquez-idm/onlineecosystemmon',
    # Add other relevant information about your package.
)
