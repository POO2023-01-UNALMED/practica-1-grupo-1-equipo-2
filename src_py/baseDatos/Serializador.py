import pickle
from src_py.Calendario.gestionDatos import gestionDatos

class Serializador:
    @classmethod
    def serializador(cls):
        file = open("PYTHON/src/baseDatos/temp/profesores.pkl", "wb")
        pcs = gestionDatos.getProfesores()
        pickle.dump(pcs, file)
        file.close()

        file = open("PYTHON/src/baseDatos/temp/estudiantes.pkl", "wb")
        pcs = gestionDatos.getEstudiantes()
        pickle.dump(pcs, file)
        file.close()


        file = open("PYTHON/src/baseDatos/temp/estimulosEstudiantes.pkl", "wb")
        pcs = gestionDatos.getSistemaBecas()
        pickle.dump(pcs, file)
        file.close()

        file = open("PYTHON/src/baseDatos/temp/cursos.pkl", "wb")
        pcs = gestionDatos.getMaterias()
        pickle.dump(pcs, file)
        file.close()