import Locations as l

class Ingredient:
    def __init__(self, quantity,name, location, ingredients):
        self.quantity = quantity
        self.name = name
        self.ingredients = ingredients
        self.location = location 

#Base Ingredients
Alcohol = Ingredient(1, "Alcohol", [l.School, l.Hospital], [])
Cloth = Ingredient(1, "Cloth", [l.Alley, l.TownHall, l.Temple, l.Slum], [])
Battery = Ingredient(1, "Battery", [l.FireStation, l.Lighthouse], [])
Fertilizer = Ingredient(1, "Fertilizer", [l.Pond, l.Hotel, l.TownHall], [])
Glue = Ingredient(1, "Glue", [l.Hospital, l.Factory], [])
Gunpowder = Ingredient(1, "Gunpowder", [l.Lighthouse, l.Tunnel, l.ArcheryRange], [])
Gasoline = Ingredient(1, "Gasoline", [l.FireStation, l.ArcheryRange, l.Slum, l.TownHall], [])
IronOre = Ingredient(3, "Iron Ore", [l.Trail, l.Cemetary, l.Forest, l.Lighthouse], [])
Wire = Ingredient(1, "Wire", [l.Tunnel, l.Factory], [])
Leather = Ingredient(1, "Leather", [l.Forest, l.ArcheryRange, l.Temple], [])
Rubber = Ingredient(1, "Rubber", [l.Beach, l.School, l.Cemetary], [])
Bullet = Ingredient(20, "Bullet", [l.Lighthouse, l.Dock, l.Beach, l.Well, l.Random], [])
Arrow = Ingredient(20, "Arrow", [l.TownHall, l.ArcheryRange, l.Cemetary, l.Well, l.Random], [])
ScrapMetal = Ingredient(1, "Scrap Metal", [l.Factory, l.Chapel, l.Slum, l.Beach, l.Alley], [])
Lighter = Ingredient(3, "Lighter", [l.Slum, l.Lighthouse, l.School], [])
ThickPaper = Ingredient(1, "ThinkPaper", [l.Temple, l.ArcheryRange, l.TownHall], [])
LaserPointer = Ingredient(1, "Laser pointer", [l.Factory, l.School], [])
Mithril = Ingredient(1, "Mithril", [l.Random], [])
TurtleShell = Ingredient(1, "Turtle Shell", [l.Pond, l.Beach, l.Well, l.Dock], [])
ArcaneStone = Ingredient(1, "Arcane Stone", [l.Random], [])
HolyBlood = Ingredient(1, "Holy Blood", [l.Random], [])
Meteorite = Ingredient(1, "Meteorite", [l.Random], [])
OgreSkin = Ingredient(1, "Ogre Skin", [l.Random], [])
Feather = Ingredient(1, "Feather", [l.Cemetary, l.Forest, l.ArcheryRange, l.Trail], [])
#Ingredients
Ruby = Ingredient(1, "Ruby", [], [Gemstone, Hammer])
Steel = Ingredient(2, "Steel", [], [IronOre, ScrapMetal])
Oilcloth = Ingredient(1, "Oilcloth", [], [Cloth, Gasoline])
ElectronicParts = Ingredient(1, "Electronic Parts", [], [Wire, Battery])
Ash = Ingredient(1, "Ash", [], [Lighter, ThickPaper])
IronSheet = Ingredient(2, "Iron Sheet", [], [ScrapMetal, Hammer])
Blueprint = Ingredient(1, "Blueprint", [], [ThickPaper ,FountainPen])
Flint = Ingredient(1, "Flint", [], [Gunpowder, Stone])
IonBattery = Ingredient(1, "Ion Battery", [], [Battery, SportsDrink])
GlassPieces = Ingredient(1, "Glass Pieces", [], [GlassCup, Stone])
Lye = Ingredient(1, "Lye", [], [Ash, Water])
GlassPanel = Ingredient(1, "Glass Panel", [], [GlassPieces, Glue])
CRT = Ingredient(1, "CRT", [], [TV, Hammer])
LCDPanel = Ingredient(1, "LCD Panel", [], [GlassPanel, CRT])
CellPhone = Ingredient(1, "Cell Phone", [], [Blueprint, ElectronicParts])
Gold = Ingredient(1, "Gold", [], [Gemstone, Pickaxe])
Adamantium = Ingredient(1, "Adamantium", [], [Mithril, IronOre])
Motor = Ingredient(1, "Motor", [], [Steel, ElectronicParts])
Poison = Ingredient(1, "Poison", [], [Lye, Fertilizer])
WhitePowder = Ingredient(1, "White Powder", [], [WhiteChalk, Stone])
EngineeredArcaneMotor = Ingredient(1, "Engineerd Arcane Motor", [], [Motor, ArcaneStone])
BoilingWater = Ingredient(2, "Boiling Water", [], [Water, Lighter])