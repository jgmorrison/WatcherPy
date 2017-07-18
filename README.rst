WatcherPy
=========

A simple CLI program to watch an html file and css for changes and reload the browser when a change is saved to either file.

**Installation**

Install from PyPI

    ``pip install watcherpy``

Watcherpy is also available on Anaconda.org

    ``conda install -c jmorrison watcherpy``

**Usage**

Just pass the html file you want to reload and watch as the first argument and the css file you want to watch as the second argument. If either file changes the html file passed in the first argument will be automatically reloaded in the browser or a browser will launch if not already opened.

    ``watcher index.html style.css``
