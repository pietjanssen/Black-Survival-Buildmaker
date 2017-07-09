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
Glasses = Armor(1, "Glasses", [l.Factory, l.Lighthouse], [], [Head], 1)
Hat = Armor(1, "Hat", [l.ArcheryRange, l.School], [], [Head], 3)
HikingHat = Armor(1, "Hiking Hat", [l.Forest, l.Trail], [], [Head], 3)
BikeHelmet = Armor(1, "Bike Helmet", [l.Beach, l.School, l.Trail, l.Tunnel], [], [Head], 5)
#Armor
Eyepatch = Armor(1, "Eyepatch", [], [Rubber, Leather], [Head], 10)
Mask = Armor(1, "Mask", [], [Feather, Glasses], [Head], 10)
FireHelmet = Armor(1, "Fire Helmet", [l.FireStation], [BikeHelmet, Water], [Head], 12)
Circlet = Armor(1, "Circlet", [], [Hairband, Branch], [Head], 12) 
Tiara = Armor(1, "Tiara", [], [Circlet, Wire], [Head], 12)
Beret = Armor(1, "Beret", [], [FabricArmor, Scissors], [Head], 12)
BallisticHelmet = Armor(1, "Ballistic Helmet", [], [BikeHelmet, Bullet], [Head], 15)
ChainCoif = Armor(1, "Chain Coif", [], [Hat, SteelChain], [Head], 15)
SafetyHelmet = Armor(1, "Safety Helmet", [], [BikeHelmet, Stone], [Head], 15)
Motorcycle = Armor(1, "Motorcycle Helmet", [l.Tunnel], [], [Head], 15)
Crown = Armor(1, "Crown", [], [Gold, Ruby], [Head], 25)
ChiefsEyepatch = Armor(1, "Chief's Eyepatch", [], [Eyepatch, Scissors], [Head], 28)
ProphetsTurban = Armor(1, "Prohet's Turban", [], [Scarf, HolyWater], [Head], 28)
CloseHelm = Armor(1, "Close Helm", [], [ChainCoif, Mask], [Head], 30)
CrystalTiara = Armor(1, "Crystal Tiara", [], [Tiara, GlassPieces], [Head], 32)
LaurelWreath = Armor(1, "Laurel Wreath", [], [Circlet, TreeOfLife], [Head], 40)
HelmOfBanneret = Armor(1, "Helm of Banneret", [], [CloseHelm, IronSheet], [Head], 40)
ImperialBurgonet = Armor(1, "Imperial Burgonet", [], [CloseHelm, Gold], [Head], 48)
TacticalOPSHelmet = Armor(1, "Tactical OPS Helmet", [], [BallisticHelmet, CellPhone], [Head], 48)
ImperialCrown = Armor(1, "Imperial Crown", [], [Crown, CrimsonBracelet], [Head], 52)
TiaraOfLight = Armor(1, "Tiara of Light", [], [CrystalTiara, AngelWing], [Head], 60)