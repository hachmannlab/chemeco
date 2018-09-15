import setuptools
from os import path
# import versioneer

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

if __name__ == "__main__":
    setuptools.setup(
        name='chemeco',
        version="0.1.0",
        description='A General-Purpose Framework for Data Mining Without Coding',
        long_description=long_description,
        author='Mojtaba Haghighatlari, Johannes Hachmann',
        author_email='mojtabah@buffalo.edu, hachmann@buffalo.edu',
        project_urls={
            'Source': 'https://github.com/hachmannlab/chemeco',
            'url': 'https://hachmannlab.github.io/chemeco/'
        },
        license='BSD-3C',
        packages=setuptools.find_packages(),
        scripts=['lib/chemeco'],

        install_requires=[
        ],
        extras_require={
            'docs': [
                'sphinx',
                'sphinxcontrib-napoleon',
                'sphinx_rtd_theme',
                'numpydoc',
            ],
            'tests': [
                'pytest',
                'pytest-cov',
                'pytest-pep8',
                'tox',
            ],
        },

        tests_require=[
            'pytest',
            'pytest-cov',
            'pytest-pep8',
            'tox',
        ],

        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'Programming Language :: Python :: 2.7',
        ],
        zip_safe=False,
    )
