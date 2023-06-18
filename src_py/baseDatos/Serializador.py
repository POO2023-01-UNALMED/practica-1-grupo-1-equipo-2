import pickle
from src_py.Calendario.gestionDatos import gestionDatos

class Serializador:
    @classmethod
    def serializador(cls):
        file = open("src_py/baseDatos/temp/profesores.pkl", "wb")
        pcs = gestionDatos.getProfesores()
        pickle.dump(pcs, file)
        file.close()

        file = open("src_py/baseDatos/temp/estudiantes.pkl", "wb")
        pcs = gestionDatos.getEstudiantes()
        pickle.dump(pcs, file)
        file.close()


        file = open("src_py/baseDatos/temp/becas.pkl", "wb")
        pcs = gestionDatos.getSistemaBecas()
        pickle.dump(pcs, file)
        file.close()

        file = open("src_py/baseDatos/temp/materias.pkl", "wb")
        pcs = gestionDatos.getMaterias()
        pickle.dump(pcs, file)
        file.close()