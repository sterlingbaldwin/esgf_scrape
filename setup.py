from setuptools import setup, find_packages

__version__ = (0, 0, 1)

setup(
    name='esgf_scrape',
    description='Utility to download and store node dataset metadata from the esgf network',
    keywords='mongo database data science climate',
    version='.'.join(str(d) for d in __version__),
    url='https://github.com/sterlingbaldwin/esgf_scrape',
    author='Sterling Baldwin for the Lawrence Livermore National Labratory',
    author_email='sterling16@mac.com',
    packages=find_packages(),
    scripts = [ 'scripts/esgf_scrape.py' ],
    install_requires = [ 'requests',
                         'esgf-pyclient',
                         'MyProxyClient' ],
    include_package_data=True,
    license='GPL-2.1',
    
)