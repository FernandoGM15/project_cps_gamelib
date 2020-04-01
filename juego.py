import requests
import API_request
import json
from abc import ABCMeta, abstractmethod


class juego(object):
      # def __init__(self, name:str, desc:str, rating:str, fecha:str, pictures:list , plataforms: list , devs: list, genres: list,ESRB:str):
  #   self.name=name
  #   self.desc=desc
  #   self.rating=rating
  #   self.fecha=fecha
  #   self.pictures=pictures
  #   self.plataforms=plataforms
  #   self.devs=devs
  #   self.genres=genres
  #   self.ESRB=ESRB

  def __str__(self):
    r=f"\nName: {self.name}\n"
    r+=f"Description:{self.desc}"
    r+=f"Rating:{self.rating}"
    r+=f"Release date:{self.fecha}"
    r+=f"Picture links{self.pictures}"


  def get_juego(self,game):
    game=game.replace(" ", "-")
    r=requests.get(f"https://api.rawg.io/api/games/{game}")
    r=json.loads(r.text)
    r=str(r["slug"])
    r=requests.get(f"https://api.rawg.io/api/games/{r}")
    r=json.loads(r.text)
    return(f"Nombre: {r['name']}\nDescripcion: {r['description']}\nRating: {r['rating']}\nFecha de lanzamiento: {r['released']}\nPlataformas: {r['platforms']}\nDesarrolladores: {r['developers']}\nGeneros: {r['genres']}\nESRB: {r['esrb_rating']}")

if __name__=="__main__":
    juego = juego()
    print(juego.get_juego("super mario bros"))

