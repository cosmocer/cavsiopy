# cavsiopy: Calculation and Visualization of Spacecraft Instrument Orientation

## Description:
cavsiopy imports the ephemerides and attitude information of the spacecraft and calculates the pointing direction of an instrument onboard.

## Table of Contents:
This package contains routines for
1. Finding the orientation of a spacecraft
2. Finding the look direction of an instrument on-board the spacecraft
3. Calculation of the look angles of the spacecraft (elevation and azimuth)
4. Calculation of the look angles of the instrument (elevation and azimuth)
5. Calculation of the distance between the spacecraft and a designated point on the ground
6. Calculation of the line-of-sight direction vector from the spacecraft to the ground point
7. Transformation routines for the transformations between GEI J2K, ECEF, NED, NEC, ICRF, ITRF reference frames.
8. Visualization of spacecraft and instrument direction in 2D and 3D (simple or overlaid on geographical regions of the Earth below the satellite trajectory).

The pointing direction vectors can be obtained in GEI J2K, ECEF, NED, NEC, ICRF, ITRF.

## Requirements:
numpy, matplotlib, astropy, cartopy, geopy

## Optional:
* spacepy: If you work with cdf files
* h5py: If you work with HDF files

## Installation:
Before installation please see the requirements.

pip install cavsiopy

## Usage:
Given the information of instrument body vector with respect to spacecraft in spacecraft body frame X, Y and Z axes, users can obtain the pointing direction of an instrument on-board spacecraft with this python package. For antenna on spacecraft, this information is useful for finding the deviation of the antenna boresight from the line-of-sight signal transmitted from a ground transmitter. For imagers, the user can easily find the ground coverage of the imager if the field of view of the imager is known.


Contributing: Andrew Howarth, Warren Holley

Credits: C. Eyiguler, Warren Holley

License: Apache License V2.0
