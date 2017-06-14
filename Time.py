import numpy as np
from astropy.time import Time as time
"""
Sidereal Time = Time to 360 deg rotation of earth as measured by measuring transit of some star over Greenwich = 23 h 56 min
	Mean Sidereal Time = refers to mean equanox which only considers secular motion (precession)
	Apparent Sidereal Time = measures from true vernal equinox (includes periodic motion)
Solar Time = Time measured as transit of Sun over Greenwich, longer than sidereal because of Earth motion around Sun = 24 h
Universtal Time (UT) = Time measured from transit of an idealized Mean Sun derived mathematically from Sidereal Time
Dynamical Time (DT) = Time derived from motion of celestial body (eg moon around earth). Needs relativistic corrections
Atomic Time (AT) = Most precise, based on quantum transitions of electrons in Cesium-133
Coordinated Universal Time (UTC) = most common, derived from atomic time and includes leap seconds for fixing irregularities in earth rotation
Julian Date (JD) = time measured in days from epoch January 1, 4713 BC. Named after creator's father not Caesar. Defined at noon so night owl astronomers can collect all their data in one julian day.
"""
class Epoch(object):

    def __init__(self):
        self.setEpoch('2017-01-01 00:00:00', format='iso', scale='utc')
        
    def setEpoch(self, *args, **kwargs):
        self._epoch = time(*args, **kwargs)
     
    def local_mean_sidereal_time(t,lon):
	"""
	full algorithm located in page 61 of Vallado
	returns array in degrees
	"""
	lmst = t.sidereal_time('mean', lon).degree
	return lmst

    def JD(t):
	if t.scale != 'ut1':
		t = t.ut1

	jd = t.jd
	
	return jd
    
    def utc(isodate):
	t = time(isodate, format='iso', scale='utc')
	
	return t
 
    def T_TDT(t):
	"""
	Julian centuries of Dynamical Time
	"""
	T = (TDT(t).jd - 2451545.0)/36525.0
	return T

    def  
