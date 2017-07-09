import Locations as l

class Ingredient:
    def __init__(self, quantity,name, location, ingredients):
        self.quantity = quantity
        self.name = name
        self.ingredients = ingredients
        self.location = location 

#Base Ingredients
Nail = Enhance(1, "Nail", [l.Factory, l.Tunnel], [])
Whetstone = Enhance(1, "Whetstone", [l.Tunnel, l.Uptown, l.Hotel, l.Dock], [])
#Ingredients
Starsteel = Enhance(1, "Enhance", [], [Meteorite, IronOre])