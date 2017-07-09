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
CrudeBow = Weapon(1, "Crude Bow", [], [], [Bow], 6)
YumiBow = Weapon(1, "Yumi Bow", [l.Temple, l.ArcheryRange], [], [Bow], 12)
Bow = Weapon(1, "Bow", [], [l.ArcheryRange, l.Chapel], [Bow], 12)
ShortCrossbow = Weapon(1, "Short Crossbow", [l.Well, l.Factory, l.Chapel], [], [Bow], 12)
HeavyCrossbow = Weapon(1, "Heavy Crossbow", [l.ArcheryRange], [], [Bow], 24)
#Weapons
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