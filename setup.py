from setuptools import  find_packages
from distutils.core import setup

setup(
        name='HEAH', 
        version='0.1.0',
        author='Ta-Wei Ho',
        author_email='davidho@gapp.nthu.edu.tw',
        maintainer='Ta-Wei Ho',
        maintainer_email='davidho@gapp.nthu.edu.tw',
        licence='OSI Approved, MIT License',
        keywords='High energy physics',
        python_requires='>=3.6',
        setup_requires=[
            'setuptools==39.0.1',
            'pytest-runner>=3.0',
            ],
        install_requires=[
            'pandas==1.0.5',
            'numpy>=1.19.0',
            ],
        tests_require=[
            'pytest>=3.3.1',
            'pytest-cov>=2.5.1',
            ],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers :: HEP students',
            'Topic :: Software Development :: Build Tools',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.6.9',
            ],
        url='https://github.com/davidho27941/HEAH',
        packages=find_packages(),
        zip_safe=False)
