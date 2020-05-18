import requests
import json
from abc import *

class juego(object):
  def __init__(self, name:str, desc:str, rating:str, fecha:str, pictures:list , platforms: list , devs: list, genres: list,ESRB:list):
    self.name=name
    self.desc=desc
    self.rating=rating
    self.fecha=fecha
    self.pictures=pictures
    self.platforms=platforms
    self.devs=devs
    self.genres=genres
    self.ESRB=ESRB or "NOT DEFINED, game too old(?)"
  
  def get_name(self):
    return self.name
  
  def get_desc(self):
    return self.desc
  
  def get_everything(self):
    juego = {
      'name': self.name,
      'desc': self.desc,
      'rating': self.rating,
      'fecha': self.fecha,
      'picture': self.pictures,
      'platforms': self.platforms,
      'devs': self.devs,
      'genres': self.genres,
      'esrb': self.ESRB
    }
    return juego
  
  def __str__(self):
    r=f"\nName: {self.name}\n"
    r+=f"\nDescription: {self.desc}"
    r+=f"\nRating: {self.rating}"
    r+=f"\nRelease date: {self.fecha}"
    r+=f"\nPicture links: {self.pictures}"
    r+=f"\nPlatforms: {self.platforms}"
    r+=f"\nevelopers: {self.devs}"
    r+=f"\nGenres: {self.genres}"
    r+=f"\nESRB: {self.ESRB}"
    return r

class api_juego(metaclass= ABCMeta):
  @abstractmethod
  def get_juego(self):
    pass

class rawg_juego(api_juego):
  def __init__(self):
    self.url='https://api.rawg.io/api/games/'

  def get_juego(self,game):
    game=game.replace(" ", "-")
    r=requests.get(f"{self.url}{game}")
    r=json.loads(r.text)
    r=str(r["slug"])
    r=requests.get(f"{self.url}{r}")
    r=json.loads(r.text)
    game=juego(r['name'],r['description_raw'],r['rating'],r['released'],r["background_image"],[i.get("platform",{}).get("name") for i in r['platforms']],[i.get("name") for i in r['developers']],[i.get("name",{}) for i in r['genres']], r['esrb_rating'].get("name"))
    return game

def build_juego(api, game):
  juego = api.get_juego(game)
  return juego

if __name__ == '__main__':
  rawg=rawg_juego()
  print(build_juego(rawg,'the legend of zelda ocarina of time'))