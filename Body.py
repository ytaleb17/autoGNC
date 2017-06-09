class Body(object):
    
    def __init__(self, name=None, mass=0.0):
        super(Body, self).__init__()

        self.name = name
        self._mass = mass
        self._parent = None
        
    def getName(self):
        return self._name
        
    def getMass(self):
        return self._mass
    
    def setName(self, mass):
        self._name = name
        
    def setMass(self, mass):
        self._mass = mass
    
    def setParent(self, p):
        self._parent = p