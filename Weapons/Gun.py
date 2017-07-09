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
CrudeGun = Weapon(1, "Crude Gun", [], [], [Gun], 6)
RevolverMk2 = Weapon(1, "Revolver Mk 2", [l.Chapel, l.Dock], [], [Gun], 10)
RevolverMk1 = Weapon(1, "Revolver Mk 1", [l.Dock, l.Chapel], [], [Gun], 10)
WalterPPK = Weapon(1, "Walter PPK", [l.Dock], [], [Gun], 22)
BerettaM92F = Weapon(1, "Beretta M92F", [l.Chapel, l.Dock], [], [Gun], 22)
RemingtonM31RS = Weapon(1, "Remington M31RS", [l.Dock], [], [Gun], 22)
IngramMAC10 = Weapon(1, "Ingram MAC-10", [l.Beach], [], [Gun], 24)
ColtPython = Weapon(1, "Colt Python", [l.Beach], [], [Gun], 28)

#Weapons
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