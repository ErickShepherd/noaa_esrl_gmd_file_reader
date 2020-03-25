# Standard library imports.
import os
import sys

# Third party imports.
import setuptools

# Module dunder definitions.
#  - Versioning system: {major_version}.{minor_version}.{build_number}
__author__  = "Erick Edward Shepherd"
__version__ = "1.0.1"

setup_kwargs = {
    "name"                 : "noaa_esrl_gmd_file_reader",
    "version"              : __version__,
    "description"          : ("A package for reading NOAA ESRL GMD ASCII data"
                              "files."),
    "long_description"     : "",
    "author"               : __author__,
    "author_email"         : "Contact@ErickShepherd.com",
    "maintainer"           : __author__,
    "maintainer_email"     : "Contact@ErickShepherd.com",
    "url"                  : "https://darktarget.gsfc.nasa.gov/",
    "download_url"         : "",
    "packages"             : setuptools.find_packages(),
    "license"              : "AGPLv3"
}

if __name__ == "__main__":

    setuptools.setup(**setup_kwargs)
