from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in saudi_arabia_compliance/__init__.py
from saudi_arabia_compliance import __version__ as version

setup(
	name="saudi_arabia_compliance",
	version=version,
	description="App to include Saudi Arabia specific compliance ifor ERPNext",
	author="Frappe Technologies Private Limited",
	author_email="diksha@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
