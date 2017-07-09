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
Snare = Weapon(2, "Snare", [l.Chapel, l.Pong, l.Dock, l.Well, l.Beach, l.ArcheryRange, l.Forest], [], [Trap], 5)
PianoWire = Weapon(1, "Piano Wire", [l.ArcheryRange, l.Cemetary, l.FireStation, l.TownHall], [], [Trap], 8)
Mousetrap = Weapon(1, "Mousetrap", [l.FireStation, l.Beach, l.Pond, l.Factory], [], [Trap], 10)
HuntingTrap = Weapon(2, "Hunting trap", [], [], [Trap], 30)
#Weapons
BambooTrap = Weapon(2, "Bamboo Trap", [], [Snare, Bamboo], [Trap], 20)
ElectricShockTrap = Weapon(2, "ElectricShockTrap", [], [DeadBattery], [Trap], 25)
SpikedPlank = Weapon(2, "SpikedPlank", [], [Needle, Branch], [Trap], 30)
Boobytrap = Weapon(1, "Booby Trap", [], [Snare, Glue], [Trap], 40)
EnhancedMouseTrap = Weapon(2, "Enhanced Mouse Trap", [], [Mousetrap, Glue], [Trap], 40)
PopupPirate = Weapon(2, "Popup Pirate", [], [KitchenKnife, Bamboo], [Trap], 45)
RDX = Weapon(1, "RDX", [], [ScrapMetal, Dynamite], [Trap], 50)
Mine = Weapon(1, "Mine", [], [EnhancedMouseTrap, RDX], [Trap], 50)
FireMine = Weapon(3, "Fire Mine", [], [Oilcloth, Mine], [Trap], 40)
JungleGuillotine = Weapon(1, "Jungle Guillotine", [], [Boobytrap, Shameshir], [Trap], 65)
ExplosiveTrap = Weapon(1, "Explosive Trap", [], [Gunpowder, Boobytrap], [Trap], 65)
PendulumAxe = Weapon(1, "Pendulum Axe", [], [BambooTrap, AxeChain], [Trap], 70)
SmallClaymore = Weapon(1, "Small Claymore", [], [GlassPieces, Mine], [Trap], 70)
MithrilString = Weapon(1, "Mithril String", [], [Mithril, Wire], [Trap], 70)
Stringburst = Weapon(1, "Stringburst", [], [SpikedPlank, RDX], [Trap], 80)
FireTrap = Weapon(1, "Fire Trap", [], [Oilcloth, ExplosiveTrap], [Trap], 110)
C4 = Weapon(2, "C4", [], [RDX, WhitePowder], [Trap], 70)
HiddenMaiden = Weapon(2, "Hidden Maiden", [], [Stringburst, PopupPirate], [Trap], 80)
Claymore = Weapon(1, "Claymore", [], [SmallClaymore, IronBall], [Trap], 90)
SmartBomb = Weapon(2, "Smart Bomb", [], [CellPhone, RDX], [Trap], 110)
DoubleGuillotine = Weapon(1, "Double Guillotine", [], [JungleGuillotine, PendulumAxe], [Trap], 130)
SpiderMine = Weapon(3, "Spider Mine", [], [EngineeredArcaneMotor, RDX], [Trap], 120)