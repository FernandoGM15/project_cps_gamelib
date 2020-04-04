from API_request import API_request
import requests
import json
class rawg(API_request):
  def __init__(self, name:str):
    self.name = name

  def get_juego(self):
    self.name=self.name.replace(" ", "-")
    r=requests.get(f"https://api.rawg.io/api/games/{self.name}")
    r=json.loads(r.text)
    r=str(r["slug"])
    r=requests.get(f"https://api.rawg.io/api/games/{r}")
    r=json.loads(r.text)
    dato=f"\nName: {r['name']}\n"
    dato+=f"\nDescription:{r['description']}"
    dato+=f"\nRating:{r['rating']}"
    dato+=f"\nRelease date:{r['released']}"
    dato+=f"\nPicture links{r['background_image']}"
    dato+=f"\nPlataforms: {r['platforms']}"
    dato+=f"\ndevelopers: {r['developers']}"
    dato+=f"\nGenres: {r['genres']}"
    dato+=f"\nESRB: {r['esrb_rating']}"
    return dato