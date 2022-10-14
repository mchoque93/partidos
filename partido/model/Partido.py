class Partido:
    def __init__(self, equipo1: "Equipo", equipo2: "Equipo"):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.goles = 0

    def __repr__(self):
        return f"Partido (equipo1:{self.equipo1} equipo2 {self.equipo2})"

    def __contains__(self, item: str):
        return self.equipo1.nombre == item or self.equipo2.nombre == item
