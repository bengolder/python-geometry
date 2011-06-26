from setuptools import setup, find_packages

setup(
    name = "geometry",
    version = "0.1",
    packages = find_packages(),
    #scripts = [''],
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['numpy>=1.5'],
    test_suite = "test.test_all",
    package_data = {
    },

    # metadata for upload to PyPI
    author = "Stefano Borini", # add others
    author_email = "stefano.borini@ferrara.linux.it", # add others
    description = "2D and 3D geometry library",
    license = "BSD 2",
    keywords = "geometry 3d 2d",
    url = "https://github.com/stefanoborini/python-geometry/",  

    # could also include long_description, download_url, classifiers, etc.
)
