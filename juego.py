import requests
import API_request
import json
import abc

class juego(object):
  def __init__(self, name:str, desc:str, rating:str, fecha:str, pictures:list , plataforms: list , devs: list, genres: list,ESRB:str):
    self.name=name
    self.desc=desc
    self.rating=rating
    self.fecha=fecha
    self.pictures=pictures
    self.plataforms=plataforms
    self.devs=devs
    self.genres=genres
    self.ESRB=ESRB or "NOT DEFINED, game too old(?)"

  def __str__(self):
    r=f"\nName: {self.name}\n"
    r+=f"\nDescription:{self.desc}"
    r+=f"\nRating:{self.rating}"
    r+=f"\nRelease date:{self.fecha}"
    r+=f"\nPicture links{self.pictures}"
    r+=f"\nPlataforms: {self.plataforms}"
    r+=f"\ndevelopers: {self.devs}"
    r+=f"\nGenres: {self.genres}"
    r+=f"\nESRB: {self.ESRB}"
    return r


class api_juego():
  @abc.abstractmethod
  def get_juego(self):
    pass

class rawg_juego(api_juego):
  def get_juego(game):
    game=game.replace(" ", "-")
    r=requests.get(f"https://api.rawg.io/api/games/{game}")
    r=json.loads(r.text)
    r=str(r["slug"])
    r=requests.get(f"https://api.rawg.io/api/games/{r}")
    r=json.loads(r.text)
    game=juego(r['name'],r['description'],r['rating'],r['released'],["foto1","foto2"],r['platforms'],r['developers'],r['genres'], r['esrb_rating'])
    return game

if __name__=="__main__":
    jueguito = rawg_juego.get_juego("super-mario-bros")
    print(jueguito)

