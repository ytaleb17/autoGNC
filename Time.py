import numpy as np
from astropy.time as time
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
class Time(object):

    def __init__(self):
        self.setEpoch('2017-01-01 00:00:00', format='iso', scale='utc')
        
    def setEpoch(self, *args, **kwargs):
        self._epoch = time.Time(*args, **kwargs)
     
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
	t = time.Time(isodate, format='iso', scale='utc')
	
	return t
 
    def TDT(t):
	"""
	Not used because TDT(t) = t.tt 
	"""
	dt = time.TimeDelta(32.184, format='sec')
	tdt = t.tai + dt
	
	return tdt
	
    def T_TDT(t):
	"""
	Julian centuries of Dynamical Time
	"""
	ttdt = (t.tt.jd - 2451545.0)/36525.0
	return ttdt

    def TDB(t):
	"""
	Not used because TDB(t) == t.tdb
	"""
	M_e = (357.5277233 + 35999.05034 * T_TDT(t))*np.pi/180.0
	dt = time.TimeDelta(0.001658*np.sin(M_e) + 0.00001385*np.sin(2.0*M_e)
	tdb = TDT(t) + dt
	return tdb

    def T_TDB(t):
	JD2000 = 2451545.0
	ttdb = (t.tdb.jd - JD2000)/36525.0

	return ttdb

    def TP(t):
	"""
	Precession transformation according to IAU-76/FK5
	Approximated, go to latest edition of Vallado for full
	MOD to GCRF
	"""
	DEG2RAD = np.pi/180.0
	ARCSEC2RAD = DEG2RAD/3600.0
	dT = T_TDB(t)
	dT2 = dT**2
	dT3 = dt**3
	
	zeta = (2306.2181*dT + 0.30188*dT2 + 0.017998*dT3)*ARCSEC2RAD
	theta = (2004.3109*dT - 0.42665*dT2 - 0.041833*dT3)*ARCSEC2RAD
	z = (2306.2181*dT + 1.09468*dT2 + 0.018203*dT3)*ARCSEC2RAD
	
	czeta = np.cos(zeta)
	szeta = np.sin(zeta)
	ctheta = np.cos(theta)
	stheta = np.sin(theta)
	cz = np.cos(z)
	sz = np.sin(z)
		 
	tp = np.array([[ctheta*cz*czeta - sz*szeta, sz*ctheta*czeta + szeta*cz, stheta*czeta],
		       [-szeta*ctheta*cz - sz*czeta, -sz*szeta*ctheta + cz*czeta, -stheta*szeta],
		       [-stheta*cz, -stheta*sz, ctheta]])

	return tp


