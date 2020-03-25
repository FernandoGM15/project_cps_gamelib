import json
class Biblioteca(object):
    def __init__(self):
        self.juegos = []
    
    def AddJuego(self, juego:dict):
        self.juegos.append(juego)
    
    def RemoveJuego(self,juego):
        pass

    def __str__(self):
        return json.dumps(self.juegos,indent=0,ensure_ascii=False)
class main():
    juego = {
    "name":"Grand Theft Auto V",
    "description":"Rockstar Games went bigger, since their previous installment of the series. You get the complicated and realistic world-building from Liberty City of GTA4 in the setting of lively and diverse Los Santos, from an old fan favorite GTA San Andreas. 561 different vehicles (including every transport you can operate) and the amount is rising with every update. \r\nSimultaneous storytelling from three unique perspectives: \r\nFollow Michael, ex-criminal living his life of leisure away from the past, Franklin, a kid that seeks the better future, and Trevor, the exact past Michael is trying to run away from. \r\nGTA Online will provide a lot of additional challenge even for the experienced players, coming fresh from the story mode. Now you will have other players around that can help you just as likely as ruin your mission. Every GTA mechanic up to date can be experienced by players through the unique customizable character, and community content paired with the leveling system tends to keep everyone busy and engaged.",
    "rating":4.58
    }
    juego2 = {
    "name":"The legend of Zelda: Ocarina of time",
    "description":"The Legend of Zelda™: Ocarina of Time™ – one of the most critically\nacclaimed games ever made –returns on the Nintendo eShop for Wii U™. Set\noff on a legendary journey to stop Ganondorf, who has plunged Hyrule\ninto darkness. Travel through time as child and adult Link™ and\nexperience Hyrule in peace and war to save the world and protect the\nTriforce.\n\nYour quest takes you through dense forests and across wind-whipped\ndeserts. Swim raging rivers, climb treacherous mountains, dash on\nhorseback across rolling hills, and delve into dungeons full of\ncreatures that fight to the finish to put an end to your adventures. As\nLink, you'll also travel through time to solve puzzles, save friends,\nand right Ganondorf's wrongs with the help from your trusty Ocarina of\nTime and the mysterious youth, Sheik. The Legend of Zelda: Ocarina of\nTime is one of Nintendo's most epic challenges ever and one of its most\ntouching stories, and is an absolute must-play for Nintendo fans.\nThis classic game is part of the Virtual Console service, which brings you great games created for consoles such as NES™, Super NES™ and Game Boy™ Advance. We hope you'll enjoy the new features (including off-TV play) that have been added to this title. See more Virtual Console games for Wii U.",
    "rating":4.35
    }
    add = Biblioteca()
    add.AddJuego(juego)
    add.AddJuego(juego2)
    print (add)