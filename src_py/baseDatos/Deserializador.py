import pickle
from src_py.Calendario.gestionDatos import gestionDatos


class Deserializador:

    @staticmethod
    def deserializador():
        file = open("src_py/baseDatos/temp/profesores.pkl", "wb")
        pcs = pickle.load(file)
        gestionDatos.setProfesores(pcs)

        file.close()

        file = open("src_py/baseDatos/temp/estudiantes.pkl", "wb")
        pcs = pickle.load(file)
        gestionDatos.setEstudiantes(pcs)

        file.close()

        file = open("src_py/baseDatos/temp/becas.pkl", "wb")
        pcs = pickle.load(file)
        gestionDatos.setSistemaBecas(pcs)

        file.close()

        file = open("src_py/baseDatos/temp/materias.pkl", "wb")
        pcs = pickle.load(file)
        gestionDatos.setMaterias(pcs)

        file.close()
