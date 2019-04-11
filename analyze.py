import json, os
import matplotlib.pyplot as plt

PATH = './OutputDirectory'
jsonPaths = [os.path.join(dp, f) for dp, dn, filenames in os.walk(PATH) for f in filenames if os.path.splitext(f)[1] == '.json']




'''
    for each participant, plot x, y position
    orientation versus time

    

'''



def GenerateScatter(name, data):
    x = []
    z = []
    y = []
    for d in data:
        x.append(d["x-coordinate"])
        y.append(d["y-coordinate"])
        z.append(d['z-coordinate'])
    plt.scatter(x,z)
    plt.ylabel("Entrance Side")
    plt.xlabel("Right Wall")
    plt.title(name)
    plt.show()

i = 0
for p in jsonPaths:
    i += 1
    data = None
    with open(p) as json_file:
        data = json.load(json_file)

    GenerateScatter(str("User " + str(i)), data)
