import json
import os
import subprocess
from Person import Person
from Game import Game
peopleWithKey = {"people":[]}
gamesWithKey = {"games":[]}

def readFile(path):
    try:
        with open(path) as json_file:
            myjson = json.load(json_file) # load json file if present
        return myjson
    except Exception:
        return False

def writeObjToFile(path,jsonObj):
    try:
        with open(path, "w") as f:
            json.dump(jsonObj, f, indent=4) #write people list
    except Exception:
        return False

def hasPerson(mylist,name): # check if there is a json object with the same 'name' as arguement
    found = False
    for x in mylist:
        if str(x["name"]).lower() == str(name).lower():
            return True
    return found

def getAge(mylist,name): # return the age of the given arguement 'name', otherwise return 0
    for x in mylist:
        if str(x["name"]).lower() == str(name).lower():
            return x["age"]
    return 0

def hasGame(mylist,name): # check if there is a json object with the same 'title' as arguement
    found = False
    for x in mylist:
        if str(x["title"]).lower() == str(name).lower():
            return True
    return found

def runGame(mylist,title): # run game file either through steam or through os.startfile
    for x in mylist:
        if str(x["title"]).lower() == str(title).lower():
            if "steam://rungameid/" in x["executable"]:
                temp = x["executable"].split("steam://rungameid/")
                print(temp)
                subprocess.Popen("C:/Program Files (x86)/Steam/Steam.exe -applaunch {}".format(temp))
            else:
                os.startfile(x["executable"])
            break


if not(readFile('data/people.json')): # read people file
    #writePeopleToFile(peopleWithKey)
    writeObjToFile('data/people.json',peopleWithKey) # otherwise create one
    print("Error. People file not found. File created!")
else:
    peopleWithKey = readFile('data/people.json')
    print("People file found and loaded")
print(peopleWithKey)

if not(readFile('data/games.json')): # read game file
    #writeGamesToFile(gamesWithKey)
    writeObjToFile('data/games.json',gamesWithKey) # otherwise create one
    print("Error. Games file not found. File created!")
else:
    gamesWithKey = readFile('data/games.json')
    print("Games file found and loaded")
print(gamesWithKey)

for x in peopleWithKey["people"]: #loop over people and print their 'name'
    print(x["name"])

p4 = Person("profile99",102)
if not(hasPerson(peopleWithKey["people"],p4.name)):
    peopleWithKey["people"].append(p4.__dict__)
else:
    print("person already exists. Will not be added to the file".format())

#writePeopleToFile(peopleWithKey)
writeObjToFile('data/people.json',peopleWithKey)
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

g1 = Game("tester","D:/Work/backups/Apps/Game Profile Manager/Game Profile Manager.exe","C:/Users/user/AppData/Local/SessionGame/Saved/SaveGames")
if not(hasGame(gamesWithKey["games"],g1.title)):
    gamesWithKey["games"].append(g1.__dict__)
else:
    print("game already exists. Will not be added.")

writeObjToFile('data/games.json',gamesWithKey)

runGame(gamesWithKey["games"],"Session.")