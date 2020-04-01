from abc import abstractmethod, ABCMeta
@abstractmethod
class DataBase_biblio(metaclass=ABCMeta):
    def create_biblioteca(self, nombre:str, juegos:dict):
        pass

    def get_biblioteca(self, nombre:str):
        pass

    def remove_biblioteca(self, name:str):
        pass

    def Remove_juego(self,nombre_biblio:str, nombre_juego:str):
        pass

    def Add_juego(self, nombre_biblio:str,**args):
        pass