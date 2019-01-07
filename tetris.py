#Designed by Alex Palumbo
import time
import pygame
import random
pygame.init()
gameDisplay = pygame.display.set_mode((582,785))
clock = pygame.time.Clock()

#all spaces, 0=empty 1=filled 2=active
rows=[
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],  #in tuple: first is piece type, second is color
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
]
"""
for i in range(18):
    rows.append([])
    for w in range(10):
        rows[i].append([0,0])
    print rows[i]
"""
def place(x,y, color):
    colors=["tiles/color1.jpg","tiles/color2.jpg","tiles/color3.jpg","tiles/color4.jpg","tiles/color5.jpg","tiles/color6.jpg","tiles/color7.jpg"]
    piece = pygame.image.load(colors[color])
    gameDisplay.blit(piece,(x,y))

def canMoveToSide(num):
    spots=find2S()
    for spot in spots:
        if not (isRowToSideOpen(spot[0],spot[1], num)):
            return False
    return True
    
def canMoveDown():
    spots=find2S()
    for spot in spots:
        if not(isRowBelowOpen(spot[0],spot[1])):
            return False
    return True

def find2S():
    All2s=[]
    currRow=0
    currSpot=0
    for row in rows:
        for num in row:
            if num[0]==2:
                All2s.append((currRow,currSpot))
            currSpot+=1
        currSpot=0
        currRow+=1
    return All2s #(row, spot) for every 2

def find1S():                           
    All1s=[]
    currRow=0
    currSpot=0
    for row in rows:
        for num in row:
            if num[0]==1:
                All1s.append((currRow,currSpot))
            currSpot+=1
        currSpot=0
        currRow+=1
    return All1s #(row, spot) for every 1
        
def isRowBelowOpen(row,spot):
    if row==17:
        return False
    nextRow=rows[row+1]
    if nextRow[spot][0]==0 or nextRow[spot][0]==2:
        return True
    elif nextRow[spot][0]==1:
        return False
    
def isRowToSideOpen(row,spot,num):
    if num==1:  #left
        if spot==0:
            return False
        if rows[row][spot-1][0]==2 or rows[row][spot-1][0]==0:
            return True
        return False
    elif num==2:    #right
        if spot==9:
            return False
        if rows[row][spot+1][0]==2 or rows[row][spot+1][0]==0:
            return True
        return False

def updateBackgroundBoard(num):
    spots=find2S() #[(1,2), (5,9)]
    color=rows[spots[0][0]][spots[0][1]][1]
    if num==2:
        for spot in spots:              #setting new update to zero because it on top of it
            rows[spot[0]][spot[1]][0]=0
        for spot in spots:
            rows[spot[0]+1][spot[1]][0]=2
            rows[spot[0]+1][spot[1]][1]=color
    elif num==1:
        for spot in spots:
            rows[spot[0]][spot[1]][0]=1
    elif num==3:
        for spot in spots:
            rows[spot[0]][spot[1]][0]=0
        for spot in spots:   
            rows[spot[0]][spot[1]-1][0]=2
            rows[spot[0]][spot[1]-1][1]=color
    elif num==4:
        for spot in spots:
            rows[spot[0]][spot[1]][0]=0
        for spot in spots:
            rows[spot[0]][spot[1]+1][0]=2
            rows[spot[0]][spot[1]+1][1]=color

def updateVisualBoard():
    both=[find1S(),find2S()]
    for each in both:
        if len(each)>0:
            for spot in each:
                x=146+(29*spot[1])
                y=192+(29*spot[0])
                color=rows[spot[0]][spot[1]][1]
                place(x,y,color)

def checkLineWin():
    rowNum=0
    lines=0
    score=0
    for row in rows:
        tot=0
        for num in row:
            tot+=num[0]
        if tot==10:
            breakLine(rowNum)
            dropDownAllRows(rowNum)
            lines+=1
            score+=1
        rowNum+=1
    return (lines, score)

def breakLine(line):
    for i in range(10):
        rows[line][i][0]=0
        
def dropDownAllRows(rowNum):
    ones=find1S()
    for spot in ones:
        if spot[0]<rowNum:
            rows[spot[0]][spot[1]][0]=0
    for spot in ones:
        if spot[0]<rowNum:
            rows[spot[0]+1][spot[1]][0]=1
    
pieceRotation=0    
def spawnNewPiece(score,highscore):
    global pieceRotation
    pieceRotation=0
    piece,color= pickPiece(1)
    lpiece=piece.split(",")
    if checkSpawnLose(lpiece,5):
        for i in range(len(lpiece)):            #how many rows
            for w in range(len(lpiece[0])):
                if lpiece[i][w]=="1":
                    rows[i][5+w][0]=2
                    rows[i][5+w][1]=color
    else:
        playAgain(score,highscore)
        return 1

def checkSpawnLose(lpiece,num):
    for i in range(len(lpiece)):
        for w in range(len(lpiece[0])):
            if lpiece[i][w]=="1":
                if rows[i][num+w][0]==1:
                    return False
    return True

def playAgain(score,highscore):
    updateVisualBoard()
    updateScore(score, score)
    updateHighscore(highscore)
    gameDisplay.blit(pygame.image.load('images/playAgainButton.png'),(231,360))
    pygame.display.update()
    open("files/highscore.txt","w").write(str(highscore))
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    resetGame()
                    return
            if event.type == pygame.QUIT:
                pygame.quit()
                
def resetGame():
    saveNum=0
    pieceRotation=0
    count1=count2=0
    for row in rows:    #clear board
        for item in row:
            for i in range(2):
                rows[count1][count2][i]=0
            count2+=1
        count2=0
        count1+=1
    updateVisualBoard()

saveNum=0
def pickPiece(rotateDir):
    global pieceRotation, saveNum
    pieces=[
    ["110,011",
    "01,11,10",
    "110,011",
    "01,11,10"],
    ["1,1,1,1",
    "1111",
    "1,1,1,1",
    "1111"],
    ["11,11",
    "11,11",
    "11,11",
    "11,11"],
    ["011,110",
    "10,11,01",
    "011,110",
    "10,11,01"],
    ["10,10,11",
    "111,100",
    "11,01,01",
    "001,111"],
    ["01,01,11",
    "100,111",
    "11,10,10",
    "111,001"],
    ["111,010",
    "01,11,01",
    "010,111",
    "10,11,10"]
    ]
    num=random.randint(0,6)
    if rotateDir==1:
        saveNum=num
        return pieces[num][0],num
    elif rotateDir==2:      #left
        if pieceRotation!=3:
            pieceRotation+=1
        else:
            pieceRotation=0
        return pieces[saveNum][pieceRotation]   #pos + up
    elif rotateDir==3:
        if pieceRotation==0:
            pieceRotation=3
        else:
            pieceRotation+=-1

def rotatePiece():
    piece = pickPiece(2)
    lpiece=piece.split(",")
    spots=find2S()
    color=rows[spots[0][0]][spots[0][1]][1]
    x=y=20
    for spot in spots:
        if spot[0]<y:
            y=spot[0]
        if spot[1]<x:
            x=spot[1]
    if canRotate(x,y,len(lpiece),len(lpiece[0])):
        for spot in spots:
            rows[spot[0]][spot[1]][0]=0
        for i in range(len(lpiece)):
            for w in range(len(lpiece[0])):
                if lpiece[i][w]=="1":
                    rows[y+i][x+w][0]=2
                    rows[y+i][x+w][1]=color

def canRotate(x,y,i,w):
    testRows=rows[:]
    if x+w>10 or y+i>18 or rows[y+i-1][x+w-1][0]==1:
        pickPiece(3)
        return False
    return True

def updateScore(lines, score):
    pygame.font.init() 
    font = pygame.font.Font('fonts/arial.ttf', 45)
    block = font.render(str(score), True, (0, 0, 0))
    rect = block.get_rect()
    rect.center = (510, 250)
    gameDisplay.blit(block, rect)

def updateHighscore(highscore):
    pygame.font.init() 
    font = pygame.font.Font('fonts/arial.ttf', 45)
    block = font.render(str(highscore), True, (0, 0, 0))
    rect = block.get_rect()
    rect.center = (510, 465)
    gameDisplay.blit(block, rect)

def game_loop():
    global board
    gameExit = False
    yCount=0
    lines=0
    score=0
    highscore = int(open("highscore.txt","r").read())
    spawnNewPiece(score,highscore)
    while not gameExit:
        gameDisplay.blit(pygame.image.load('images/background4.jpg'),(0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if canMoveToSide(1):
                        updateBackgroundBoard(3)
                if event.key == pygame.K_RIGHT:
                    if canMoveToSide(2):
                        updateBackgroundBoard(4)
                if event.key == pygame.K_UP:
                    rotatePiece()
                if event.key == pygame.K_DOWN:  #ablitliy to hold down, left, or right
                    if canMoveDown():
                        updateBackgroundBoard(2)
                if event.key == pygame.K_SPACE:
                    while canMoveDown():
                        updateBackgroundBoard(2)
            if event.type == pygame.QUIT:
                pygame.quit()
                
        if yCount==7:
            if canMoveDown():
                updateBackgroundBoard(2)
            else:
                updateBackgroundBoard(1)
                lineWin = checkLineWin()
                if type(lineWin)!=None:
                    lines+=lineWin[0]
                    score+=lineWin[1]
                    if score>highscore:
                        highscore=score
                if spawnNewPiece(score,highscore)==1:
                    return
            yCount=0
        yCount+=1
        updateScore(lines, score)
        updateHighscore(highscore)
        updateVisualBoard()
        pygame.display.update()
        clock.tick(30)
        
def splashScreen():
    timer=0
    while 1:
        gameDisplay.blit(pygame.image.load('images/splash.jpg'),(0,0))
        timer+=1
        if timer>60:
            return
        pygame.display.update()

def startScreen():
    while 1:
        gameDisplay.blit(pygame.image.load('images/background4.jpg'),(0,0))
        gameDisplay.blit(pygame.image.load('images/startButton.png'),(231,360))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                if event.type == pygame.QUIT:   #quit key
                    pygame.quit()
                    
        pygame.display.update()
        clock.tick(30)

def gameLooper():
    while 1:
        game_loop()
    gameLooper()

splashScreen()
startScreen()
gameLooper()
    
pygame.quit()

#lose
#calculate score vs lines
