import json
from juego import *

class Biblioteca(object):
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.juegos = []

    def addJuego(self, juego: juego):
        self.juegos.append(juego)
    
    def biblio_getjuegos(self):
        lista = []
        for i in self.juegos:
            lista.append(i.get_everything())
        return lista


if __name__ == '__main__':
    rawg =rawg_juego()
    juego = build_juego(rawg,'the legend of zelda ocarina of time')
    juego2 = build_juego(rawg,'gta 5')
    biblio = Biblioteca("Aventura")
    biblio.addJuego(juego)
    biblio.addJuego(juego2)
    print(biblio.biblio_getjuegos())
