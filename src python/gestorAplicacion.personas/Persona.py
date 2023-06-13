
class Persona:
    def __init__(self, nombre, ID, Email):
        self.nombre = nombre
        self.ID = ID
        self.Email = Email

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getID(self):
        return self.ID

    def setID(self, ID):
        self.ID = ID

    def getEmail(self):
        return self.Email

    def setEmail(self, Email):
        self.Email = Email
