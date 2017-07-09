import Locations as l
import Category

class Armor:
    def __init__(self, quantity, name, location, ingredients, category, armor):
        self.quantity = quantity
        self.name = name
        self.location = location
        self.ingredients = ingredients
        self.category = category
        self.armor = armor

#Base armor
Box = Armor(1, "Box", [l.Tunnel, l.School, l.Pond], [], [Accessory], 2)
Cross = Armor(1, "Cross", [l.Chapel], [], [Accessory], 2)
Flower = Armor(1, "Flower", [l.Pond, l.Cemetary, l.Forest, l.ArcheryRange], [], [Accessory], 2)
Ribbon = Armor(1, "Ribbon", [l.Uptown, l.School], [], [Accessory], 2)
#Armor
Telescope = Armor(1, "Telescope", [], [GlassMarble, Bamboo], [Accessory], 2)
Magainze = Armor(1, "Magazine", [l.Beach, l.Dock], [Box, IronSheet], [Accessory], 6)
Quiver = Armor(1, "Quiver", [l.ArcheryRange], [Bamboo, Leather], [Accessory], 6)
Doll = Armor(1, "Doll", [], [Cloth, GlassMarble], [Accessory], 6)
Belt = Armor(1, "Belt", [], [Leather, ScrapMetal], [Accessory], 6)
PowderOfLife = Armor(1, "Powder of Life", [], [TreeOfLife, Stone], [Accessory], 6)
FlagPole = Weapon(1, "Flag Pole", [], [LongRod, Nail], [Blunt], 10)
Flag = Armor(1, "Flag", [], [FlagPole, Cloth], [Accessory], 8)
CrossOfGolgotha = Armor(1, "Cross of Golgotha", [], [HolyGrail, Cross], [Accessory], 8)
GlacialIce = Armor(1, "GlacialIce", [], [PowderOfLife, Ice], [Accessory], 8)
SnipingScope = Armor(1, "Sniping Scope", [], [LaserPointer, Telescope], [Accessory], 8)
TrueSamadhiFire = Armor(1, "True Samadhi Fire", [], [PowderOfLife, Lighter], [Accessory], 8)
MoonStone = Armor(1, "Moon Stone", [], [Starsteel, Stone], [Accessory], 8)
BuddhaSahira = Armor(1, "Buddha Sarira", [], [BuddhistScripture, WoodenFish], [Accessory], 10)
AngelWing = Armor(1, "Angel Wing", [], [BishopsCassock, Feather], [Accessory], 10)
DiceOfDestiny = Armor(1, "Dice of Destiny", [], [PlayingCards, Dice], [Accessory], 10)
MirrorMarble = Armor(1, "Mirror Marble", [], [Mithril, GlassMarble], [Accessory], 12)
Uchiwa = Armor(1, "Uchiwa", [], [Fan, Doll], [Accessory], 12)
MoonlightPendant = Armor(1, "Moonlight Pendant", [], [Moonstone, Ribbon], [Accessory], 14)
PirateFlag = Armor(1, "PirateFlag", [], [Flag, TwinSword], [Accessory], 16)
SchrodingersBox = Armor(1, "Schrodinger's Box", [], [Box, Poison], [Accessory], 18)
Kundala = Armor(1, "Kundala", [], [Adamantium, MoonStone], [Accessory], 18)
VeritasLuxMea = Armor(1, "Veritas Lux Mea", [], [CrossOfGolgotha, BuddhaSahira], [Accessory], 20)