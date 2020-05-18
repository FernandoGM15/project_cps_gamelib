from abc import abstractmethod, ABCMeta
import requests
import json
import sqlite3
from juego import *

class DataBase(metaclass=ABCMeta):
    @abstractmethod
    def Add_juego(self):
        pass
    
    @abstractmethod
    def Create_Biblio(self):
        pass


class DB_Biblioteca(DataBase):
    def __init__(self):
        self.conexion = sqlite3.connect("Bibliotecas.db")
        self.cursor = self.conexion.cursor()

    def Create_Biblio(self, nombre):
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {nombre} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCAHR(50),
                description  VARCHAR(1500),
                rating FLOAT,
                release VARCHAR (20),
                picture VARCHAR (50),
                platforms VARCHAR (50),
                developers VARCHAR (50),
                genre VARCHAR(50),
                esrb VARCHAR(30)
            )
        ''')
    
    def Add_juego(self, juego: dict, nombre: str):
        self.cursor.execute(f'''
        INSERT INTO {nombre} (name, description, rating, release, picture, platforms, developers, genre, esrb) 
        VALUES ("{juego.get('name')}", "{juego.get('desc')}", {juego.get("rating")},"{juego.get("fecha")}","{juego.get('picture')}","{juego.get('platforms')}","{juego.get('devs')}","{juego.get('genres')}","{juego.get('esrb')}");
        ''')
        self.conexion.commit()

if __name__ == '__main__':
    db = DB_Biblioteca()
    db.Create_Biblio("Accion")
    rawg=rawg_juego()
    juego = build_juego(rawg,'the legend of zelda ocarina of time')
    db.Add_juego(juego.get_everything(),"Accion")
    