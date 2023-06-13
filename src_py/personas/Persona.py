from abc import ABC

class Persona(ABC):
    def __init__(self, nombre: str, ID: int, Email: str):
        self.__nombre = nombre
        self.__ID = ID
        self.__Email = Email

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getID(self) -> int:
        return self.__ID

    def setID(self, ID: int):
        self.__ID = ID

    def getEmail(self) -> str:
        return self.__Email

    def setEmail(self, Email: str):
        self.__Email = Email
