import os, json
from pymongo import MongoClient

OutputDirectory = "./OutputDirectory"
if not os.path.exists(OutputDirectory):
    os.makedirs(OutputDirectory)

ConnectionString = "mongodb+srv://admin:admin1@cluster0-ka88r.mongodb.net/test?retryWrites=true"
client = MongoClient(ConnectionString)

Logs = client["holotours"]["tours"]

SeenUserIDs = []
Data = []

i = 0
for D in Logs.find({}):
    id = D["_id"]
    id = str(id)
    del D["_id"]
    D["_id"] = id

    if D["userID"] not in SeenUserIDs:
        SeenUserIDs.append(D["userID"])
        Data.append([])

    i = SeenUserIDs.index(D["userID"])

    Data[i].append(D)



TotalLen = 0
#Now Append these into the arrays
for i in range(len(SeenUserIDs)):
    UserID = SeenUserIDs[i]
    Path = OutputDirectory + "/User-" + str(UserID) + ".json"
    CurrentData = Data[i]
    PreData = []
    try:
        with open(Path) as f:
            PreData = json.load(f)

        print("Preloaded Length " + str(len(PreData)))
    except:
        pass

    #combine data in with old data
    #check for previous data
    for D in CurrentData:
        Match = False
        for P in PreData:
            if(D["_id"] == P["_id"]):
                if(str(D["timeStamp"]) == str(P["timeStamp"])):
                    if(str(D["userID"]) == str(P["userID"])):
                        Match = True
                        break

        #if no match add it to PreData to be Written out
        if(Match == False):
            PreData.append(D)

    #Write out Json Data
    with open(Path, 'w') as outfile:
        json.dump(PreData, outfile)
