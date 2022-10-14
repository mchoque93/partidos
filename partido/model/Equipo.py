class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estadisticas = Estadistica()

    def __repr__(self):
        return f"{self.nombre}"
