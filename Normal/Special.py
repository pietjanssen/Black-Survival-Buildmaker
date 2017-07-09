import Locations as l

class Ingredient:
    def __init__(self, quantity,name, location, ingredients):
        self.quantity = quantity
        self.name = name
        self.ingredients = ingredients
        self.location = location 

#Base Ingredients
Silencer = Special(1, "Silencer", [l.Forest, l.Factory], [])
#Ingredients
LaptopFaulty = Special(1, "Laptop(fault circuit)", [], [LCDPanel, LaptopBroken])
SystemShutdownCode = Special(1, "System Shutdown Code", [], [CDPlayer, Blueprint])
ClangClatter = Special(1, "ClangClatter", [], [Can, Plate])
LaptopDead = Special(1, "Laptop(dead battery)", [], [SolderingIron, LaptopFaulty])
Stimulant = Special(1, "Stimulant", [], [Coffee, Baccus])
SearingPalmScroll = Special(1, "Searing Palm Scroll", [], [AnatomyModel, Blueprint])
SmokeBomb = Special(1, "Smoke Bomb", [], [FlourBomb, Gunpowder])
Laptop = Special(1, "Laptop", [], [IonBattery, LaptopDead])
NetworkPC = Special(1, "Network PC", [], [CellPhone, Laptop])