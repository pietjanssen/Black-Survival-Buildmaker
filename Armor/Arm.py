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
Thimble = Armor(1, "Thimble", [l.Hotel], [], [Arm], 1)
Bracelet = Armor(1, "Bracelet", [l.Alley, l.Slum, l.Uptown], [], [Arm], 3)
ReserveeArmband = Armor(1, "Reservee Armband", [l.School], [], [Arm], 3)
Watch = Armor(1, "Watch", [l.Lighthouse, l.FireStation, l.Hotel], [], [Arm], 3)
ArmWarmers = Armor(1, "Arm Warmers", [l.School, l.Slum, l.Uptown], [], [Arm], 5)
HeartbeatSensor = Armor(1, "Heartbeat Sensor", [l.Random], [], [Arm], 10)
#Armor
Bracer = Armor(1, "Bracer", [], [ArmWarmers, ReliefPatch], [Arm], 12)
LeatherShield = Armor(1, "LeatherShield", [], [Leather, TurtleShell], [Arm], 12)
Wristband = Armor(1, "Wristband", [], [Bandage, Rubber], [Arm], 20)
Bazuband = Armor(1, "Bazuband", [], [ArmWarmers, IronSheet], [Arm], 20)
CrimsonBracelet = Armor(1, "Crimson Bracelet", [], [Bracelet, Ruby], [Arm], 20)
Sheath = Armor(1, "Sheath", [], [Leather, IronSheet], [Arm], 25)
SquadLeaderArmband = Armor(1, "Squad Leader Armband", [], [ReserveeArmband, Needle], [Arm], 25)
SwordStoppers = Armor(1, "Sword Stoppers", [], [Bazuband, IronClaw], [Arm], 25)
OPG = Armor(1, "OPG", [], [OgreSkin, Gauntlet], [Arm], 30)
CaptainsShield = Armor(1, "Captain's Shield", [], [TurtleShell, Mithril], [Arm], 30)
SteelShield = Armor(1, "Steel Shield", [], [Leather Shield, Steel], [Arm], 30)
BraceletOfSkadi = Armor(1, "Bracelet of Skadi", [], [GlacialIce, Bracelet], [Arm], 35)
Radar = Armor(1, "Radar", [], [Blueprint, HeartbeatSensor], [Arm], 35)
GalaxyWatch = Armor(1, "Galaxy Watch", [], [CellPhone, Watch], [Arm], 45)