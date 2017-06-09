import numpy as np
import astropy.time as time

class Epoch(object):

    def __init__(self):
        self.setEpoch('2017-01-01 00:00:00', format='iso', scale='utc')
        
    def setEpoch(self, *args, **kwargs):
        self._epoch = time(*args, **kwargs)