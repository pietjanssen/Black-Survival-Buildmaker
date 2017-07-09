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
Cassock = Armor(1, "AAA", [l.Chapel], [], [Clothes], 5)
DoctorsGown = Armor(1, "Doctor's Gown", [], [l.Hospital], [Clothes], 5)
Windbreaker = Armor(1, "Windbreaker", [l.Uptown, l.Well, l.School], [], [Clothes], 5)
FabricArmor = Armor(1, "Fabric Armor", [l.Temple, l.ArcheryRange], [], [Clothes], 8)
BunkerJacket = Armor(1, "Bunker Jacket", [l.FireStation], [], [Clothes], 8)
MonkRobe = Armor(1, "Monk Robe", [l.Temple], [], [Clothes], 8)
#Armor
BishopsCassock = Armor(1, "Bishop's Cassock", [], [Cross, Cassock], [Clothes], 12)
Bikini = Armor(1, "Bikini", [], [FullBodySwimsuit, Scissors], [Clothes], 12)
Dress = Armor(1, "Dress", [], [Cloth, DoctorsGown], [Clothes], 15)
DressShirts = Armor(1, "Dress Shirts", [], [Cloth, Scissors], [Clothes], 15)
TurtleDobok = Armor(1, "Turtle Dobok", [], [MonkRobe, TurtleShell], [Clothes], 15)
DivingSuit = Armor(1, "Diving Suit", [], [FullBodySwimsuit, Rubber], [Clothes], 18)
PatchedRobe = Armor(1, "Patched Robe", [], [MonkRobe, Cloth], [Clothes], 18)
MilitarySuit = Armor(1, "Military Suit", [], [Windbreaker, Branch], [Clothes], 18)
LeatherArmor = Armor(1, "Leather Armor", [], [FabricArmor, Leather], [Clothes], 20)
LeatherJacket = Armor(1, "Leather Jacket", [], [Leather, Windbreaker], [Clothes], 30)
Hanbok = Armor(1, "Hanbok", [], [Dress, Flower], [Clothes], 35)
Qipao = Armor(1, "Qipao", [], [Dress, Scissors], [Clothes], 35)
Suit = Armor(1, "Suit", [], [DressShirts, Cloth], [Clothes], 35)
BulletproofVest = Armor(1, "Bulletproof Vest", [], [MilitarySuit, IronSheet], [Clothes], 35)
RiderJacket = Armor(1, "Rider Jacket", [], [LeatherJacket, SteelChain], [Clothes], 35)
ChainArmor = Armor(1, "Chain Armor", [], [SteelChain, LeatherArmor], [Clothes], 40)
SheetMetalArmor = Armor(1, "Sheet Metal Armor", [], [FabricArmor, Steel], [Clothes], 40)
SunsetArmor = Armor(1, "Sunset Armor", [], [LeatherArmor, Ruby], [Clothes], 50)
ButletsSuit = Armor(1, "Butler's Suit", [], [Suit, FeatherDuster], [Clothes], 50)
TuxedoMask = Armor(1, "Tuxedo Mask", [], [Suit, MoonlightPendant], [Clothes], 40)
OpticalCamouflageSuit = Armor(1, "Optical Camouflage Suit", [], [DivingSuit, GlassPanel], [Clothes], 50)
AmazonesArmor = Armor(1, "Amazones Armor", [], [SheetMetalArmor, Bikini], [Clothes], 55)
CrusaderArmor = Armor(1, "Crusader Armor", [], [CrusaderArmor, BishopsCassock], [Clothes], 55)
DragonDobok = Armor(1, "Dragon Dobok", [], [Qipao, TurtleDobok], [Clothes], 55)
EODSuit = Armor(1, "Bulletproof Vest", [], [BulletproofVest, PatchedRobe], [Clothes], 55)
ChangPao = Armor(1, "Chang Pao", [], [Qipao, DressShirts], [Clothes], 55)
PopesCassock = Armor(1, "Pope's Cassock", [], [BishopsCassock, Gold], [Clothes], 55)
RockerJacket = Armor(1, "Rocker Jacker", [], [RiderJacket, IronSheet], [Clothes], 55)
RedHood = Armor(1, "Red Hood", [], [PatchedRobe, HolyBlood], [Clothes], 55)
BattleSuit = Armor(1, "Battle Suit", [], [DivingSuit, BulletproofVest], [Clothes], 60)
DazzlingSuit = Armor(1, "Dazzling", [], [ChainArmor, Dress], [Clothes], 60)
CovertAgentUniform = Armor(1, "Covert Agent Uniform", [], [StallionMedal, Hanbok], [Clothes], 60)
Kabana = Armor(1, "Kabana", [], [SheetMetalArmor, Adamantium], [Clothes], 65)
BlazingArmor = Armor(1, "Blazing Armor", [], [Dress, TrueSamadhiFire], [Clothes], 65)
CommandersArmor = Armor(1, "Commander's Armor", [], [ChainArmor, Gold], [Clothes], 65)
MithrilArmor = Armor(1, "Mithril Armor", [], [ChainArmor, Mithril], [Clothes], 65)
GhostriderJacket = Armor(1, "Ghostrider Jacket", [], [RiderJacket, TrueSamadhiFire], [Clothes], 90)
Automail = Armor(1, "Automail", [], [SheetMetalArmor, EngineeredArcaneMotor], [Clothes], 120)
QueenOfHeart = Armor(1, "Queen of Heart", [], [ArcaneStone, PlayingCards], [Clothes], 150)