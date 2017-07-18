from distutils.core import setup

setup(
    name ='watcherpy',
    version ='0.1.0',
    description ='Simple CLI tool to watch html and css files and reload the browser on change.',
    long_description = open("README.rst").read(),
    author ='John Morrison',
    author_email ='john@johmorrison.io',
    url = "https://github.com/jgmorrison/watcherpy",
    packages = ["watcherpy"],
    entry_points = {"console_scripts" : ["watcher = watcherpy.__main__:main"]}
)
