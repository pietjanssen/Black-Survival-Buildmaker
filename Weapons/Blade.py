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

#Base Blade weapons
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

#Blade weapons
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