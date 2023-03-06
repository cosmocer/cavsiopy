from setuptools import setup, find_packages

setup(name='cavsiopy',
      version='0.9.0',
      description='Package for finding and plotting spacecraft instrument attitude',
      long_description='Python package for calculation and visualization of spacecraft instrument pointing direction',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Linux :: Ubuntu',
	'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics ',
	'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Utilities',
      ],
      keywords=[
'spacecraft', 'attitude', 'orientation', 'Swarm', 'RRI', 'Euler', 'rotation matrices',
],
      url='http://github.com/cosmocer/cavsiopy',
      author='E. Ceren Kalafatoglu Eyiguler, Warren Holley, Donald W. Danskin, Andrew D. Howarth, Kuldeep Pandey, Carley Martin, Glenn C. Hussey, Robert G. Gillies',
      author_email='ceren.eyiguler@usask.ca',
      license='MIT',
      packages=['cavsiopy'],
      packages=setuptools.find_packages(where="src")
      package_dir={'geospacepy' : 'geospacepy'},
      license='LICENSE.txt',
      install_requires=[
          'numpy','astropy','cartopy','matplotlib','h5py','geopy','pysofa',
      ],
      zip_safe=False,
      python_requires=">=3.4",)

print("... All done!")


