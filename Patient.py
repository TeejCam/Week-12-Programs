class Patient:
    def __init__(self, fName, mName, lName,
                 address, city, state, zip, phone,
                 emergencyContactName, emergencyContactPhone):
        self.fName = fName
        self.mName = mName
        self.lName = lName
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.emergencyContactName = emergencyContactName
        self.emergencyContactPhone = emergencyContactPhone

    # Accessors
    def getFName(self):
        return self.fName

    def getMName(self):
        return self.mName

    def getLName(self):
        return self.lName

    def getAddress(self):
        return self.address

    def getCity(self):
        return self.city

    def getState(self):
        return self.state

    def getZip(self):
        return self.zip

    def getPhone(self):
        return self.phone

    def getEmergencyContactName(self):
        return self.emergencyContactName

    def getEmergencyContactPhone(self):
        return self.emergencyContactPhone

    # Mutators
    def setFName(self, fName):
        self.fName = fName

    def setMName(self, mName):
        self.mName = mName

    def setLName(self, lName):
        self.lName = lName

    def setAddress(self, address):
        self.address = address

    def setCity(self, city):
        self.city = city

    def setState(self, state):
        self.state = state

    def setZip(self, zip):
        self.zip = zip

    def setPhone(self, phone):
        self.phone = phone

    def setEmergencyContactName(self, emergencyContactName):
        self.emergencyContactName = emergencyContactName

    def setEmergencyContactPhone(self, emergencyContactPhone):
        self.emergencyContactPhone = emergencyContactPhone

        