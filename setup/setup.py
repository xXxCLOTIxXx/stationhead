from setuptools import setup, find_packages

with open("README.md", "r") as file:
	long_description = file.read()

link = 'https://github.com/xXxCLOTIxXx/stationhead/archive/refs/heads/main.zip'
ver = '1.0'

setup(
	name = "stationhead",
	version = ver,
	url = "https://github.com/xXxCLOTIxXx/stationhead",
	download_url = link,
	license = "MIT",
	author = "Xsarz",
	author_email = "xsarzy@gmail.com",
	description = "Library for creating stationhead bots and scripts.",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	keywords = [
		"stationhead.py",
		"stationhead",
		"stationhead-py",
		"stationhead-bot",
		"api",
		"python",
		"python3",
		"python3.x",
		"xsarz",
		"official",
		"sync"
	],
	install_requires = [
		"requests"
	],
	packages = find_packages()
)
