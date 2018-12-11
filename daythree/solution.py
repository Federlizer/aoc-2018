data = open("./input.txt", "r")

claims = data.read().split("\n")

data.close()

UNVISITED = 0
VISITED = 1
COUNTED = 2

fabric = [[UNVISITED for x in range(1000)] for y in range(1000)]

duplicateCount = 0

def countClaim(claim, fabric):
    coords = claim.split("@")[1].split(":")
    count = 0
    
    startPoints = coords[0].split(",")
    startPointX = int(startPoints[0].strip())
    startPointY = int(startPoints[1].strip())

    sizes = coords[1].split("x")
    sizeX = int(sizes[0].strip())
    sizeY = int(sizes[1].strip())
    
    for y in range(startPointY, startPointY + sizeY):
        for x in range(startPointX, startPointX + sizeX):
            if fabric[x][y] == UNVISITED:
                fabric[x][y] = VISITED
            elif fabric[x][y] == VISITED:
                fabric[x][y] = COUNTED
                count += 1
            else:
                continue
    return count

for claim in claims:
    duplicateCount += countClaim(claim, fabric)

print(duplicateCount)