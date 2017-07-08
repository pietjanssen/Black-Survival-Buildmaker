import Locations as l

class Ingredient:
    def __init__(self, name, ingredients, location):
        self.name = name
        self.ingredients = ingredients
        self.location = location        

class Enhance:
    def __init__(self, name, ingredients, location):
        self.name = name
        self.ingredients = ingredients
        self.location = location

class Special:
    def __init__(self, name, ingredients, location):
        self.name = name
        self.ingredients = ingredients
        self.location = location

class Weapon:
    def __init__(self, name, ingredients, location, category):
        self.name = name
        self.ingredients = ingredients
        self.location = location
        self.category = category

#List of base ingredients (ingredients without requirements)
Alcohol = Ingredient("Alcohol", [l.School, l.Hospital], [])
Bloth = Ingredient("Cloth", [l.Alley, l.TownHall, l.Temple, l.Slum], [])
Battery = Ingredient("Battery", [l.FireStation, l.Lighthouse], [])
Fertilizer = Ingredient("Fertilizer", [l.Pond, l.Hotel, l.TownHall], [])
Glue = Ingredient("Glue", [l.Hospital, l.Factory], [])
Gunpowder = Ingredient("Gunpowder", [l.Lighthouse, l.Tunnel, l.ArcheryRange], [])
Gasoline = Ingredient("Gasoline", [l.FireStation, l.ArcheryRange, l.Slum, l.TownHall], [])
IronOre = Ingredient("Iron Ore", [l.Trail, l.Cemetary, l.Forest, l.Lighthouse], [])
Wire = Ingredient("Wire", [l.Tunnel, l.Factory], [])
Leather = Ingredient("Leather", [l.Forest, l.ArcheryRange, l.Temple], [])
Rubber = Ingredient("Rubber", [l.Beach, l.School, l.Cemetary], [])
Bullet = Ingredient("Bullet", [l.Lighthouse, l.Dock, l.Beach, l.Well, l.Random], [])

adamantium = Ingredient("adamantium", [], [])