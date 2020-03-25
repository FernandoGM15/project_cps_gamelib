import requests
import json

class juego(object):
  def __init__(self, name:str, desc:str, rating:str, fecha:str, pictures:list , plataforms: list , devs: list, genres: list,ESRB:str):
    self.name=name
    self.desc=desc
    self.rating=rating


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
