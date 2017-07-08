import Locations as l

class Ingredient:
    def __init__(self, name, location, ingredients):
        self.name = name
        self.ingredients = ingredients
        self.location = location        

class Enhance:
    def __init__(self, name, location, ingredients):
        self.name = name
        self.ingredients = ingredients
        self.location = location

class HFood:
    def __init__(self, name, location, ingredients, health):
        self.name = name
        self.location = location
        self.ingredients = ingredients
        self.health = health

class SFood:
    def __init__(self, name, location, ingredients, stamina):
        self.name = name
        self.location = location
        self.ingredients = ingredients
        self.stamina = stamina

class Special:
    def __init__(self, name, location, ingredients):
        self.name = name
        self.ingredients = ingredients
        self.location = location

class Weapon:
    def __init__(self, name, location, ingredients, category):
        self.name = name
        self.ingredients = ingredients
        self.location = location
        self.category = category

class Armor:
    def __init__(self, name, location, ingredients, category):
        self.name = name
        self.location = location
        self.ingredients = ingredients
        self.category = category

class Category:
    def __init__(self, name):
        self.name = name

#List of Weapon categories
Blade = Category("Blade")
Blunt = Category("Blunt")
Bow = Category("Bow")
Hand = Category("Hand")
Gun = Category("Gun")
Thrown = Category("Thrown")
Trap = Category("Trap")
Stab = Category("Stab")
Head = Category("Head")
Clothes = Category("Clothes")
Arm = Category("Arm")
Leg = Category("Leg")
Accessory = Category("Accessory")

#List of base ingredients (ingredients without requirements)
Alcohol = Ingredient("Alcohol", [l.School, l.Hospital], [])
Cloth = Ingredient("Cloth", [l.Alley, l.TownHall, l.Temple, l.Slum], [])
Battery = Ingredient("Battery", [l.FireStation, l.Lighthouse], [])
Fertilizer = Ingredient("Fertilizer", [l.Pond, l.Hotel, l.TownHall], [])
Glue = Ingredient("Glue", [l.Hospital, l.Factory], [])
Gunpowder = Ingredient("Gunpowder", [l.Lighthouse, l.Tunnel, l.ArcheryRange], [])
Gasoline = Ingredient("Gasoline", [l.FireStation, l.ArcheryRange, l.Slum, l.TownHall], [])
Gemstone = Ingredient("Gemstone", [l.Trail, l.Pond, l.Tunnel], [])
IronOre = Ingredient("Iron Ore", [l.Trail, l.Cemetary, l.Forest, l.Lighthouse], [])
Wire = Ingredient("Wire", [l.Tunnel, l.Factory], [])
Leather = Ingredient("Leather", [l.Forest, l.ArcheryRange, l.Temple], [])
Rubber = Ingredient("Rubber", [l.Beach, l.School, l.Cemetary], [])
Bullet = Ingredient("Bullet", [l.Lighthouse, l.Dock, l.Beach, l.Well, l.Random], [])
Arrow = Ingredient("Arrow", [l.TownHall, l.ArcheryRange, l.Cemetary, l.Well, l.Random], [])
ScrapMetal = Ingredient("Scrap Metal", [l.Factory, l.Chapel, l.Slum, l.Beach, l.Alley], [])
Lighter = Ingredient("Lighter", [l.Slum, l.Lighthouse, l.School], [])
ThickPaper = Ingredient("ThinkPaper", [l.Temple, l.ArcheryRange, l.TownHall], [])
LaserPointer = Ingredient("Laser pointer", [l.Factory, l.School], [])
Mithril = Ingredient("Mithril", [l.Random], [])
TurtleShell = Ingredient("Turtle Shell", [l.Pond, l.Beach, l.Well, l.Dock], [])
ArcaneStone = Ingredient("Arcane Stone", [l.Random], [])
HolyBlood = Ingredient("Holy Blood", [l.Random], [])
Hammer = Ingredient("Hammer", [l.FireStation, l.TownHall, l.Dock, l.Hospital], [])
FountainPen = Ingredient("Fountain Pen", [l.School, l.Hospital], [])
Meteorite = Ingredient("Meteorite", [l.Random], [])
SportsDrink = Ingredient("Sports Drink", [l.Lighthouse, l.ArcheryRange], [])
GlassCup = Ingredient("Glass Cup", [l.Alley, l.Uptown, l.Hotel, l.Slum], [])
OgreSkin = Ingredient("Ogre Skin", [l.Random], [])
Nail = Enhance("Nail", [l.Factory, l.Tunnel], [])
Whetstone = Enhance("Whetstone", [l.Tunnel, l.Uptown, l.Hotel, l.Dock], [])

#List of base HFood
SweetPotato = HFood("Sweet Potato", [l.Hotel], [], 5)
CurryPowder = HFood("Curry Powder", [l.Uptown], [], 5)
SoySauce = HFood("Soy Sauce", [l.Uptown], [], 5)
OrientalGrass = HFood("Oriental grass", [l.Trail, l.Forest], [], 7)
Burdock = HFood("Burdock", [l.Hotel] , [], 10)
ReliefPatch = HFood("Relief Patch", [l.TownHall], [], 10)
Tuna = HFood("Tuna", [l.Dock], [], 10)
Garlic = HFood("Garlic", [l.Hotel], [], 10)
Potato = HFood("Potato", [l.Hotel], [], 10)
Orange = HFood("Orange", [l.Uptown], [], 12)
BandAid = HFood("Band-Aid", [l.Hospital], [], 15)
Cookie = HFood("Cookie", [l.Hotel, l.Random], [], 15)
Antiseptic = HFood("Antiseptic", [l.Hospital], [], 15)
Ramen = HFood("Ramen", [l.Alley, l.Slum], [], 15)
Bread = HFood("Bread", [], [], 20)
Chocolate = HFood("Chocolate", [l.Uptown], [], 20)
Bandage = HFood("Bandage", [l.Hospital], [], 30)
ScorchedRiceSoup = HFood("Scorched Rice Soup", [], [], 40)
Gimbap = HFood("Gimbap", [], [], 70)
FreshSashimi = HFood("Fresh Sashimi", [l.Beach, l.Dock], [], 120)
GrilledEel = HFood("Grilled Eel", [], [], 170)


#Lit of base SFood
Water  = SFood("Water", [l.Pond, l.FireStation, l.Well, l.Beach, l.Forest, l.Dock, l.Random], [], 10)
Honey = SFood("Honey", [l.TownHall, l.Hotel], [], 22)
Coffee = SFood("Coffee", [l.Uptown], [], 20)

#List of base Weapons
#Blade
Pickaxe = Weapon("Pickaxe", [l.Cemetary, l.Tunnel], [], [Blade])
KitchenKnife = Weapon("Kitchen Knife", [l.Uptown, l.Alley, l.Slum, l.hotel], [], [Blade, Stab])
#Blunt
ScrollsOfDongYi = Weapon("Scrolls of DongYi", [l.Hospital], [], [Blunt])
Hammer = Weapon("Hammer", [l.FireStation, l.TownHall, l.Dock, l.Hospital], [], [Blunt])
FryingPan = Weapon("Frying Pan", [l.Slum, l.Hotel], [], [Blunt])
#Bow
#Hand
#Gun
#Thrown
TV = Weapon("TV", [l.Alley, l.Slum, l.Uptown, l.TownHall], [], [Thrown])
WhiteChalk = Weapon("White Chalk", [l.SChool], [], [Thrown])
Stone = Weapon("Stone", [l.Tunnel, l.Trail, l.Temple, l.Cemetary, l.Hotel], [], [Thrown])
LaptopBroken = Weapon("Laptop(screen broke)", [l.Uptown, l.Hotel], [], [Thrown])
CookingPot = Weapon("Cooking Pot", [l.Slum, l.Uptown, l.Alley, l.Hotel], [], [Thrown])
HolyGrail = Weapon("Holy Grail", [l.Chapel], [], [Thrown])
GlassBottle = Weapon("Glass Bottle", [l.Tunnel], [], [Thrown])
#Trap
#Stab
Needle = Weapon("Needle", [l.Alley, l.Slum, l.Uptown], [], [Stab])

#List of base armor
#Head
#Clothes
#Arm
#Leg
#Accessory
Flower = Armor("Flower", [l.Pond, l.Cemetary, l.Forest, l.ArcheryRange], [], [Accessory])
Box = Armor("Box", [l.Tunnel, l.School, l.Pond], [], [Accessory])

#List of ingredients
Ruby = Ingredient("Ruby", [], [Gemstone, Hammer])
Steel = Ingredient("Steel", [], [IronOre, ScrapMetal])
Oilcloth = Ingredient("Oilcloth", [], [Cloth, Gasoline])
ElectronicParts = Ingredient("Electronic Parts", [], [Wire, Battery])
Ash = Ingredient("Ash", [], [Lighter, ThickPaper])
IronSheet = Ingredient("Iron Sheet", [], [ScrapMetal, Hammer])
Blueprint = Ingredient("Blueprint", [], [ThickPaper ,FountainPen])
Flint = Ingredient("Flint", [], [Gunpowder, Stone])
IonBattery = Ingredient("Battery", [], [Battery, SportsDrink])
GlassPieces = Ingredient("Glass Pieces", [], [GlassCup, Stone])
Lye = Ingredient("Lye", [], [Ash, Water])
GlassPanel = Ingredient("Glass Panel", [], [GlassPieces, Glue])
CRT = Ingredient("CRT", [], [TV, Hammer])
LCDPanel = Ingredient("LCD Panel", [], [GlassPanel, CRT])
CellPhone = Ingredient("Cell Phone", [], [Blueprint, ElectronicParts])
Gold = Ingredient("Gold", [], [Gemstone, Pickaxe])
Adamantium = Ingredient("Adamantium", [], [Mithril, IronOre])
Motor = Ingredient("Motor", [], [Steel, ElectronicParts])
Poison = Ingredient("Poison", [], [Lye, Fertilizer])
WhitePowder = Ingredient("White Powder", [], [WhiteChalk, Stone])
EngineeredArcaneMotor = Ingredient("Engineerd Arcane Motor", [], [Motor, ArcaneStone])
Starsteel = Enhance("Enhance", [], [Meteorite, IronOre])
BoilingWater = Ingredient("Boiling Water", [], [Water, Lighter])

#List of weapons
#Blade
SharpKitchenKnife = Weapon("Sharp Kitchen Knife", [], [Whetstone, KitchenKnife], [Blade, Stab])
#Blunt
#Bow
#Hand
#Gun
#Thrown
#Trap
#Stab


#List of SFood
Soju = SFood("Soju", [], [Water, Alcohol], 44)
CoffeeLiqueur = SFood("Coffee Liqueur", [], [Alcohol, Coffee], 60)

#List of HFood
Pill = HFood("Pill", [l.Hospital], [OrientalGrass, ScrollsOfDongYi], 60)
OrientalConcotion = HFood("Oriental Concotion", [], [OrientalGrass, BoilingWater], 35)
Curry = HFood("Curry", [], [CurryPowder, BoilingWater], 38)
Bungeoppang = HFood("Bungeoppang", [], [Carp, Bread], 48)
HoneyMedicine = HFood("Honey Medicine", [], [Honey, Pill], 48)
HotRamen = HFood("Hot Ramen", [], [Ramen, BoilingWater], 50)
ChocolatePie = HFood("Chocolate Pie", [], [Chocolate, Bread], 60)
Herb = HFood("Herb", [], [OrientalGrass, Flower], 60)
TurtleSoup = HFood("Turtle Soup", [], [TurtleShell, CookingPot], 61)
Acupuncture = HFood("Acupuncture", [], [Needle, ScrollsOfDongYi], 65)
FirstAidKit = HFood("First Aid Kit", [], [Box, Pill], 76)
HolyWater = HFood("Holy Water", [l.Chapel], [HolyGrail, Water], 101)
HerbMedicine = HFood("Herb Medicine", [], [TurtleShell, ScrollsOfDongYi], 200)
GarlicBread = HFood("Garlic Bread", [], [Garlic, Bread], 40)
LiquorBread = HFood("Liquor Bread", [], [Soju, Bread], 40)
StirFriedRamen = HFood("Stir Fried Ramen", [], [FryingPan, Ramen], 43)
HealingPotion = HFood("Healing Potion", [], [Herb, GlassBottle], 55)
MochaBread = HFood("Mocha Bread", [], [CoffeeLiqueur, Bread], 60)
Sashimi = HFood("Sashimi", [], [SharpKitchenKnife, Tuna], 70)
