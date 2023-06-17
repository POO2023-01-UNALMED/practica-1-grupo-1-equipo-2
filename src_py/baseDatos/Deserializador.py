import pickle
from src_py.Calendario.gestionDatos import gestionDatos

class Deserializador:
    @classmethod
    def deserializador(cls):
        file = open("PYTHON/src/baseDatos/temp/profesores.pkl", "wb")
        pcs = pickle.load(file)
        gestionDatos.setProfesores(pcs)

        file.close()

        file = open("PYTHON/src/baseDatos/temp/estudiantes.pkl", "wb")
        pcs = pickle.load(file)
        gestionDatos.setEstudiantes(pcs)

        file.close()


        file = open("PYTHON/src/baseDatos/temp/becas.pkl", "wb")
        pcs = pickle.load(file)
        gestionDatos.setSistemaBecas(pcs)

        file.close()

        file = open("PYTHON/src/baseDatos/temp/materias.pkl", "wb")
        pcs = pickle.load(file)
        gestionDatos.setMaterias(pcs)

        file.close()