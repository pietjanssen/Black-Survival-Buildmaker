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
Needle = Weapon("Needle", [l.Alley, l.Slum, l.Uptown], [], [Stab])
FountainPen = Weapon(1, "Fountain Pen", [l.School, l.Hospital], [], Stab)
CrudeAwl = Weapon(1, "CrudeAwl", [], [], [Stab], 6)
ShortSpear = Weapon(1, "Short Spear", [l.Temple, l.Forest], [], [Stab], 10)
Harpoon = Weapon(1, "Harpoon", [l.Forest], [], [Stab], 14)

#Weapons
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
LanceOfPoseidon = Weapon(1, "Lance of Poseidon", [], [PurifiedWater, Trident], [Stab], 48)
SpearOfLonginus = Weapon(1, "SpearOfLonginus", [], [LongSpear, HolyBlood], [Stab], 48)