class Procedure:
    def __init__(self, procedure, date, name, charge):
        self.procedure = procedure
        self.date = date
        self.name = name
        self.charge = charge

    def getProcedure(self):
        return self.procedure

    def getDate(self):
        return self.date

    def getName(self):
        return self.name

    def getCharge(self):
        return self.charge

    def setProcedure(self, procedure):
        self.procedure = procedure

    def setDate(self, date):
        self.date = date

    def setName(self, name):
        self.name = name

    def setCharge(self, charge):
        self.charge = charge

