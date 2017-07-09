import Location as l

class SFood:
    def __init__(self, quantity, name, location, ingredients, stamina):
        self.quantity = quantity
        self.name = name
        self.location = location
        self.ingredients = ingredients
        self.stamina = stamina

#Base food
Water  = SFood(3, "Water", [l.Pond, l.FireStation, l.Well, l.Beach, l.Forest, l.Dock, l.Random], [], 10)
Ice = SFood(1, "Ice", [l.Well, l.Hotel], [], 10)
SportsDrink = SFood(1, "Sports Drink", [l.Lighthouse, l.ArcheryRange], [], 10)
CarbonatedWater = SFood(1, "Carbonated Water", [l.Well], [], 13)
TobaccoLeaves = SFood(1, "Tobacco Leaves", [], [], 15)
Coffee = SFood(1, "Coffee", [l.Uptown], [], 20)
LiverSupplementPill = SFood(1, "Liver Supplement Pill", [l.Hospital], [], 20)
Honey = SFood(1, "Honey", [l.TownHall, l.Hotel], [], 22)
Baccus = SFood(1, "Baccus", [l.Slum], [], 25)
TreeOfLife = SFood(1, "Tree of Life", [l.Random], [], 4)
#Food
IceWater = SFood(8, "Ice Water", [], [Ice, Water], 15)
SorghumWine = SFood(1, "Sorghum Wine", [], [Alcohol, Lighter], 30)
WaterBottle = SFood(3, "1.5L Water Bottle", [], [Water, PlasticBottle], 33)
KoaliangLiquor = SFood(4, "Laoliang Liquor", [], [SorghumWine, Lighter], 36)
HalfFilledGlass = SFood(2, "Half-filled Glass", [], [Water, GlassCup], 37)
HoneyWater = SFood(2, "Honey Water", [], [Honey, Water], 42)
Soju = SFood("Soju", [], [Water, Alcohol], 44)
OrientalRaisinWater = SFood(3, "Oriental Raisin Water", [], [Branch, BoilingWater], 46)
HerbalLiquor = SFood(3, "Herbal Liquor", [], [SorghumWine, OrientalGrass], 75)
Whiskey = SFood(1, "Whiskey", [], [], 120)
SparklingSoju = SFood(4, "Sparkling Soju", [], [CarbonatedWater, Soju], 35)
IonizedSoju = SFood(3, "Ionized Soju", [], [SportsDrink, Soju], 40)
HotHoneyWater = SFood(4, "Hot Honey Water", [], [Honey, BoilingWater], 42)
BurdockTea = SFood(3, "Burdock Tea", [], [Burdock, BoilingWater], 45)
OrangeAde = SFood(5, "Orange Ade", [], [Orange, CarbonatedWater], 50)
Americano = SFood(3, "Americano", [], [BoilingWater, Coffee], 55)
HotChocolate = SFood(3, "Hot Chocolate", [], [Chocolate, BoilingWater], 55)
CoffeeLiqueur = SFood(2, "Coffee Liqueur", [], [Alcohol, Coffee], 60)
IceCoffee = SFood(4, "Ice Coffee", [], [Coffee, Ice], 70)
FlowerLiquor = SFood(3, "Flower Liquor", [], [Flower, SorghumWine], 90)
Cigarette = SFood(10, "Cigarette", [], [TobaccoLeaves, Lighter], 54)
Cocktail = SFood(10, "Cocktail", [], [Whiskey, Orange], 90)
CoffeeLiqueur = SFood("Coffee Liqueur", [], [Alcohol, Coffee], 60)