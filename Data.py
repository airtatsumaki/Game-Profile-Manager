import json

class Data:
    def __init__(self):
        self.userList = []
        self.userFile = 'resources/profiles.json'
        self.gameList = []
        self.gameFile = 'resources/games.json'
        if self.readFile(self.userFile):
            self.userJSON = self.readFile(self.userFile)
        else:
            self.userJSON = {"profiles":[]}
        for x in self.userJSON["profiles"]:
             self.userList.append(x["name"])
        
        if self.readFile(self.gameFile):
            self.gameJSON = self.readFile(self.gameFile)
        else:
            self.gameJSON = {"games":[]}
        for x in self.gameJSON["games"]:
             self.gameList.append(x["title"])

    def readFile(self, path):
        try:
            with open(path) as json_file:
                myjson = json.load(json_file) # load json file if present
            return myjson
        except Exception:
            return False
    
    def writeObjToFile(self, path, jsonObj):
        try:
            with open(path, "w") as f:
                json.dump(jsonObj, f, indent=4) #write people list
        except Exception:
            return False
    
    def getUserList(self):
        return self.userList
    
    def getGameList(self):
        return self.gameList

    def refreshUserList(self):
        self.userList = []
        for x in self.userJSON["profiles"]:
            self.userList.append(x["name"])
        return self.userList

    def refreshGameList(self):
        self.gameList = []
        for x in self.gameJSON["games"]:
            self.gameList.append(x["title"])
        print("new list = {}".format(self.gameList))
        return self.gameList

    def hasUser(self, user):
        return {'name': user} in self.userJSON["profiles"]

    def hasGame(self, game):
        result = False
        for x in self.gameJSON["games"]:
            if x['title'] == game:
                result = True
                break
        return result

    def addUser(self, user):
        self.userJSON["profiles"].append({'name': user})
        print("user " + user + " added to the file")
        self.writeObjToFile(self.userFile, self.userJSON)
        return self.refreshUserList()
    
    def deleteUser(self, user):
        self.userJSON["profiles"].remove({'name': user})
        print("user " + user + " removed from file")
        self.writeObjToFile(self.userFile, self.userJSON)
        return self.refreshUserList()
    
    def addGame(self, gameTitle, gamePath, savePath):
        self.gameJSON["games"].append({"title": gameTitle, "executable": gamePath, "saveLocation": savePath, "lastPlayer": ""})
        print("game " + gameTitle + " added to the file")
        self.writeObjToFile(self.gameFile, self.gameJSON)
        return self.refreshGameList()

    def deleteGame(self, gameTitle):
        for x in self.gameJSON["games"]:
            print("x is {} ".format(x))
            if x["title"] == gameTitle:
                print("game found, delete")
                self.gameJSON["games"].remove(x)
                self.writeObjToFile(self.gameFile, self.gameJSON)
        return self.refreshGameList()