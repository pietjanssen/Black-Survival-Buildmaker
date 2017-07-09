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
Slipper = Armor(1, "Slipper", [l.TownHall], [], [Leg], 1)
RunningShoes = Armor(1, "Running Shoed", [l.Uptown, l.Alley], [], [Leg], 3)
Tights = Armor(1, "Tights", [l.Random], [], [Leg], 3)
WoodenShoes = Armor(1, "Wooden Shoed", [l.Chapel], [], [Leg], 3)
HikingShoes = Armor(1, "Hiking Shoes", [l.Trail], [], [Leg], 3)
#Armor
KneePads = Armor(1, "KneePads", [], [Cloth, Leather], [Leg], 10)
FeatherBoots = Armor(1, "Feather Boots", [], [Boots, Feather, [Leg], 12)
AdvancedMilitaryBoots = Armor(1, "Advanced Military Boots", [], [Boots, Cloth], [Leg], 15)
Heelys = Armor(1, "Heelys", [], [RunningShoes, IronBall], [Leg], 20)
HighHeels = Armor(1, "High Heels", [], [Slipper, ScrapMetal], [Leg], 20)
ChainLeggings = Armor(1, "Chain Leggings", [], [Tights, SteelChain], [Leg], 22)
SteelKneePads = Armor(1, "Steel Knee Pads", [], [KneePads, Steel], [Leg], 25)
BattleBoots = Armor(1, "Battle Boots", [], [AdvancedMilitaryBoots, SteelKneePads], [Leg], 30)
DetectivesHeelys = Armor(1, "Detective Heelys", [], [Heelys, ElectronicParts], [Leg], 30)
KillHeels = Armor(1, "Kill Heels", [], [HighHeels, GlassPieces], [Leg], 35)
MithrilBoots = Armor(1, "Mithril Boots", [], [FeatherBoots, Mitrhil], [Leg], 35)
BootsOfTheHermes = Armor(1, "Boots of the Hermes", [], [ArcaneStone, FeatherBoots], [Leg], 45)