import Locations as l
import Category
from Normal import *

class Weapon:
    def __init__(self, quantity, name, location, ingredients, category, damage):
        self.quantity = quantity
        self.name = name
        self.ingredients = ingredients
        self.location = location
        self.category = category
        self.damage = damage

#Base weapons
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

#Weapons
CDPlayer = Weapon(1, "CD Player", [], [ElectronicParts, GlassMarble], [Thrown], 5)
DeadBattery = Weapon(1, "Dead Battery", [], [Water, Battery], [Thrown], 14)
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