import pickle
import os

class Serializador:
    @staticmethod
    def serializar(gestor):
        base_path = os.path.dirname(os.path.abspath(__file__))
        temp_path = os.path.join(base_path, "temp")
        os.makedirs(temp_path, exist_ok=True)  # Create 'temp' directory if it doesn't exist

        est_path = os.path.join(temp_path, "Estudiantes.pkl")
        prof_path = os.path.join(temp_path, "Profesores.pkl")
        mat_path = os.path.join(temp_path, "Materias.pkl")
        beca_path = os.path.join(temp_path, "Beca.pkl")

        Serializador.serializarEstudiantes(gestor, est_path)
        Serializador.serializarProfesores(gestor, prof_path)
        Serializador.serializarMaterias(gestor, mat_path)
        Serializador.serializarBeca(gestor, beca_path)
    @staticmethod
    def serializarEstudiantes(gestor, ruta):
        try:
            with open(ruta, "wb") as file:
                pickle.dump(gestor.getEstudiantes(), file)
        except FileNotFoundError as e:
            print("Error en la serialización:", e)

    @staticmethod
    def serializarProfesores(gestor, ruta):
        try:
            with open(ruta, "wb") as file:
                pickle.dump(gestor.getProfesores(), file)
        except FileNotFoundError as e:
            print("Error en la serialización:", e)

    @staticmethod
    def serializarMaterias(gestor, ruta):
        try:
            with open(ruta, "wb") as file:
                pickle.dump(gestor.getMaterias(), file)
        except FileNotFoundError as e:
            print("Error en la serialización:", e)

    @staticmethod
    def serializarBeca(gestor, ruta):
        try:
            with open(ruta, "wb") as file:
                pickle.dump(gestor.getSistemaBecas(), file)
        except FileNotFoundError as e:
            print("Error en la serialización:", e)
