class oppskrift:
    def __init__(self, id=0, tittel="", beskrivelse="", ingredienser=[]):
        self.id = id
        self.tittel = tittel
        self.beskrivelse = beskrivelse
        self.ingredienser = ingredienser

class ingrediens:
    def __init__(self, id=0, tittel="", mengde=0, naering=[""]):
        self.id = id
        self.tittel = tittel
        self.mengde = mengde
        self.naering = naering

ingredienser = []
ingredienser.append(ingrediens(2,"ost",25,["d-vitaminer", "fett"]))
ingredienser.append(ingrediens(0,"kylling",205,["proteiner", "litt fett"]))
ingredienser.append(ingrediens(1,"pasta",250,["carbs", "fiber"]))

#print(ingredienser[0].mengde)

#ost = ingrediens(0,"ost",25,["proteiner", "fett"])

enoppskrift = oppskrift(0, "kyllingpasta", "et veldig digg måltid med masse proteiner og carbs", 
                        ingredienser=[
                             1, 
                            2, 
                            0, 
                            ])

#print(next((x for x in ingredienser if x.id == 1), None).tittel)

