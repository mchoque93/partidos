class Programa:
    def __init__(self):
        self.lista_equipos = self.cargar_equipos()
        self.lista_sorteo = self.sorteo()

    def registrar_partido(self, equipo1: str, equipo2: str, goles: tuple):
        partido = self.get_partido(equipo1, equipo2)
        partido.goles = goles
        # partidos jugados
        partido.equipo1.estadisticas.PJ += 1
        partido.equipo2.estadisticas.PJ += 1

        # goles:
        gol_1, gol_2=goles
        # equipo 1
        partido.equipo1.estadisticas.GF += gol_1
        partido.equipo1.estadisticas.GC += gol_2

        # equipo 2
        partido.equipo2.estadisticas.GF += gol_2
        partido.equipo2.estadisticas.GC += gol_1

        if gol_1 == gol_2:
            # partidos empatados (PE)
            partido.equipo1.estadisticas.PE += 1
            partido.equipo2.estadisticas.PE += 1

        elif gol_1 > gol_2:
            # partidos ganados (PG)
            partido.equipo1.estadisticas.PG += 1
            # partidos perdidos (PP)
            partido.equipo2.estadisticas.PP += 1

        else:
            # partidos ganados (PG)
            partido.equipo2.estadisticas.PG += 1
            # partidos perdidos (PP)
            partido.equipo1.estadisticas.PP += 1

    @staticmethod
    def cargar_equipos():
        lista_equipos = []
        f = open("C:/Users/e056701/Desktop/equipos.txt", "r")
        while (True):
            linea = f.readline().rstrip('\n')
            if not linea:
                break
            lista_equipos.append(Equipo(linea))
        f.close()
        return lista_equipos

    def sorteo_old(self):
        lista_sorteo = []
        for x in range(0, len(self.lista_equipos) - 2):
            for y in range(x + 1, len(self.lista_equipos) - 1):
                if x != y:
                    lista_sorteo.append(Partido(self.lista_equipos[x], self.lista_equipos[y]))
        return lista_sorteo

    def sorteo(self):
        lista_sorteo = []
        lista_combinaciones= combinations(self.lista_equipos, 2)
        for combinacion in lista_combinaciones:
            lista_sorteo.append(Partido(*combinacion))
        return lista_sorteo

    def get_partido(self, equipo1: str, equipo2: str):
        return next(partido for partido in self.lista_sorteo if equipo1 in partido and equipo2 in partido)
