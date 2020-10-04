import json
from Person import Person
#people = {}
peopleWithKey = {"people":[]}

def readPeopleFromFile():
    try:
        with open("data\people.json") as json_file:
            myjson = json.load(json_file) # load json file into loaded_users (will be a list)
        return myjson
    except Exception:
        return False

def writePeopleToFile(jsonObj):
    try:
        with open("data\people.json", "w") as f:
            json.dump(jsonObj, f, indent=4) #write users list to file
    except Exception:
        return False

def hasPerson(mylist,name): # check if their is a json object with the same name as arguement
    found = False
    for x in mylist:
        if str(x["name"]).lower() == str(name).lower():
            return True
    return found

def getAge(mylist,name): # return the age of the given arguement name, otherwise return 0
    for x in mylist:
        if str(x["name"]).lower() == str(name).lower():
            return x["age"]
    return 0

if not(readPeopleFromFile()):
    writePeopleToFile(peopleWithKey)
    print("Error. People file not found. File created!")
else:
    peopleWithKey = readPeopleFromFile()
    print("People file found and loaded")
print(peopleWithKey)

for x in peopleWithKey["people"]:
    print(x["name"])

if not(hasPerson(peopleWithKey["people"],"profile2")):
    p4 = Person("profile2",98)
    json_p4 = json.loads(json.dumps(p4.__dict__))
    peopleWithKey["people"].append(json_p4)
else:
    print("person already exists. Will not be added to the file".format())

writePeopleToFile(peopleWithKey)
print(peopleWithKey)

#p1 = Person("naz",35)
#p2 = Person("joe",30)
#p3 = Person("bev",26)

#json_p1 = json.loads(json.dumps(p1.__dict__))
#json_p2 = json.loads(json.dumps(p2.__dict__))
#json_p3 = json.loads(json.dumps(p3.__dict__))

#people.append(json_p1)
#people.append(json_p2)
#people.append(json_p3)

