import pickle
import os

class Deserializador:
    @staticmethod
    def deserializar(gestor):
        base_path = os.path.dirname(os.path.abspath(__file__))
        temp_path = os.path.join(base_path, "temp")
        os.makedirs(temp_path, exist_ok=True)  # Create 'temp' directory if it doesn't exist

        est_path = os.path.join(temp_path, "Estudiantes.pkl")
        prof_path = os.path.join(temp_path, "Profesores.pkl")
        mat_path = os.path.join(temp_path, "Materias.pkl")
        beca_path = os.path.join(temp_path, "Beca.pkl")

        Deserializador.deserializarEstudiantes(gestor, est_path)
        Deserializador.deserializarProfesores(gestor, prof_path)
        Deserializador.deserializarMaterias(gestor, mat_path)
        Deserializador.deserializarBeca(gestor, beca_path)
    @staticmethod
    def deserializarEstudiantes(gestor, ruta):
        try:
            with open(ruta, "rb") as file:
                gestor.setEstudiantes(pickle.load(file))
        except FileNotFoundError as e:
            print("Error en la deserialización:", e)

    @staticmethod
    def deserializarProfesores(gestor, ruta):
        try:
            with open(ruta, "rb") as file:
                gestor.setProfesores(pickle.load(file))
        except FileNotFoundError as e:
            print("Error en la deserialización:", e)

    @staticmethod
    def deserializarMaterias(gestor, ruta):
        try:
            with open(ruta, "rb") as file:
                gestor.setMaterias(pickle.load(file))
        except FileNotFoundError as e:
            print("Error en la deserialización:", e)

    @staticmethod
    def deserializarBeca(gestor, ruta):
        try:
            with open(ruta, "rb") as file:
                gestor.setSistemaBecas(pickle.load(file))
        except FileNotFoundError as e:
            print("Error en la deserialización:", e)
