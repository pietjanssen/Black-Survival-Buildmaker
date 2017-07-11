import Items as i
import collections
import json
import inspect

#Basic Cloth
#Easy Ruby
#Medium Sabre
#Hard PetalTorrent
#Special BloodwingKnuckle

def optimalLocations(list):
    finalList = []
    oldDelList = []
    delList = []
    counter = 0
    while(counter < len(list)):
        current = list[counter]
        newList = []
        for location in current.location:
            if(location.name in finalList):
                newList = []
                for item in oldDelList:
                    if(location.name != item):
                        finalList.remove(item)
                break
            elif(location.name not in newList):
                newList.append(location.name)
                delList.append(location.name)
        counter+=1
        finalList = finalList + [current.name] + newList
        oldDelList = delList
        delList = []
    return finalList

class ObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "to_json"):
            return self.default(obj.to_json())
        elif hasattr(obj, "__dict__"):
            d = dict(
                (key, value)
                for key, value in inspect.getmembers(obj)
                if not key.startswith("__")
                and not inspect.isabstract(value)
                and not inspect.isbuiltin(value)
                and not inspect.isfunction(value)
                and not inspect.isgenerator(value)
                and not inspect.isgeneratorfunction(value)
                and not inspect.ismethod(value)
                and not inspect.ismethoddescriptor(value)
                and not inspect.isroutine(value)
            )
            return self.default(d)
        return obj
testItem = i.TwinSword
test = testItem.returnIngredients()
print(test)
print(testItem.returnUniqueLocations())
print(optimalLocations(test))

# Write Json objects of Items.py to file
# file = open("testfile.txt","w") 
# file.write(json.dumps(i, cls=ObjectEncoder, indent=2, sort_keys=True))