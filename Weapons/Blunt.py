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
BuddhistScripture = Weapon(1, "Buddhist Scripture", [l.Temple], [], [Blunt], 5)
Fan = Weapon(1, "Fan", [l.TownHall], [], [Blunt], 5)
RippedScroll1 = Weapon(1, "Ripped Scroll -1", [l.Slum], [], [Blunt], 5)
RippedScroll2 = Weapon(1, "Ripped Scroll -2", [l.Hotel], [], [Blunt], 5)
Scarf = Weapon(1, "Scarf", [l.Trail], [], [Blunt], 5)
AnatomyModel = Weapon(1, "Anatomy Model", [l.Hospital, l.School], [], [Blunt], 5)
Branch = Weapon(1, "Branch", [l.Cemetary, l.Trail, l.Forest], [], [Blunt], 5)
ScrollsOfDongYi = Weapon(1, "Scrolls of DongYi", [l.Hospital], [], [Blunt], 5)
CrudeBat = Weapon(1, "Crude Bat", [], [], [Blunt], 5)
ShortRod = Weapon(1, "Short Rod", [l.Chapel, l.Pond], [], [Blunt], 6)
Bamboo = Weapon(1, "Bamboo", [l.Cemetary, l.Forest, l.Trail], [], [Blunt], 8)
FryingPan = Weapon(1, "Frying Pan", [l.Slum, l.Hotel], [], [Blunt], 6)
WoodenFish = Weapon(1, "Wooden Fish", [l.Temple], [], [Blunt], 8)
SteelPipe = Weapon(1, "Steel Pipe", [l.Factory], [], [Blunt], 8)
SteelChain = Weapon(1, "Steel Chain", [l.Uptown, l.Slum, l.Hotel, l.Alley], [], [Blunt], 8)
Whip = Weapon(1, "Whip", [l.Cemetary, l.Hotel, l.Lighthouse], [], [Blunt], 10)
Bat = Weapon(1, "Bat", [l.School], [], [Blunt], 10)
Hammer = Weapon(1, "Hammer", [l.FireStation, l.TownHall, l.Dock, l.Hospital], [], [Blunt], 12)
LongRod = Weapon(1, "Long rod", [l.Trail, l.Pond], [], [Blunt], 14)

#Weapons
SolderingIron = Weapon(1, "Soldering Iron", [], [Nail, ElectronicParts], [Blunt], 5)
SpearHandle = Weapon(1, "Spear Handle", [l.Lighthouse, l.Temple], [Bamboo, PianoWire], [Blunt], 6)
StoneAxe = Weapon(1, "Stone Axe", [], [Stone, Bamboo], [Blunt], 10)
FlagPole = Weapon(1, "Flag Pole", [], [LongRod, Nail], [Blunt], 10)
HeatedSteelPipe = Weapon(1, "Heated Steel Pipe", [], [SteelPipe, Lighter], [Blunt], 15)
FeatherDuster = Weapon(1, "Feather Duster", [], [Feather, SpearHandle], [Blunt], 15)
MorningStar = Weapon(1, "MorningStar", [], [LongRod, IronBall], [Blunt], 15)
HeatedFryingPan = Weapon(1, "Heated Frying Pan", [], [FryingPan, Lighter], [Blunt], 15)
GoblinBat = Weapon(1, "Goblin Bat", [], [ShortRod, Nail], [Blunt], 15)
Tonfa = Weapon(1, "Tonfa", [], [CottonWorkGloves, ShortRod], [Blunt], 18)
ChainRod = Weapon(1, "Chain Rod", [], [SteelChain, ShortRod], [Blunt], 20)
HighVoltageLine = Weapon(1, "High Voltage Line", [], [DeadBattery, Wire], [Blunt], 20)
Bullwhip = Weapon(1, "Bullwhip", [], [Razor, Whip], [Blunt], 20)
SafetyRod = Weapon(1, "Safety Rod", [], [], [Blunt], 20)
Warhammer = Weapon(1, "Warhammer", [], [Hammer, SpearHandle], [Blunt], 22)
LeatherWhip = Weapon(1, "Leather Whip", [], [Leather, Scissors], [Blunt], 24)
ClawHammer = Weapon(1, "Claw Hammer", [], [], [Blunt], 25)
Iron Mace = Weapon(1, "Iron Mace", [], [StoneAxe, SteelChain], [Blunt], 30)
SpikedBat = Weapon(1, "Spiked bat", [], [Bat, Nail], [Blunt], 34)
TorchHold = Weapon(1, "Torch Hold", [], [Oilcloth, Bamboo], [Blunt], 26)
Umbrella = Weapon(1, "Umbrella", [], [Oilcloth, LongRod], [Blunt], 32)
RopeCuffs = Weapon(1, "Rope Cuffs", [], [StallionMedal, Whip], [Blunt], 32)
LightningWhip = Weapon(1, "Lightning Whip", [], [Bullwhip, DeadBattery], [Blunt], 32)
Torch = Weapon(1, "Torch", [], [TorchHold, Lighter], [Blunt], 32)
Nunchaku = Weapon(1, "Nunchaku", [], [ChainRod, ShortRod], [Blunt], 32)
ThornWhip = Weapon(1, "Thorn Whip", [], [SpikedPlank, Whip], [Blunt], 32)
ElectricWhip = Weapon(1, "Electic Whip", [], [HighVoltageLine, Whip], [Blunt], 34)
UsurperWarhammer = Weapon(1, "Usurper Warhammer", [], [Warhammer, Adamantium], [Blunt], 34)
SteelTonfa = Weapon(1, "Steel Tonfa", [], [Tonfa, Steel], [Blunt], 34)
WhiteCraneFan = Weapon(1, "White Crane Fan", [], [Feather, Fan], [Blunt], 34)
Flail = Weapon(1, "Flail", [], [ChainRod, IronBall], [Blunt], 38)
GolfClub = Weapon(1, "Golf Club", [], [HeatedSteelPipe, Hammer], [Blunt], 38)
GoldenWhip = Weapon(1, "Golden Whip", [], [Bullwhip, Gold], [Blunt], 40)
TripleNunchaku = Weapon(1, "Triple Nunchaku", [], [Nunchaku, ChainRod], [Blunt], 43)
DoubleNunchaku = Weapon(1, "Double Nunchaku", [], [Nunchaku, Bullwhip], [Blunt], 43)
BeamTonfa = Weapon(1, "Beam Tonfa", [], [SteelTonfa, LaserPointer], [Blunt], 40)
Vajra = Weapon(1, "Vajra", [], [TreeOfLife, SpikedBat], [Blunt], 41)
KGBAgentUmbrella = Weapon(1, "KGB Agent Umbrella", [], [Umbrella, Poison], [Blunt], 44)
RedMuffler = Weapon(1, "Red Muffler", [], [Scarf, HolyBlood], [Blunt], 46)
TitanHammer = Weapon(1, "Titan Hammer", [], [Hammer, OgreSkin], [Blunt], 46)
BananaLeafFan = Weapon(1, "Banana Leaf Fan", [], [WhiteCraneFan, PowderOfLife], [Blunt], 46)
VillainousWhip = Weapon(1, "'Villainous Whip'", [], [LightningWhip, ElectricWhip], [Blunt], 46)
HammerOfThor = Weapon(1, "Hammer of Thor", [], [UsurperWarhammer, HighVoltageLine], [Blunt], 48)
FangMace = Weapon(1, "Fang Mace", [], [ArcaneStone, GoblinBat], [Blunt], 48)
Gleipnir = Weapon(1, "Gleipnir", [], [RopeCuffs, ThornWhip], [Blunt], 48)
StatueOfLiberty = Weapon(1, "Statue of Liberty", [], [Torch, AnatomyModel], [Blunt], 48)
MagicStick = Weapon(1, "Magic Stick", [], [Warhammer, MoonlightPendant], [Blunt], 48)
MonkeyKingBar = Weapon(1, "Monkey King Bar", [], [NanorizedArms, SpearHandle], [Blunt], 65)