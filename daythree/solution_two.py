import pprint
data = open("./input.txt", "r")

claims = data.read().split("\n")

data.close()

UNCLAIMED = 0
OVERLAPPING = -1

fabric = [[UNCLAIMED for x in range(1000)] for y in range(1000)]

def claimFabric(claim, fabric):
    claimN = int(claim.split("@")[0][1:2])
    coords = claim.split("@")[1].split(":")
    
    startPoints = coords[0].split(",")
    startPointX = int(startPoints[0].strip())
    startPointY = int(startPoints[1].strip())

    sizes = coords[1].split("x")
    sizeX = int(sizes[0].strip())
    sizeY = int(sizes[1].strip())

    for y in range(startPointY, startPointY + sizeY):
        for x in range(startPointX, startPointX + sizeX):
            if fabric[x][y] == UNCLAIMED:
                fabric[x][y] = claimN
            else:
                fabric[x][y] = OVERLAPPING
    
def checkClaims(claim, fabric):
    claimN = int(claim.split("@")[0][1:2])
    coords = claim.split("@")[1].split(":")
    
    startPoints = coords[0].split(",")
    startPointX = int(startPoints[0].strip())
    startPointY = int(startPoints[1].strip())

    sizes = coords[1].split("x")
    sizeX = int(sizes[0].strip())
    sizeY = int(sizes[1].strip())

    wantedSize = sizeX * sizeY
    actualSize = 0

    for y in range(startPointY, startPointY + sizeY):
        for x in range(startPointX, startPointX + sizeX):
            spot = fabric[x][y]
            
            if spot == claimN:
                actualSize += 1

    return actualSize == wantedSize


for claim in claims:
    claimFabric(claim, fabric)

for claim in claims:
    if checkClaims(claim, fabric):
        print(claim)