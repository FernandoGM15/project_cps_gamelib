import requests
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
    self.ESRB=ESRB

  def __str__(self):
    r=f"\nName: {self.name}\n"
    r+=f"Description:{self.desc}"
    r+=f"Rating:{self.rating}"
    r+=f"Release date:{self.fecha}"
    r+=f""


def get_juego(game: str):
    game=game.replace(" ", "-")
    r=requests.get(f"https://api.rawg.io/api/games/{game}")
    r=json.loads(r.text)
    r=str(r["slug"])
    r=requests.get(f"https://api.rawg.io/api/games/{r}")
    r=json.loads(r.text)
    return(r)

if __name__=="__main__":
  r=get_juego("super-mario-bros")
  print(r["description_raw"])
