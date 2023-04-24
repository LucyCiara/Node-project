import random
thing = 0
x = 0
y = 0
square = []
squarePos = []
squareSubPos = []
tang = True
dong = 0
scale = int(input("Scale: "))
obstiY = False
obstiX = False
history = []
regX = False
regY = False
possibility = True
impMap = []
thingHist = []
skipCal = False


def makeSquare():
    #makes a list and sublist which contains random intengers
    for i in range(0, scale):
        square.append([])
        for j in range(0, scale):
            if(i == 0 and j == 0):
                square[i].append(0)
            else:
                dong = random.randint(0, 5)
                if dong == 3:
                    square[i].append("x")
                else:
                    square[i].append(random.randint(0, 100))

def makeImpMap():
    #makes a second hidden map for notation of dead ends
    for i in range (0, scale):
        impMap.append([])
        for j in range (0, scale):
            impMap[i].append(square[i][j])
    


def makeSquarePos():
    #makes a copy of square with a node replaced by A, representing the algorithm's position
    global x, y, squarePos, square, squareSubPos
    squarePos.clear()
    for i in range (0, scale):
        squarePos.append([])
        for j in range (0, scale):
            squarePos[i].append(square[i][j])
    squarePos[x][y] = "A"



def update():
    #prints the contents of the sublists in a way that makes it look like a grid
    #with the position of the algorithm inside it represented by an "A"
    global x, y, squarePos, square, thing, skipCal
    makeSquarePos()

    #prints its x and y value as well as its total calculated number of points
    if skipCal == False:
        thing = thing + square[x][y]
        thingHist.append(thing)
    else:
        skipCal = False



def squarePrint():
    #prints the contents of the sublists in a way that makes it look like a grid
    for i in range(0, scale):
        row = ""
        for j in range(0, scale):
            row = row + "\t" + str(square[j][i])
        print(row)
        print()
    print("-----------------------------------------------")



def move():
    #chooses whether to increase x or y to get as few points as possible
    global x, y, thing
    if square[x+1][y] < square[x][y+1]:
        history.append(1)
    else:
        history.append(-1)
    

        

def uniCheck():
    #checks whether it is near a border, or an obstacle
    global obstiX, obstiY, x, y
    if y == scale - 1:
        obstiY = True
    elif impMap[x][y+1] == "x":
        obstiY = True
    else:
        obstiY = False
    if x == scale - 1:
        obstiX = True
    elif impMap[x+1][y] == "x":
        obstiX = True
    else:
        obstiX = False


def checkHalf():
    #moves along the uninterrupted direction
    global obstiX, x, y
    if obstiX:
        history.append(-1)
    else:
        history.append(1)
    



def checkFull():
    #goes back in time using a quantum flux powered time wheel along our time branch
    global obstiX, obstiY, x, y, regX, regY, possibility, thing, skipCal
    if x == 0 and y == 0:
        possibility = False
    else:
        impMap[x][y] = "x"
        del history[-1]
        del thingHist[-1]
        thing = thingHist[-1]
        skipCal = True

    
     


def checkAct():
    #executes the function for when there's one blockade when there's one blockade,
    #and executes the function for when there's two blockades when there are two
    global obstiX, obstiY, x, y
    uniCheck()
    if True in [obstiX, obstiY]:
        if False in [obstiX, obstiY]:
            checkHalf()
        else:
            checkFull()
    else:
        move()
    
    #interprets history in position
    x = 0
    y = 0
    for i in range (0, len(history)):
        if history[i] == 1:
            x = x + 1
        else:
            y = y + 1
    update()
        
            

makeSquare()

makeImpMap()

squarePrint()

update()


while tang == True:
    #executes the uni check function if it isn't finished. if it is, it disables the while loop.
    if (len(history))/2+1 < scale and possibility == True:
        checkAct()
    else:
        tang = False
    
if possibility == False:
    print("Det finnes ingen utvei")
else:
    print(thing)



