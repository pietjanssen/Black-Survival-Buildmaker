import Locations as l

class Ingredient:
    def __init__(self, quantity,name, location, ingredients):
        self.quantity = quantity
        self.name = name
        self.ingredients = ingredients
        self.location = location        

class Enhance:
    def __init__(self, quantity, name, location, ingredients):
        self.quantity = quantity
        self.name = name
        self.ingredients = ingredients
        self.location = location

class HFood:
    def __init__(self, quantity, name, location, ingredients, health):
        self.quantity = quantity
        self.name = name
        self.location = location
        self.ingredients = ingredients
        self.health = health

class SFood:
    def __init__(self, quantity, name, location, ingredients, stamina):
        self.quantity = quantity
        self.name = name
        self.location = location
        self.ingredients = ingredients
        self.stamina = stamina

class Special:
    def __init__(self, quantity, name, location, ingredients):
        self.quantity = quantity
        self.name = name
        self.ingredients = ingredients
        self.location = location

class Weapon:
    def __init__(self, quantity, name, location, ingredients, category, damage):
        self.quantity = quantity
        self.name = name
        self.ingredients = ingredients
        self.location = location
        self.category = category
        self.damage = damage

class Armor:
    def __init__(self, quantity, name, location, ingredients, category, armor):
        self.quantity = quantity
        self.name = name
        self.location = location
        self.ingredients = ingredients
        self.category = category
        self.armor = armor

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
Alcohol = Ingredient(1, "Alcohol", [l.School, l.Hospital], [])
Cloth = Ingredient(1, "Cloth", [l.Alley, l.TownHall, l.Temple, l.Slum], [])
Battery = Ingredient(1, "Battery", [l.FireStation, l.Lighthouse], [])
Fertilizer = Ingredient(1, "Fertilizer", [l.Pond, l.Hotel, l.TownHall], [])
Glue = Ingredient(1, "Glue", [l.Hospital, l.Factory], [])
Gunpowder = Ingredient(1, "Gunpowder", [l.Lighthouse, l.Tunnel, l.ArcheryRange], [])
Gasoline = Ingredient(1, "Gasoline", [l.FireStation, l.ArcheryRange, l.Slum, l.TownHall], [])
Gemstone = Ingredient(1, "Gemstone", [l.Trail, l.Pond, l.Tunnel], [])
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
GlassCup = Ingredient(1, "Glass Cup", [l.Alley, l.Uptown, l.Hotel, l.Slum], [])
OgreSkin = Ingredient(1, "Ogre Skin", [l.Random], [])
Nail = Enhance(1, "Nail", [l.Factory, l.Tunnel], [])
Whetstone = Enhance(1, "Whetstone", [l.Tunnel, l.Uptown, l.Hotel, l.Dock], [])

#List of base HFood
SweetPotato = HFood(1,"Sweet Potato", [l.Hotel], [], 5)
CurryPowder = HFood(1, "Curry Powder", [l.Uptown], [], 5)
SoySauce = HFood(1, "Soy Sauce", [l.Uptown], [], 5)
OrientalGrass = HFood(1, "Oriental grass", [l.Trail, l.Forest], [], 7)
Burdock = HFood(1, "Burdock", [l.Hotel] , [], 10)
ReliefPatch = HFood(1, "Relief Patch", [l.TownHall], [], 10)
Tuna = HFood(1, "Tuna", [l.Dock], [], 10)
Garlic = HFood(1, "Garlic", [l.Hotel], [], 10)
Potato = HFood(1, "Potato", [l.Hotel], [], 10)
Orange = HFood(5, "Orange", [l.Uptown], [], 12)
BandAid = HFood(1, "Band-Aid", [l.Hospital], [], 15)
Cookie = HFood(3, "Cookie", [l.Hotel, l.Random], [], 15)
Antiseptic = HFood(1, "Antiseptic", [l.Hospital], [], 15)
Ramen = HFood(1, "Ramen", [l.Alley, l.Slum], [], 15)
Bread = HFood(2, "Bread", [], [], 20)
Chocolate = HFood(1, "Chocolate", [l.Uptown], [], 20)
Bandage = HFood(2, "Bandage", [l.Hospital], [], 30)
ScorchedRiceSoup = HFood(4, "Scorched Rice Soup", [], [], 40)
Gimbap = HFood(2, "Gimbap", [], [], 70)
FreshSashimi = HFood(1, "Fresh Sashimi", [l.Beach, l.Dock], [], 120)
GrilledEel = HFood(1, "Grilled Eel", [], [], 170)

#List of base SFood
# = SFood(, "", [], [], )
Water  = SFood(3, "Water", [l.Pond, l.FireStation, l.Well, l.Beach, l.Forest, l.Dock, l.Random], [], 10)
Ice = SFood(1, "Ice", [l.Well, l.Hotel], [], 10)
SportsDrink = SFood(1, "Sports Drink", [l.Lighthouse, l.ArcheryRange], [], 10)
CarbonatedWater = SFood(1, "Carbonated Water", [l.Well], [], 13)
TobaccoLeaves = SFood(1, "Tobacco Leaves", [], [], 15)
Coffee = SFood(1, "Coffee", [l.Uptown], [], 20)
LiverSupplementPill = SFood(1, "Liver Supplement Pill", [l.Hospital], [], 20)
Honey = SFood(1, "Honey", [l.TownHall, l.Hotel], [], 22)
Baccus = SFood(1, "Baccus", [l.Slum], [], 25)
TreeOfLife = SFood(1, "Tree of Life", [l.Random], [], 4)

#List of base Weapons
#Blade
# = Weapon(, "", [], [], [], )
Razor = Weapon(1, "Razor", [l.School, l.Hotel], [], [Blade, Stab], 5)
Cutter = Weapon(1, "Cutter", [l.Alley, l.Hotel], [], [Blade, Stab], 5)
Scissors = Weapon(1, "Scissors", [l.Hospital, l.School, l.Alley], [], [Blade], 5)
CrudeAxe = Weapon(1, "Crude Axe", [], [], [Blade], 6)
KitchenKnife = Weapon(1, "Kitchen Knife", [l.Uptown, l.Alley, l.Slum, l.Hotel], [], [Blade, Stab], 8)
Pickaxe = Weapon(1, "Pickaxe", [l.Cemetary, l.Tunnel], [], [Blade], 8)
Sickle = Weapon(1, "Sickle", [l.Lighthouse, l.Forest], [], [Blade], 10)
Knife = Weapon(1, "Knife", [l.Well], [], [Blade, Stab], 10)
Hatchet = Weapon(1, "Hatchet", [l.Forest, l.Trail], [], [Blade], 10)
Shameshir = Weapon(1, "Shameshir", [l.Cemetary, l.Trail], [], [Blade], 12)
LongSword = Weapon(1, "Long Sword", [l.Cemetary, l.Chapel], [], [Blade, Stab], 12)
Katana = Weapon(1, "Katana", [l.Temple, l.Uptown], [], [Blade, Stab], 18)
JewelSword = Weapon(1, "Jewel Sword", [l.Random], [], [Blade, Stab], 20)


#Blunt
ScrollsOfDongYi = Weapon(1, "Scrolls of DongYi", [l.Hospital], [], [Blunt])
Hammer = Weapon(1, "Hammer", [l.FireStation, l.TownHall, l.Dock, l.Hospital], [], [Blunt])
FryingPan = Weapon(1, "Frying Pan", [l.Slum, l.Hotel], [], [Blunt])
Branch = Weapon(1, "Branch", [l.Cemetary, l.Trail, l.Forest], [], Blunt)
#Bow
#Hand
#Gun
#Thrown
TV = Weapon(1, "TV", [l.Alley, l.Slum, l.Uptown, l.TownHall], [], [Thrown])
WhiteChalk = Weapon("White Chalk", [l.SChool], [], [Thrown])
Stone = Weapon("Stone", [l.Tunnel, l.Trail, l.Temple, l.Cemetary, l.Hotel], [], [Thrown])
LaptopBroken = Weapon("Laptop(screen broke)", [l.Uptown, l.Hotel], [], [Thrown])
CookingPot = Weapon("Cooking Pot", [l.Slum, l.Uptown, l.Alley, l.Hotel], [], [Thrown])
HolyGrail = Weapon("Holy Grail", [l.Chapel], [], [Thrown])
GlassBottle = Weapon("Glass Bottle", [l.Tunnel], [], [Thrown])
Carp = Weapon("Carp", [l.Pond], [], [Thrown])
Can = Weapon("Can", [l.Tunnel, l.Beach], [], [Thrown])
Mudfish = Weapon(1, "Mudfish", [l.Pond], [], Thrown)
PlasticBottle = Weapon(1, "Plastic Bottle", [l.Pond], [], Thrown)
#Trap
#Stab
Needle = Weapon("Needle", [l.Alley, l.Slum, l.Uptown], [], [Stab])
FountainPen = Weapon(1, "Fountain Pen", [l.School, l.Hospital], [], Stab)

#List of base armor
#Head
#Clothes
#Arm
#Leg
#Accessory
Flower = Armor(1, "Flower", [l.Pond, l.Cemetary, l.Forest, l.ArcheryRange], [], [Accessory])
Box = Armor(1, "Box", [l.Tunnel, l.School, l.Pond], [], [Accessory])

#List of ingredients
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
Starsteel = Enhance(1, "Enhance", [], [Meteorite, IronOre])
BoilingWater = Ingredient(2, "Boiling Water", [], [Water, Lighter])

#List of weapons
#Stab
#Blade
# = Weapon(, "", [], [], [], )
SharpKitchenKnife = Weapon(1, "Sharp Kitchen Knife", [], [Whetstone, KitchenKnife], [Blade, Stab], 14)
Jamadhar = Weapon(1, "Jamadhar", [], [Knuckle, KitchenKnife], [Blade, Stab], 20)
ChainScythe = Weapon(1, "Chain Scythe", [], [SteelChain, Sickle], [Blade], 26)
AxeChain = Weapon(1, "Axe Chain", [], [SteelChain, Hatchet], [Blade], 26)
BattleAxe = Weapon(1, "Battle Axe", [], [SpearHandle, Hatchet], [Blade], 26)
HeatedWhetstone = Weapon(1, "Heated Whetstone", [], [Lighter, Whetstone], [Thrown])
Sabre = Weapon(1, "Sabre", [], [Shameshir, HeatedWhetstone], [Blade], 28)
Scimitar = Weapon(1, "Scimitar", [], [Shameshir, SharpKitchenKnife], [Blade], 28)
ArmyKnife = Weapon(1, "Army Knife", [], [Knife, Branch], [Blade, Stab], 36)
TwinSword = Weapon(1, "Twin Sword", [], [SharpKitchenKnife, KitchenKnife], [Blade, Stab], 32)
HorseGuandao = Weapon(1, "Horse Guandao", [], [Scimitar, SpearHandle], [Blade], 34)
Masamune = Weapon(1, "Masamune", [l.Temple], [], [Blade, Stab], 34)
ReapersScythe = Weapon(1, "Reaper's Scythe", [], [Sickle, SpearHandle], [Blade], 34)
Odachi = Weapon(1, "Odachi", [], [Katana, IronSheet], [Blade], 34)
Muramasa = Weapon(1, "Muramasa", [l.Random], [], [Blade, Stab], 34)
HalberdAxe = Weapon(1, "Halberd Axe", [], [LongSpear, Hatchet], [Blade, Stab], 34)
BastardSword = Weapon(1, "Bastard Sword", [], [LongSword, Steel], [Blade, Stab], 34)
BeamSabre = Weapon(1, "Beam Sabre", [], [Sabre, LaserPointer], [Blade, Stab], 34)
SwordOfJustice = Weapon(1, "Sword of Justice", [], [StallionMedal, LongSword], [Blade, Stab], 40)
Arondight = Weapon(1, "Arondight", [], [BastardSword, Cross], [Blade, Stab], 40)
Chainsaw = Weapon(1, "Chainsaw", [], [SolderingIron, Battery], [Blade], 40)
FrostWail = Weapon(1, "Frostwail", [], [JewelSword, Ice], [Blade, Stab], 42)
StarSteelTwinSword = Weapon(1, "Starsteel Twin Sword", [], [Starsteel, TwinSword], [Blade, Stab], 42)
Excalibur = Weapon(1, "Excalibur", [], [JewelSword, Cross], [Blade, Stab], 42)
StarsteelClaymore = Weapon(1, "Starsteel Claymore", [], [Starsteel, LongSword], [Blade, Stab], 42)
BeamAxe = Weapon(1, "Beam Axe", [], [BattleAxe, BeamSabre], [Blade], 45)
SwordOfRupture = Weapon(1, "Sword of Rupture", [], [BeamSabre, TreeOfLife], [Blade, Stab], 46)
PulseKnife = Weapon(1, "Pulse Knife", [], [Motor, Knife], [Blade, Stab], 46)
Dainsleif = Weapon(1, "Dáinsleif", [], [HolyBlood, BastardSword], [Blade, Stab], 48)
DivineDualSword = Weapon(1, "Divine Dual Swords", [], [Muramasa, Masamune], [Blade, Stab], 48)
WarpBlade = Weapon(1, "Warp Blade", [], [EngineeredArcaneMotor, LongSword], [Blade, Stab], 48)
SkyPiercer = Weapon(1, "Sky Piercer", [], [HalberdAxe, HorseGuandao], [Blade, Stab], 48)
Monohoshizao = Weapon(1, "Monohoshizao", [], [Odachi, Blueprint], [Blade], 48)
ParallelSword = Weapon(1, "Parallel Sword", [], [BastardSword, Rapier], [Blade, Stab], 48)
Harpe = Weapon(1, "Harpe", [], [Scimitar, JewelSword], [Blade], 48)
SevenStarSword = Weapon(1, "Seven Star Sword", [], [Meteorite, JewelSword], [Blade, Stab], 50)
Winterer = Weapon(1, "Winterer", [], [GlacialIce, JewelSword], [Blade, Stab], 50)
SantaMuerte = Weapon(1, "Santa Muerte", [], [ReapersScythe, Adamantium], [Blade], 50)
DragonGuandao = Weapon(1, "Dragon Guandao", [], [HalberdAxe, TreeOfLife], [Blade], 50)
Laevateinn = Weapon(1, "Laevteinn", [], [TreeSamadhiFire, JewelSword], [Blade, Stab], 50)
AxeOfPangu = Weapon(1, "Axe of Pangu", [], [BattleAxe, Adamantium], [Blade], 50)
PhaseSabre = Weapon(1, "Phase Sabre", [], [ManorizedArms, LaserPointer], [Blade, Stab], 65)
#Blunt
#Bow
#Hand
#Gun
#Thrown
#Trap


#List of armor
#Head
#Clothes
#Arm
#Leg
#Accessory
PowderOfLife = Armor(1, "Powder of Life", [], [TreeOfLife, Stone], [Accessory])


#List of SFood
# = SFood(, "", [], [], )
IceWater = SFood(8, "Ice Water", [], [Ice, Water], 15)
SorghumWine = SFood(1, "Sorghum Wine", [], [Alcohol, Lighter], 30)
WaterBottle = SFood(3, "1.5L Water Bottle", [], [Water, PlasticBottle], 33)
KoaliangLiquor = SFood(4, "Laoliang Liquor", [], [SorghumWine, Lighter], 36)
HalfFilledGlass = SFood(2, "Half-filled Glass", [], [Water, GlassCup], 37)
HoneyWater = SFood(2, "Honey Water", [], [Honey, Water], 42)
Soju = SFood("Soju", [], [Water, Alcohol], 44)
OrientalRaisinWater = SFood(3, "Oriental Raisin Water", [], [Branch, BoilingWater], 46)
HerbalLiquor = SFood(3, "Herbal Liquor", [], [SorghumWine, OrientalGrass], 75)
Whiskey = SFood(1, "Whiskey", [], [], 120)
SparklingSoju = SFood(4, "Sparkling Soju", [], [CarbonatedWater, Soju], 35)
IonizedSoju = SFood(3, "Ionized Soju", [], [SportsDrink, Soju], 40)
PurifiedWater = SFood(4, "Purified Water", [], [BoilingWater, Ice], 40)
HotHoneyWater = SFood(4, "Hot Honey Water", [], [Honey, BoilingWater], 42)
BurdockTea = SFood(3, "Burdock Tea", [], [Burdock, BoilingWater], 45)
OrangeAde = SFood(5, "Orange Ade", [], [Orange, CarbonatedWater], 50)
Americano = SFood(3, "Americano", [], [BoilingWater, Coffee], 55)
HotChocolate = SFood(3, "Hot Chocolate", [], [Chocolate, BoilingWater], 55)
CoffeeLiqueur = SFood(2, "Coffee Liqueur", [], [Alcohol, Coffee], 60)
IceCoffee = SFood(4, "Ice Coffee", [], [Coffee, Ice], 70)
FlowerLiquor = SFood(3, "Flower Liquor", [], [Flower, SorghumWine], 90)
Cigarette = SFood(10, "Cigarette", [], [TobaccoLeaves, Lighter], 54)
Cocktail = SFood(10, "Cocktail", [], [Whiskey, Orange], 90)

CoffeeLiqueur = SFood("Coffee Liqueur", [], [Alcohol, Coffee], 60)

#List of HFood
Pill = HFood(1, "Pill", [l.Hospital], [OrientalGrass, ScrollsOfDongYi], 60)
OrientalConcotion = HFood(3, "Oriental Concotion", [], [OrientalGrass, BoilingWater], 35)
Curry = HFood(6, "Curry", [], [CurryPowder, BoilingWater], 38)
Bungeoppang = HFood(3, "Bungeoppang", [], [Carp, Bread], 48)
HoneyMedicine = HFood(3, "Honey Medicine", [], [Honey, Pill], 48)
HotRamen = HFood(4, "Hot Ramen", [], [Ramen, BoilingWater], 50)
ChocolatePie = HFood(2, "Chocolate Pie", [], [Chocolate, Bread], 60)
Herb = HFood(2, "Herb", [], [OrientalGrass, Flower], 60)
# Problem with this sort of class making bullshit
HerbalTea = SFood(5, "Herbal Tea", [], [Herb, BoilingWater], 30)
TurtleSoup = HFood(2, "Turtle Soup", [], [TurtleShell, CookingPot], 61)
Acupuncture = HFood(3, "Acupuncture", [], [Needle, ScrollsOfDongYi], 65)
FirstAidKit = HFood(2, "First Aid Kit", [], [Box, Pill], 76)
HolyWater = HFood(1, "Holy Water", [l.Chapel], [HolyGrail, Water], 101)
HerbMedicine = HFood(1, "Herb Medicine", [], [TurtleShell, ScrollsOfDongYi], 200)
GarlicBread = HFood(3, "Garlic Bread", [], [Garlic, Bread], 40)
LiquorBread = HFood(2, "Liquor Bread", [], [Soju, Bread], 40)
StirFriedRamen = HFood(5, "Stir Fried Ramen", [], [FryingPan, Ramen], 43)
MudfishSoup = HFood(4, "Mudfish Soup", [], [Mudfish, CookingPot], 50)
BakedMudfish = HFood(3, "Baked Mudfish", [], [Mudfish, HeatedWhetstone], 50)
SpicyNoodle = HFood(5, "SpicyNoodle", [], [Ramen, SoySauce], 54)
HealingPotion = HFood(4, "Healing Potion", [], [Herb, GlassBottle], 55)
MochaBread = HFood(3, "Mocha Bread", [], [CoffeeLiqueur, Bread], 60)
Sashimi = HFood(6, "Sashimi", [], [SharpKitchenKnife, Tuna], 70)
ChocoPieBox = HFood(2, "Choco Pie Box", [], [ChocolatePie, Box], 70)
BakedSweetPotato = HFood(4, "Baked Sweet Potato", [], [SweetPotato, HeatedWhetstone], 70)
ChocolateChipCookie = HFood(3, "Chocolate Chip Cookie", [], [Chocolate, Cookie], 70)
FishStew = HFood(3, "Fish Stew", [], [Carp, CookingPot], 72)
BakedCarp = HFood(2, "Baked Carp", [], [Carp, HeatedWhetstone], 75)
PickledGarlic = HFood(4, "Pickled Garlic", [], [Garlic, SoySauce], 85)
GlazedSweetPotato = HFood(3, "Glazed Sweet Potato", [], [SweetPotato, Honey], 95)
TunaCan = HFood(2, "Tuna Can", [], [Tuna, Can], 110)
BakedPotato = HFood(2, "Baked Potato", [], [Potato, HeatedWhetstone], 120)
BraisedBurdock = HFood(4, "Braised Burdock", [], [Burdock, SoySauce], 70)
GarlicRamen = HFood(3, "Garlic Ramen", [], [HotRamen, Garlic], 80)
BraisedPotato = HFood(3, "Braised Potato", [], [Potato, SoySauce], 90)
TenTonicsSoup = HFood(2, "Ten Tonics Soup", [], [TurtleSoup, ScrollsOfDongYi], 100)
GrilledTuna = HFood(2, "Grilled Tuna", [], [Tuna, HeatedWhetstone], 120)
BullIntestine = HFood(1, "Bull Intestine", [], [], 1111)
PetalDewPill = HFood(3, "Petal Dew Pull", [], [PowderOfLife, Flower], 140)
