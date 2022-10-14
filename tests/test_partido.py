from unittest import TestCase
from partido.partido import *

class TestValidarTarea(TestCase):
    def test_validar_carga_equipos(self):
        programa1 = Programa.cargar_equipos()
        assert programa1[0].nombre=='Real Madrid'

    def test_validar_sorteo(self):
        programa1 = Programa()
        lista_sorteo=programa1.lista_sorteo
        lista_equipos=programa1.lista_equipos
        if any([partido.equipo1==partido.equipo2 for partido in lista_sorteo]):
            raise ValueError("el sorteo está mal hecho")
        #if not all([equipo in set([partido.equipo1 for partido in lista_sorteo]+[partido.equipo2 for partido in lista_sorteo]) for equipo in lista_equipos] ):
        #    raise ValueError("no todos los partidos han entrado en el sorteo")

        a = [(partido.equipo1, partido.equipo2) for partido in programa1.lista_sorteo]
        b = [set(a) for a in a]
        for i in range(0, len(b) - 1):
            for j in range(1, len(b) - 2):
                if i != j:
                    if b[i] == b[j]:
                        raise ValueError(f"oye{i}{j}")


    def test_validar_goles(self):
        programa1 = Programa()
        programa1.registrar_partido("Real Madrid", "Barcelona", (3,0))
        assert programa1.get_partido("Real Madrid", "Barcelona").equipo1.estadisticas.PJ==1
        assert programa1.get_partido("Real Madrid", "Barcelona").equipo2.estadisticas.PJ==1
        assert programa1.get_partido("Real Madrid", "Barcelona").equipo2.estadisticas.PP==1
        assert programa1.get_partido("Real Madrid", "Barcelona").equipo1.estadisticas.PG==1
        assert programa1.get_partido("Real Madrid", "Barcelona").equipo1.estadisticas.GF==3
        assert programa1.get_partido("Real Madrid", "Barcelona").equipo1.estadisticas.GC==0





