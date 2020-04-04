import requests
import json
from rawg_api import rawg

class juego(rawg):
    def __init__(self, name:str):
        self.name = name
        self.desc = ""
        self.rating = ""
        self.fecha = ""
        self.pictures=""
        self.plataforms=""
        self.devs=""
        self.genres=""
        self.ESRB=""

    # def get_juego(self,api):
    #     self.name=self.name.replace(" ", "-")
    #     r=requests.get(f"{api}/{self.name}")
    #     r=json.loads(r.text)
    #     r=str(r["slug"])
    #     r=requests.get(f"{api}/{r}")
    #     r=json.loads(r.text)
    #     self.name = r['name']
    #     self.desc = r['description']
    #     self.rating = r['rating']
    #     self.fecha = r['released']
    #     self.pictures=r['background_image']
    #     self.plataforms=r['platforms']
    #     self.devs=r['developers']
    #     self.genres=r['genres']
    #     self.ESRB=r['esrb_rating']

    def Datos(self):
        Datos = rawg(self.name)
        return Datos.get_juego()

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



if __name__=="__main__":
    juego1 = juego("super-mario-bros")
    print(juego1.Datos())