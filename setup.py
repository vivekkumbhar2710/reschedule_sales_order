from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in reschedule_sales_order/__init__.py
from reschedule_sales_order import __version__ as version

setup(
	name="reschedule_sales_order",
	version=version,
	description="It is reschedule sales order",
	author="Quantbit Technologies",
	author_email="contact@erpdata.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
