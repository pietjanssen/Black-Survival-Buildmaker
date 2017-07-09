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
CrudeGlove = Weapon(1, "Crude Glove", [], [], [Hand], 6)
CottonWorkGloves = Weapon(1, "Cotton Work Glove", [l.Hospital, l.Tunnel, l.Alley], [], [Hand], 8)
Knuckle = Weapon(1, "Knuckle", [l.Lighthouse, l.Temple, l.Well], [], [Hand], 10)
Claw = Weapon(1, "Claw", [l.Well, l.Forest], [], [Hand], 12)
#Weapons
LeatherGlove = Weapon(1, "Leather Glove", [], [CottonWorkGloves, Leather], [Hand], 22)
IronKnuckle = Weapon(1, "Iron Knuckle", [], [Knuckle, IronOre], [Hand], 24)
IronClaw = Weapon(1, "Iron Claw", [], [IronOre, Claw], [Hand], 26)
Gauntlet = Weapon(1, "Gauntlet", [], [CottonWorkGloves, Steel], [Hand], 26)
GlassKnuckle = Weapon(1, "Glass Knuckle", [], [Knuckle, GlassPieces], [Hand], 28)
RubberGlove = Weapon(1, "Rubber Glove", [], [CottonWorkGloves, Rubber], [Hand], 35)
WingKnuckle = Weapon(1, "Wing Knuckle", [], [IronKnuckle, Feather], [Hand], 32)
OpenFingerGlove = Weapon(1, "Open Finger Glove", [], [LeatherGlove, Scissors], [Hand], 32)
SapGlove = Weapon(1, "Sap Glove", [], [LeatherGlove, IronOre], [Hand], 32)
BoneGauntlet = Weapon(1, "Bone Gauntlet", [], [Gauntlet, TurtleShell], [Hand], 34)
Scissorhands = Weapon(1, "Scissorhands", [], [IronClaw, Scissors], [Hand], 34)
NineYinClaw = Weapon(1, "NineYin Claw", [], [RippedScroll1, RippedScroll2], [Hand], 36)
FingerPunch = Weapon(1, "Finger Punch", [], [OpenFingerGlove, IronOre], [Hand], 36)
NirvanaGauntlet = Weapon(1, "Nirvana Gauntlet", [], [OpenFingerGlove, Ash], [Hand], 36)
LaceGlove = Weapon(1, "Lace Glove", [], [CottonWorkGloves, Dress], [Hand], 37)
EnhancedGauntlet = Weapon(1, "Enhanced Gauntlet", [], SapGlove, Gauntlet[], [Hand], 37)
HolyGauntlet = Weapon(1, "Holy Gauntlet", [], [SapGlove, Cross], [Hand], 40)
CrimsonGauntlet = Weapon(1, "Crimson Gauntlet", [], [Ruby, Gauntlet], [Hand], 40)
ShatterShellGauntlet = Weapon(1, "Shatter Shell Gauntlet", [], [Gunpowder, BoneGauntlet], [Hand], 37)
MeteorGauntlet = Weapon(1, "Meteor Gauntlet", [], [Gauntlet, Meteorite], [Hand], 42)
BloodwingKnuckle = Weapon(1, "Bloodwing Knuckle", [], [WingKnuckle, Ruby], [Hand], 42)
WhiteClawPunch = Weapon(1, "White Claw Punch", [], [NineYinClaw, WhitePowder], [Hand], 43)
CorruptedScissorhands = Weapon(1, "Corrupted Scissorhands", [], [Scissorhands, Motor], [Hand], 44)
OneInchPunch = Weapon(1, "One-inch Punch", [], [AnatomyModel, EnhancedGauntlet], [Hand], 44)
WolverinesClaw = Weapon(1, "Wolverine's Claw", [], [Adamantium, IronClaw], [Hand], 44)
PoisonGlassKnuckle = Weapon(1, "Poison Glass Knuckle", [], [GlassKnuckle, Poison], [Hand], 44)
BrasilGauntlet = Weapon(1, "BrasilGauntlet", [], [EnhancedGauntlet, Oilcloth], [Hand], 44)
RulaisPalm = Weapon(1, "Rulai's Palm", [], [NirvanaGauntlet, BuddhistScripture], [Hand], 44)
PowerFist = Weapon(1, "Power Fist", [], [OgreSkin, BoneGauntlet], [Hand], 46)
DarkFrostArms = Weapon(1, "Dark Forst Arms", [], [Glacial Ice], [Hand], 46)
ImperialSilkGlove = Weapon(1, "Imperial Silk Glove", [], [SapGlove, MithrilString], [Hand], 46)
PhoenixArmsTattoo = Weapon(1, "Phoenix Arms Tattoo", [], [Gauntlet, TrueSamadhiFire], [Hand], 46)
NanorizedArms = Weapon(1, "Nanorized Arms", [], [HolyBlood, EngineeredArcaneMotor], [Hand], 60)