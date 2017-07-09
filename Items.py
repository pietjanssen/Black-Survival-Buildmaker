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
Nail = Enhance(1, "Nail", [l.Factory, l.Tunnel], [])
Whetstone = Enhance(1, "Whetstone", [l.Tunnel, l.Uptown, l.Hotel, l.Dock], [])
Feather = Ingredient(1, "Feather", [l.Cemetary, l.Forest, l.ArcheryRange, l.Trail], [])

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
BuddhistScripture = Weapon(1, "Buddhist Scripture", [l.Temple], [], [Blunt], 5)
Fan = Weapon(1, "Fan", [l.TownHall], [], [Blunt], 5)
RippedScroll1 = Weapon(1, "Ripped Scroll -1", [l.Slum], [], [Blunt], 5)
RippedScroll2 = Weapon(1, "Ripped Scroll -2", [l.Hotel], [], [Blunt], 5)
Scarf = Weapon(1, "Scarf", [l.Trail], [], [Blunt], 5)
AnatomyModel = Weapon(1, "Anatomy Model", [l.Hospital, l.School], [], [Blunt], 5)
Branch = Weapon(1, "Branch", [l.Cemetary, l.Trail, l.Forest], [], [Blunt], 5)
ScrollsOfDongYi = Weapon(1, "Scrolls of DongYi", [l.Hospital], [], [Blunt], 5)
CrudeBat = Weapon(1, "Crude Bat", [], [], [Blunt], 5)
ShortRod = Weapon(1, "Short Rod", [l.Chapel, l.Pond], [], [Blunt], 6)
Bamboo = Weapon(1, "Bamboo", [l.Cemetary, l.Forest, l.Trail], [], [Blunt], 8)
PianoWire = Weapon(1, "Piano Wire", [l.ArcheryRange, l.Cemetary, l.FireStation, l.TownHall], [], [Trap], 8)
SpearHandle = Weapon(1, "Spear Handle", [l.Lighthouse, l.Temple], [Bamboo, PianoWire], [Blunt], 6)
FryingPan = Weapon(1, "Frying Pan", [l.Slum, l.Hotel], [], [Blunt], 6)
WoodenFish = Weapon(1, "Wooden Fish", [l.Temple], [], [Blunt], 8)
SteelPipe = Weapon(1, "Steel Pipe", [l.Factory], [], [Blunt], 8)
SteelChain = Weapon(1, "Steel Chain", [l.Uptown, l.Slum, l.Hotel, l.Alley], [], [Blunt], 8)
Whip = Weapon(1, "Whip", [l.Cemetary, l.Hotel, l.Lighthouse], [], [Blunt], 10)
Bat = Weapon(1, "Bat", [l.School], [], [Blunt], 10)
Hammer = Weapon(1, "Hammer", [l.FireStation, l.TownHall, l.Dock, l.Hospital], [], [Blunt], 12)
LongRod = Weapon(1, "Long rod", [l.Trail, l.Pond], [], [Blunt], 14)
#Bow
# = Weapon(1, "AAA", [], [], [Bow], )
CrudeBow = Weapon(1, "Crude Bow", [], [], [Bow], 6)
YumiBow = Weapon(1, "Yumi Bow", [l.Temple, l.ArcheryRange], [], [Bow], 12)
Bow = Weapon(1, "Bow", [], [l.ArcheryRange, l.Chapel], [Bow], 12)
ShortCrossbow = Weapon(1, "Short Crossbow", [l.Well, l.Factory, l.Chapel], [], [Bow], 12)
HeavyCrossbow = Weapon(1, "Heavy Crossbow", [l.ArcheryRange], [], [Bow], 24)
#Hand
#Gun
CrudeGun = Weapon(1, "Crude Gun", [], [], [Gun], 6)
RevolverMk2 = Weapon(1, "Revolver Mk 2", [l.Chapel, l.Dock], [], [Gun], 10)
RevolverMk1 = Weapon(1, "Revolver Mk 1", [l.Dock, l.Chapel], [], [Gun], 10)
WalterPPK = Weapon(1, "Walter PPK", [l.Dock], [], [Gun], 22)
BerettaM92F = Weapon(1, "Beretta M92F", [l.Chapel, l.Dock], [], [Gun], 22)
RemingtonM31RS = Weapon(1, "Remington M31RS", [l.Dock], [], [Gun], 22)
IngramMAC10 = Weapon(1, "Ingram MAC-10", [l.Beach], [], [Gun], 24)
ColtPython = Weapon(1, "Colt Python", [l.Beach], [], [Gun], 28)
#Thrown
# = Weapon(1, "AAA", [], [], [Thrown], 5)
GlassCup = Weapon(1, "Glass", [l.Alley, l.Uptown, l.Hotel, l.Slum], [], [Thrown], 5)
Plate = Weapon(2, "Plate", [l.Alley, l.Hotel, l.Uptown], [], [Thrown], 5)
GlassBottle = Weapon(1, "Glass Bottle", [l.Tunnel], [], [Thrown], 5)
GlassMarble = Weapon(2, "Glass Marble", [l.Factory, l.Chapel], [], [Thrown], 5)
Dice = Weapon(1, "Dice", [l.TownHall], [], [Thrown], 5)
WhiteChalk = Weapon(1, "White Chalk", [l.SChool], [], [Thrown], 5)
CD = Weapon(1, "CD", [], [l.Chapel, l.Slum], [Thrown], 5)
Can = Weapon(1, "Can", [l.Tunnel, l.Beach], [], [Thrown], 5)
PlasticBottle = Weapon(1, "Plastic Bottle", [l.Pond], [], [Thrown], 5)
Mudfish = Weapon(1, "Mudfish", [l.Pond], [], [Thrown], 5)
CrudeBall = Weapon(10, "Crude Ball", [], [], [Thrown], 6)
Carp = Weapon(1, "Carp", [l.Pond], [], [Thrown], 6)
BaseballSet = Weapon(12, "Baseball Set", [l.TownHall, l.School, l.Slum], [], [Trown], 6)
Gemstone = Weapon(1, "Gemstone", [l.Trail, l.Pond, l.Tunnel], [], [Trown], 6)
Stone = Weapon(3, "Stone", [l.Tunnel, l.Trail, l.Temple, l.Cemetary, l.Hotel], [], [Thrown], 8)
HolyGrail = Weapon(1, "Holy Grail", [l.Chapel], [], [Thrown], 8)
CookingPot = Weapon(1, "Cooking Pot", [l.Slum, l.Uptown, l.Alley, l.Hotel], [], [Thrown], 10)
ThrowingDagger = Weapon(15, "Throwing Dagger", [l.Cemetary, l.Chapel], [], [Thrown], 12)
LaptopBroken = Weapon(1, "Laptop(screen broke)", [l.Uptown, l.Hotel], [], [Thrown], 12)
PlayingCards = Weapon(52, "Playing Cards", [l.TownHall], [], [Thrown], 5)
StallionMedal = Weapon(1, "Stallion Medal", [l.Temple], [], [Thrown], 5)
Shuriken = Weapon(20, "Shuriken", [], [l.Random], [Thrown], 24)
Dart = Weapon(28, "Dart", [], [], [Thrown], 12)
IronBall = Weapon(20, "Iron Ball", [l.Well, l.Tunnel], [], [Thrown], 8)
TV = Weapon(1, "TV", [l.Alley, l.Slum, l.Uptown, l.TownHall], [], [Thrown], 40)

#Trap
#Stab
Needle = Weapon("Needle", [l.Alley, l.Slum, l.Uptown], [], [Stab])
FountainPen = Weapon(1, "Fountain Pen", [l.School, l.Hospital], [], Stab)
CrudeAwl = Weapon(1, "CrudeAwl", [], [], [Stab], 6)
ShortSpear = Weapon(1, "Short Spear", [l.Temple, l.Forest], [], [Stab], 10)
Harpoon = Weapon(1, "Harpoon", [l.Forest], [], [Stab], 14)

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

#List of armor
#Head
#Clothes
#Arm
#Leg
#Accessory
PowderOfLife = Armor(1, "Powder of Life", [], [TreeOfLife, Stone], [Accessory])

#List of weapons
# = Weapon(1, "AAA", [], [], [Blunt], 5)
#Hand
NanorizedArms = Weapon(1, "Nanorized Arms", [], [HolyBlood, EngineeredArcaneMotor], [Hand], 60)
#Blunt
SolderingIron = Weapon(1, "Soldering Iron", [], [Nail, ElectronicParts], [Blunt], 5)
StoneAxe = Weapon(1, "Stone Axe", [], [Stone, Bamboo], [Blunt], 10)
FlagPole = Weapon(1, "Flag Pole", [], [LongRod, Nail], [Blunt], 10)
HeatedSteelPipe = Weapon(1, "Heated Steel Pipe", [], [SteelPipe, Lighter], [Blunt], 15)
FeatherDuster = Weapon(1, "Feather Duster", [], [Feather, SpearHandle], [Blunt], 15)
MorningStar = Weapon(1, "MorningStar", [], [LongRod, IronBall], [Blunt], 15)
HeatedFryingPan = Weapon(1, "Heated Frying Pan", [], [FryingPan, Lighter], [Blunt], 15)
GoblinBat = Weapon(1, "Goblin Bat", [], [ShortRod, Nail], [Blunt], 15)
Tonfa = Weapon(1, "Tonfa", [], [CottonWorkGloves, ShortRod], [Blunt], 18)
ChainRod = Weapon(1, "Chain Rod", [], [SteelChain, ShortRod], [Blunt], 20)
DeadBattery = Weapon(1, "Dead Battery", [], [Water, Battery], [Thrown], 14)
HighVoltageLine = Weapon(1, "High Voltage Line", [], [DeadBattery, Wire], [Blunt], 20)
Bullwhip = Weapon(1, "Bullwhip", [], [Razor, Whip], [Blunt], 20)
SafetyRod = Weapon(1, "Safety Rod", [], [], [Blunt], 20)
Warhammer = Weapon(1, "Warhammer", [], [Hammer, SpearHandle], [Blunt], 22)
LeatherWhip = Weapon(1, "Leather Whip", [], [Leather, Scissors], [Blunt], 24)
ClawHammer = Weapon(1, "Claw Hammer", [], [], [Blunt], 25)
Iron Mace = Weapon(1, "Iron Mace", [], [StoneAxe, SteelChain], [Blunt], 30)
SpikedBat = Weapon(1, "Spiked bat", [], [Bat, Nail], [Blunt], 34)
TorchHold = Weapon(1, "Torch Hold", [], [Oilcloth, Bamboo], [Blunt], 26)
Umbrella = Weapon(1, "Umbrella", [], [Oilcloth, LongRod], [Blunt], 32)
RopeCuffs = Weapon(1, "Rope Cuffs", [], [StallionMedal, Whip], [Blunt], 32)
LightningWhip = Weapon(1, "Lightning Whip", [], [Bullwhip, DeadBattery], [Blunt], 32)
Torch = Weapon(1, "Torch", [], [TorchHold, Lighter], [Blunt], 32)
Nunchaku = Weapon(1, "Nunchaku", [], [ChainRod, ShortRod], [Blunt], 32)
SpikedPlank = Weapon(2, "Spiked Plank", [], [Needle, Branch], [Trap], 30)
ThornWhip = Weapon(1, "Thorn Whip", [], [SpikedPlank, Whip], [Blunt], 32)
ElectricWhip = Weapon(1, "Electic Whip", [], [HighVoltageLine, Whip], [Blunt], 34)
UsurperWarhammer = Weapon(1, "Usurper Warhammer", [], [Warhammer, Adamantium], [Blunt], 34)
SteelTonfa = Weapon(1, "Steel Tonfa", [], [Tonfa, Steel], [Blunt], 34)
WhiteCraneFan = Weapon(1, "White Crane Fan", [], [Feather, Fan], [Blunt], 34)
Flail = Weapon(1, "Flail", [], [ChainRod, IronBall], [Blunt], 38)
GolfClub = Weapon(1, "Golf Club", [], [HeatedSteelPipe, Hammer], [Blunt], 38)
GoldenWhip = Weapon(1, "Golden Whip", [], [Bullwhip, Gold], [Blunt], 40)
TripleNunchaku = Weapon(1, "Triple Nunchaku", [], [Nunchaku, ChainRod], [Blunt], 43)
DoubleNunchaku = Weapon(1, "Double Nunchaku", [], [Nunchaku, Bullwhip], [Blunt], 43)
BeamTonfa = Weapon(1, "Beam Tonfa", [], [SteelTonfa, LaserPointer], [Blunt], 40)
Vajra = Weapon(1, "Vajra", [], [TreeOfLife, SpikedBat], [Blunt], 41)
KGBAgentUmbrella = Weapon(1, "KGB Agent Umbrella", [], [Umbrella, Poison], [Blunt], 44)
RedMuffler = Weapon(1, "Red Muffler", [], [Scarf, HolyBlood], [Blunt], 46)
TitanHammer = Weapon(1, "Titan Hammer", [], [Hammer, OgreSkin], [Blunt], 46)
BananaLeafFan = Weapon(1, "Banana Leaf Fan", [], [WhiteCraneFan, PowderOfLife], [Blunt], 46)
VillainousWhip = Weapon(1, "'Villainous Whip'", [], [LightningWhip, ElectricWhip], [Blunt], 46)
HammerOfThor = Weapon(1, "Hammer of Thor", [], [UsurperWarhammer, HighVoltageLine], [Blunt], 48)
FangMace = Weapon(1, "Fang Mace", [], [ArcaneStone, GoblinBat], [Blunt], 48)
Gleipnir = Weapon(1, "Gleipnir", [], [RopeCuffs, ThornWhip], [Blunt], 48)
StatueOfLiberty = Weapon(1, "Statue of Liberty", [], [Torch, AnatomyModel], [Blunt], 48)
MagicStick = Weapon(1, "Magic Stick", [], [Warhammer, MoonlightPendant], [Blunt], 48)
MonkeyKingBar = Weapon(1, "Monkey King Bar", [], [NanorizedArms, SpearHandle], [Blunt], 65)
#Gun
LongRifle = Weapon(1, "Long Rifle", [l.Dock, l.Beach], [Bamboo, Gunpowder], [Gun], 10)
BoltActionRifle = Weapon(1, "Bolt Action Rifle", [], [LongRifle, SteelPipe], [Gun], 24)
DoubleRevolverSP = Weapon(1, "Double Revolver SP", [], [RevolverMk1, RevolverMk2], [Gun], 28)
K5AutomaticRifle = Weapon(1, "K5 Automatic Rifle", [], [WalterPPK, Steel], [Gun], 34)
FN57 = Weapon(1, "FN57", [], [BerettaM92F, Steel], [Gun], 34)
HandCannon = Weapon(1, "Hand Cannon", [], [IronSheet, Gunpowder], [Gun], 36)
MP5 = Weapon(1, "MP5", [], [FN57, LaserPointer], [Gun], 38)
SteyrAUG = Weapon(1, "Steyr AUG", [], [IngramMAC10, LaserPointer], [Gun], 38)
AK47 = Weapon(1, "AK-47", [], [LongRifle, ScrapMetal], [Gun], 38)
M16A1 = Weapon(1, "M16A1", [], [WalterPPK, LaserPointer], [Gun], 38)
HolyWater = HFood(1, "Holy Water", [l.Chapel], [HolyGrail, Water], 101)
ColtAnaconda = Weapon(1, "Colt Anaconda", [], [ColtPython, HolyWater], [Gun], 42)
ElectronBlaster = Weapon(1, "Electron Blaster", [], [CRT, IonBattery], [Gun], 42)
Railgun = Weapon(1, "Railgun", [], [ElectronicParts, SteyrAUG], [Gun], 42)
MachineGun = Weapon(1, "Machine Gun", [], [Motor, M16A1], [Gun], 42)
FRF2 = Weapon(1, "FRF2", [], [AK47, SnipingScope], [Gun], 43)
PSG1 = Weapon(1, "PSG-1", [], [SteyrAUG, SnipingScope], [Gun], 43)
HarpoonGun = Weapon(1, "Harpoon Gun", [], [LongRifle, Harpoon], [Gun], 43)
GoldenRifle = Weapon(1, "Golden Rifle", [], [BoltActionRifle, Gold], [Gun], 44)
HolyShotgun = Weapon(1, "Holy Shotgun", [], [BoltActionRifle, Cross], [Gun], 45)
DevilsMarksman = Weapon(1, "Devil's Marksman", [], [DoubleRevolverSP, HandCannon], [Gun], 46)
TCArmsContender = Weapon(1, "T/C Arms Contender", [], [K5AutomaticRifle, FN57], [Gun], 46)
GrandHandCannon = Weapon(1, "Grand Hand Cannon", [], [HandCannon, TrueSamadhiFire], [Gun], 50)
UraniumCannon = Weapon(1, "Uranium Cannon", [], [HandCannon, ArcaneStone], [Gun], 50)
GatlingGun = Weapon(1, "Gatling Gun", [], [MachineGun, AK47], [Gun], 50)
BarrettM82A1 = Weapon(1, "Barrett M82A1", [], [PSG1, HandCannon], [Gun], 50)
BlizzardCannon = Weapon(1, "Blizzard Cannon", [], [HandCannon, GlacialIce], [Gun], 50)
PositronRifle = Weapon(1, "Positron Rifle", [], [ElectronBlaster, FRF2], [Gun], 52)
PlasmaRailgun = Weapon(1, "Plama Railgun", [], [Railgun, CellPhone], [Gun], 54)
Kelte = Weapon(1, "Kelte", [], [NanorizedArms, BoltActionRifle], [Gun], 75)
#Hand
#Stab
HeatedWhetstone = Weapon(1, "Heated Whetstone", [], [Lighter, Whetstone], [Thrown])
Sabre = Weapon(1, "Sabre", [], [Shameshir, HeatedWhetstone], [Blade], 28)
SharpKitchenKnife = Weapon(1, "Sharp Kitchen Knife", [], [Whetstone, KitchenKnife], [Blade, Stab], 14)
TwinSword = Weapon(1, "Twin Sword", [], [SharpKitchenKnife, KitchenKnife], [Blade, Stab], 32)
Jamadhar = Weapon(1, "Jamadhar", [], [Knuckle, KitchenKnife], [Blade, Stab], 20)
Awl = Weapon(1, "Awl", [], [Nail, ScrapMetal], [Stab], 20)
LongSpear = Weapon(1, "Long Spear", [], [ShortSpear, SpearHandle], [Stab], 26)
BambooSpear = Weapon(1, "Bamboo Spear", [], [Bamboo, Knife], [Stab], 36)
Rapier = Weapon(1, "Rapier", [], [Sabre, HeatedWhetstone], [Stab], 32)
Trident = Weapon(1, "Trident", [], [LongSpear, TwinSword], [Stab], 34)
Bident = Weapon(1, "Bident", [], [Rapier, ShortSpear], [Stab], 34)
SwordOfAssasin = Weapon(1, "Sword of Assasin", [], [Jamadhar, ArmWarmers], [Stab], 34)
SonicScrew = Weapon(1, "Sonic Screw", [], [Awl, ElectronicParts], [Stab], 36)
PileBunker = Weapon(1, "Pile Bunker", [], [RemingtonM31RS, Harpoon], [Stab], 38)
Shockblade = Weapon(1, "Shockblade", [], [SonicScrew, SwordOfAssasin], [Stab], 46)
BlazingLance = Weapon(1, "BlazingLance", [], [TrueSamadhiFire, LongSpear], [Stab], 48)
CosmicBident = Weapon(1, "Cosmic bident", [], [Bident, IonBattery], [Stab], 48)
PurifiedWater = SFood(4, "Purified Water", [], [BoilingWater, Ice], 40)
LanceOfPoseidon = Weapon(1, "Lance of Poseidon", [], [PurifiedWater, Trident], [Stab], 48)
SpearOfLonginus = Weapon(1, "SpearOfLonginus", [], [LongSpear, HolyBlood], [Stab], 48)
#Blade
ChainScythe = Weapon(1, "Chain Scythe", [], [SteelChain, Sickle], [Blade], 26)
AxeChain = Weapon(1, "Axe Chain", [], [SteelChain, Hatchet], [Blade], 26)
BattleAxe = Weapon(1, "Battle Axe", [], [SpearHandle, Hatchet], [Blade], 26)
Scimitar = Weapon(1, "Scimitar", [], [Shameshir, SharpKitchenKnife], [Blade], 28)
ArmyKnife = Weapon(1, "Army Knife", [], [Knife, Branch], [Blade, Stab], 36)
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
PhaseSabre = Weapon(1, "Phase Sabre", [], [NanorizedArms, LaserPointer], [Blade, Stab], 65)
#Bow
# = Weapon(1, "AAA", [], [], [Bow], )
CompositeBow = Weapon(1, "Composite Bow", [], [Bow, PianoWire], [Bow], 26)
WoodenBow = Weapon(1, "Wooden Bow", [], [Branch, PianoWire], [Bow], 26)
MightyBow = Weapon(1, "Mighty Bow", [], [WoodenBow, Gunpowder], [Bow], 26)
PelletBow = Weapon(1, "Pellet Bow", [], [Branch, Wire], [Bow], 28)
LongCrossbow = Weapon(1, "Long Crossbow", [], [ShortCrossbow, PianoWire], [Bow], 28)
Longbow = Weapon(1, "Longbow", [], [YumiBow, Rubber], [Bow], 34)
StrongBow = Weapon(1, "Strongbow", [], [Longbow, Gasoline], [Bow], 34)
SteelBow = Weapon(1, "Steel Bow", [], [LongCrossbow, IronSheet], [Bow], 34)
Crossbow = Weapon(1, "Crossbow", [], [CompositeBow, Bamboo], [Bow], 34)
Scorchbow = Weapon(1, "Scorchbow", [], [YumiBow, Flint], [Bow], 36)
PowerCrossbow = Weapon(1, "Power Crossbow", [], [Crossbow, Rubber], [Bow], 36)
SniperCrossbow = Weapon(1, "Sniper Crossbow", [], [LaserPointer, HeavyCrossbow], [Bow], 38)
SniperBow = Weapon(1, "Sniper Bow", [], [LongCrossbow, LaserPointer], [Bow], 38)
GoldenRatioBow = Weapon(1, "Golden-ratio Bow", [], [PelletBow, Gold], [Bow], 42)
HwaCha = Weapon(1, "HwaCha", [], [Scorchbow, PowerCrossbow], [Bow], 44)
CupidsBow = Weapon(1, "Cupid's Bow", [], [CompositeBow, CrimsonBracelet], [Bow], 46)
Twinbow = Weapon(1, "Twinbow", [], [LongCrossbow, StrongBow], [Bow], 46)
ElementalBow = Weapon(1, "Elemental Bow", [], [Scorchbow, MightyBow], [Bow], 46)
StallionBow = Weapon(1, "StallionBow", [], [WoodenBow, StallionMedal], [Bow], 46)
Ballista = Weapon(1, "Ballista", [], [SteelBow, ShortSpear], [Bow], 46)
Failnaught = Weapon(1, "Failnaught", [], [Longbow, HolyBlood], [Bow], 48)
BowOfZephyrus = Weapon(1, "Bow of Zephyrus", [], [CompositeBow], [Bow], PowderOfLife)
BowOfApollo = Weapon(1, "Bow of Apollo", [], [ArcaneStone, SteelBow], [Bow], 50)
Sharanga = Weapon(1, "Sharanga", [], [Crossbow, NanorizedArms], [Bow], 70)
#Thrown
CDPlayer = Weapon(1, "CD Player", [], [ElectronicParts, GlassMarble], [Thrown], 5)
GlueLump = Weapon(10, "Glue Lump", [], [Glue, BoilingWater], [Thrown], 20)
PaperBall = Weapon(40, "Paper Ball", [], [ThickPaper, Glue], [Thrown], 20)
Flubber = Weapon(19, "Flubber", [], [Rubber, BoilingWater], [Thrown], 20)
ThrowingStars = Weapon(15, "Throwing Stars", [], [Cutter, Razor], [Thrown], 24)
Boomerang = Weapon(10, "Boomerang", [], [Branch, Rubber], [Thrown], 26)
Javeline = Weapon(8, "Javeline", [], [SpearHandle, ThrowingDagger], [Thrown], 28)
Dynamite = Weapon(4, "Dynamite", [], [Wire, Gunpowder], [Thrown], 28)
Grenade = Weapon(20, "Grenade", [], [Gunpowder, IronBall], [Thrown], 8)
MolotovCocktail = Weapon(4, "Molotov Cocktail", [], [Gasoline, GlassBottle], [Thrown], 30)
StormBolt = Weapon(19, "Storm Bolt", [], [Hammer, DeadBattery], [Thrown], 30)
VintageCard = Weapon(12, "Vintage Card", [], [PlayingCards, FountainPen], [Thrown], 30)
FlourBomb = Weapon(2, "Flour Bomb", [], [WhitePowder, PlasticBottle], [Thrown], 32)
OnyxDagger = Weapon(12, "Onyx Dagger", [], [Cross, ThrowingDagger], [Thrown], 34)
Tomahawk = Weapon(15, "Tomahawk", [], [Hatchet, Leather], [Thrown], 34)
Chakram = Weapon(25, "Chakram", [], [ThrowingStars, CD], [Thrown], 35)
CrowCard = Weapon(20, "Crow Card", [], [BuddhistScripture, PlayingCards], [Thrown], 38)
Pilum = Weapon(7, "Pilum", [], [Javeline, ShortSpear], [Thrown], 38)
SpikyBouncyBall = Weapon(12, "Spike Bouncy Ball", [], [Flubber, GlassPieces], [Thrown], 39)
EnhancedBoomerang = Weapon(16, "Enhanced Boomerang", [], [Boomerang, Oilcloth], [Thrown], 39)
IncendiaryBomb = Weapon(1, "Incendiary Bomb", [], [MolotovCocktail, Gunpowder], [Thrown], 48)
DharmaChakram = Weapon(26, "Dharma Chakram", [], [BuddhistScripture, Chakram], [Thrown], 41)
Astrape = Weapon(60, "Astrape", [], [Pilum, SonicScrew], [Thrown], 44)
AzureDagger = Weapon(25, "Azure Dagger", [], [Poison, OnyxDagger], [Thrown], 44)
FuhmaShuriken = Weapon(1, "Fuhma Shuriken", [], [ThrowingStars, TwinSword], [Thrown], 46)
BloodyChakram = Weapon(50, "Bloody Chakram", [], [HolyBlood, Chakram], [Thrown], 46)
DavidsSling = Weapon(39, "David's Sling", [], [Adamantium, ArcaneStone], [Thrown], 50)
HighExplosiveGrenade = Weapon(6, "High Explosive Grenade", [], [Grenade, Mine], [Thrown], 50)
RutheniumMarble = Weapon(44, "Ruthnenium Marble", [], [Gold, EngineeredArcaneMotor], [Thrown], 50)
DAxeOfHeadman = Weapon(1, "D-Axe of Headsman", [], [Tomahawk, Motor], [Thrown], 51)
VenomDart = Weapon(4, "Venom Dart", [], [Needle, Poison], [Thrown], 56)
Sudarsana = Weapon(40, "Sudarsana", [], [NanorizedArms, CD], [Thrown], 75)
FrostVenomDart = Weapon(1, "Frost Venom Dart", [], [VenomDart, GlacialIce], [Thrown], 100)
PetalTorrent = Weapon(1, "Petal Torrent", [], [FrostVenomDart, StingBurst], [Thrown], 200)
#Trap

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
