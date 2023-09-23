###This is the file with all the code for the game

import random
from cmu_112_graphics import *
import math


NORTH = (-1,0)
SOUTH = (1,0)
EAST  = (0,1)
WEST  = (0,-1)

def appStarted(app, rows=14, cols=14):
    app.rows = rows
    app.cols = cols
    initgame(app)
    app.image0 = app.loadImage('Too-Cute-Kuromi-.png')
    app.image1 = app.scaleImage(app.image0, 0.35)
    app.image2 = app.loadImage('bomber.png')
    app.image3 = app.scaleImage(app.image2, 1/20)
    app.cupcake=app.loadImage('cake.png')
    app.cupcake = app.scaleImage(app.cupcake,1/50)
    app.fireimage=app.loadImage('firebomb.png')
    app.fireimage= app.scaleImage(app.fireimage,1/19)
    app.cookie=app.loadImage('ice.png')
    app.cookie = app.scaleImage(app.cookie,1/2.2)
    app.cinnaAI=app.loadImage('AIcinna.png')
    app.cinnaAI = app.scaleImage(app.cinnaAI,1/4.1)
    app.purinAI=app.loadImage('purin.webp')
    app.purinAI=app.scaleImage(app.purinAI,1/6)
    app.melodyAI=app.loadImage('melodyAI.png')
    app.melodyAI = app.scaleImage(app.melodyAI,1/11)
    ##images for start page
    app.background= app.loadImage('pinkbg2.jpg')
    app.background=app.scaleImage(app.background,0.5)
    app.title=app.loadImage('title.jpg')
    app.title=app.scaleImage(app.title,1/3)
    #images for character page
    app.kuromi= app.loadImage('kuromi.webp')
    app.kuromi=app.scaleImage(app.kuromi,1/2)
    app.melody=app.loadImage('melody.webp')
    app.melody=app.scaleImage(app.melody,0.7)
    app.cinna=app.loadImage('cinna2.webp')
    app.cinna=app.scaleImage(app.cinna,2.2)
    app.purin=app.loadImage('purin.webp')
    app.purin=app.scaleImage(app.purin,0.4)
    app.characterbg=app.loadImage('characterbg.png')
    app.characterbg=app.scaleImage(app.characterbg,1.5)
    #images for instruction
    app.scinst=app.loadImage('scinst.jpg')
    app.scinst=app.scaleImage(app.scinst,1/5)
    app.player=(0,0)
    app.bg=app.loadImage('stonetexture.png')
    app.bg = app.scaleImage(app.bg,2.3)
    app.margin = 5
    app.cW = (app.width - app.margin)/cols
    app.cH = (app.height - app.margin)/rows
    app.timerDelay=400
    app.delay=4
    

#images sources:
#https://stock.adobe.com/uk/images/pixel-art-style-set-of-different-16x16-seamless-texture-pattern-sprites-stone-wood-brick-dirt-metal-8-bit-game-design-background-tiles/248519433
#https://ar.pinterest.com/pin/35395547050856930/?amp_client_id=CLIENT_ID(_)&mweb_unauth_id={{default.session}}&simplified=true
# https://cinnamoroll.fandom.com/wiki/Cinnamoroll
#https://villains.fandom.com/wiki/Kuromi
#https://hellokitty.fandom.com/wiki/My_Melody
#https://hellokitty.fandom.com/wiki/Pompompurin
#https://hellokitty.fandom.com/wiki/Cinnamoroll?file=Sanrio_Characters_Cinnamoroll_Image029.png
#https://www.itl.cat/view/277584/
#https://www.dreamstime.com/vector-illustration-health-cracker-isolated-cookie-square-icon-vector-illustration-health-cracker-isolated-cookie-square-icon-image149227644
#https://www.google.com/search?q=cupcake+cartoon&tbm=isch&ved=2ahUKEwiYoOr4lZj3AhWPX80KHdpEDFwQ2-cCegQIABAA&oq=cupcake+cartoon&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BAgAEENQzQhY6g9grBJoAHAAeACAAc4BiAG2BpIBBTcuMC4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=LX9aYtjVOI-_tQbaibHgBQ&bih=739&biw=1268&rlz=1C5CHFA_enUS989US990&hl=en#imgrc=h0ydyJnIY27hIM&imgdii=Hh-h1lZBdd6dVM

 
def initgame(app):
    app.maze = makeBlankMaze(app.rows,app.cols)
    connectCells(app.maze)
    app.gameover=False
    app.player=(0,0)
    app.bomb=[]
    app.fire=[]
    app.cake=[]
    placeCake(app)
    app.ai1=AI(app,13,13)
    app.ai2=AI(app,0,13)
    app.ai3=AI(app,13,0)
    app.count=0
    app.win=False
    app.ai2die=False
    app.ai1die=False
    app.ai3die=False
    ##choose the page
    app.firstpage=True
    app.instructionpage=False
    app.selectCharacter=False
    app.gamestart=False
    app.playerC=None
    app.arrow=(150,300)
    app.sound = Sound('bombit.mp3')
    app.sound.start(loop=True)

def keyPressed(app,event):
    #mute or unmute the sound
    if (event.key == 's'):
        if app.sound.isPlaying(): app.sound.stop()
        else: app.sound.start()
    if app.selectCharacter:
        (cx,cy)=app.arrow  
        if event.key=="Right":
            cx+=150
        if event.key=="Left":
            cx-=150
        if cx<=600 and cx>=150:
            app.arrow =(cx,cy) 
        if event.key=='Return':
            if cx==150:
                app.playerC="Kuromi"
            if cx==300:
                app.playerC="Melody"
            if cx==450:
                app.playerC="Cinna"
            if cx==600:
                app.playerC="Purin"
            app.gamestart=True
            app.selectCharacter=False
        if event.key=="b":
            app.selectCharacter=False
            app.instructionpage=True         
    if app.gamestart:
        row,col = app.player
        if event.key=="r":
            app.maze = makeBlankMaze(app.rows,app.cols)
            connectCells(app.maze)
        elif event.key == "Up" and isValid(app, row,col,NORTH):
            doMove(app, row,col,NORTH)
        elif event.key == "Down" and isValid(app, row,col,SOUTH):
            doMove(app, row,col,SOUTH)
        elif event.key == "Left" and isValid(app, row,col,WEST):
            doMove(app, row,col,WEST)
        elif event.key== "Right" and isValid(app, row,col,EAST):
            doMove(app, row,col,EAST)
        elif event.key=="Space":
            (x0,y0,x1,y1)=getCellBounds(app, row, col)
            newBomb=Bomb(x0, y0, x1, y1, row,col, counter=0)
            app.bomb.append(newBomb)
        if isLegal(app,row,col):
            app.player=(row,col)

#funcitons for find the cell bounds
#citation:https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
def getCellBounds(app, row, col):
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    x0 = app.margin + col * cellWidth
    x1 = app.margin + (col+1) * cellWidth
    y0 = app.margin + row * cellHeight
    y1 = app.margin + (row+1) * cellHeight
    cx,cy=islandCenter(app,row,col)
    x0=cx-0.4*app.cW
    y0=cy-0.4*app.cH
    x1=cx+0.4*app.cW
    y1=cy+0.4*app.cH
    return (x0, y0, x1, y1)

def getCell(app, x, y):
    if (not pointInGrid(app, x, y)):
        return (-1, -1)
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth  = gridWidth / app.cols
    cellHeight = gridHeight / app.rows
    row = int((y - app.margin) / cellHeight)
    col = int((x - app.margin) / cellWidth)
    return (row, col)

def pointInGrid(app, x, y):
    return ((app.margin <= x <= app.width-app.margin) and
            (app.margin <= y <= app.height-app.margin))

#determind whether the movement is legal
def isLegal(app,row,col):
    if row<0 or row>=app.rows or col<0 or col>=app.cols:
        return False
    elif app.maze[row][col]!=0:
        return False
    return True

#define gmae over
def gameOver(app):
    fireset=set(app.fire)
    if len(app.fire)>0:
        for fire in fireset:
            (row,col)=(fire.row,fire.col)
            nearby=wallExist(app,row,col)
            for firerange in nearby:
                if firerange==app.player:
                    app.gameover=True
                    app.gamestart=False

#AI or player die
def die(app):
    ai1row,ai1col=app.ai1.row,app.ai1.col
    ai2row,ai2col=app.ai2.row,app.ai2.col
    ai3row,ai3col=app.ai3.row,app.ai3.col
    fireset=set(app.fire)
    if len(app.fire)>0:
        for fire in fireset:
            (row,col)=(fire.row,fire.col)
            nearby=wallExist(app,row,col)
            for firerange in nearby:
                if firerange==(ai1row,ai1col):
                    app.ai1die=True
                    app.ai1=AI(app,-1,-1)
                if firerange==(ai2row,ai2col):
                    app.ai2die=True
                    app.ai2=AI(app,-1,-1)
                if firerange==(ai3row,ai3col):
                    app.ai3die=True
                    app.ai3=AI(app,-1,-1)
            
#check the player win
def win(app):
    if app.ai1die==True and app.ai2die==True and app.ai3die==True:
        app.win=True
        app.gamestart=False

#check the movement to certian direction is valid
def isValid(app, row,col,direction):
    maze = app.maze
    rows,cols = len(maze),len(maze[0])
    if not (0<=row<rows and 0<=col<cols): return False
    if direction==EAST: return maze[row][col].east
    if direction==SOUTH: return maze[row][col].south
    if direction==WEST: return maze[row][col-1].east
    if direction==NORTH: return maze[row-1][col].south
    assert False

#move the player accroding to given direction
def doMove(app, row,col,direction):
    (drow,dcol) = direction
    maze = app.maze
    rows,cols = len(maze),len(maze[0])
    if not (0<=row<rows and 0<=col<cols): return False
    if (row+drow,col+dcol) in app.cake:return False
    app.player = (row+drow,col+dcol)


######The maze generator
#citation: https://www.cs.cmu.edu/~112/notes/maze-solver.py

def islandCenter(app, row, col):
    cellWidth,cellHeight = app.cW,app.cH
    return (col+0.5)*cellWidth,(row+0.5)*cellHeight

def rgbString(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def drawBridges(canvas, app):
    ice=rgbString(219, 241, 253)
    islands = app.maze
    rows,cols = len(islands),len(islands[0])
    width = min(app.cW,app.cH)/15
    for r in range(rows):
        for c in range(cols):
            island = islands[r][c]
            a,b=islandCenter(app, r,c)
            m,n=islandCenter(app, r+1,c)
            e,f=islandCenter(app, r,c+1)
            cx,cy=islandCenter(app,r,c)
            x0,y0=islandCenter(app, r,c)
            x1,y1=islandCenter(app, r,c+1)
            heightesat=(n-b)*0.41
            widthsouth=(e-a)*0.41     
            if (island.east):
                canvas.create_rectangle(x0-widthsouth,y0-heightesat,
                                            x1+widthsouth,y1+heightesat,fill=ice,outline=ice)

            if (island.south):
                x0,y0=islandCenter(app, r,c)
                x1,y1=islandCenter(app, r+1,c)
                canvas.create_rectangle(x0-widthsouth,y0-heightesat,
                                            x1+widthsouth,y1+heightesat,fill=ice,outline=ice)
            (x0,y0,x1,y1)=getCellBounds(app,8,8)
            (a,b,x1,y1)=getCellBounds(app,5,5)
            canvas.create_rectangle(x0,y0,x1,y1,fill=ice,outline=ice)

class Maze(object): pass

def makeGrid(number):
    cell=Maze()
    cell.east=cell.south=False
    cell.number=number
    return cell

def makeBlankMaze(rows,cols):
    grid=[[0]*cols for i in range(rows)]
    count=0
    for row in range(rows):
        for col in range(cols):
            grid[row][col] = makeGrid(count)
            count+=1
    grid[7][5].east=True
    grid[6][5].east=True
    grid[5][6].south=True
    grid[5][7].south=True
    grid[6][6].east=True
    grid[6][6].south=True
    grid[6][7].east=True
    grid[6][7].south=True
    grid[7][6].east=True
    grid[7][6].south=True
    grid[7][7].east=True
    grid[7][7].south=True
    return grid

def connectCells(grid):
    rows,cols=len(grid),len(grid[0])
    for i in range(rows*cols-1):
        pave(grid)

def pave(grid):
    rows,cols=len(grid),len(grid[0])
    while True:
        row,col=random.randint(0,rows-1),random.randint(0,cols-1)
        start=grid[row][col]
        if makechoice(): 
            if col==cols-1: 
                continue
            target=grid[row][col+1]
            if start.number==target.number: 
                continue
            start.east = True
            renameCell(start,target,grid)
        else: 
            if row==rows-1: 
                continue
            target=grid[row+1][col]
            if start.number==target.number:
                continue
            start.south=True
            renameCell(start,target,grid)
        return

def renameCell(i1,i2,grid):
    n1,n2 = i1.number,i2.number
    lo,hi = min(n1,n2),max(n1,n2)
    for row in grid:
        for cell in row:
            if cell.number==hi: cell.number=lo

def makechoice():
    return random.choice([True, False])

 ######DRAW#######
def drawInstuctionPage(app,canvas):
    canvas.create_text(400,100,text="INSTRUCTIONS",font='Ayuthaya 25 bold',fill='black')
    instruction="""
    -Your character will start at the upper left corner

    -Use "Up" "Down" "Left" or "Right" key to move your character

    -Press the "Space" key to place a bomb

    -The bomb would explode after few seconds with fire around it

    -If you get fired by the explosion, you die

    -Try to kill the three enemies by placing the bomb beside them

    -The character cannot go through a cake, use bomb to clear the cake

    -Also try to avoid getting bombed by the bombs!!

    -The map is a maze, so you might miss your way
    """
    canvas.create_text(app.width/2,360,text=instruction,
                            font='Ayuthaya 17 bold',fill='black')
    canvas.create_rectangle(600,580,760,630,fill="purple")
    canvas.create_text(680,605,text="Continue",fill="white", font='arial 35 bold')
    canvas.create_image(260,90, image=ImageTk.PhotoImage(app.image3))

def drawCharacterPage(app,canvas):
    canvas.create_text(400,150,text="Choose Your Character",font='Arial 30 bold',fill='black')
    canvas.create_image(160,400, image=ImageTk.PhotoImage(app.kuromi))
    canvas.create_text(160,500,text="Kuromi",font='Ayuthaya 20 bold',fill='Purple')
    canvas.create_image(320,400, image=ImageTk.PhotoImage(app.melody))
    canvas.create_text(320,500,text="Melody",font='Ayuthaya 20 bold',fill='Black')
    canvas.create_image(470,420, image=ImageTk.PhotoImage(app.cinna))
    canvas.create_text(480,500,text="Cinna",font='Ayuthaya 20 bold',fill='Blue')
    canvas.create_image(610,400, image=ImageTk.PhotoImage(app.purin))
    canvas.create_text(620,500,text="Purin",font='Ayuthaya 20 bold',fill='Brown')
    (cx,cy)=app.arrow
    canvas.create_polygon(cx-15,cy,cx+15,cy,cx,cy+10,fill = "yellow",outline="black",width=3)
    canvas.create_rectangle(cx-8,cy-100,cx+8,cy,fill="yellow",outline="black",width=3)
    canvas.create_image(400,670, image=ImageTk.PhotoImage(app.scinst))


def redrawAll(app, canvas):
    if app.gameover==True:
        canvas.create_rectangle(0,0, 800, 800, fill="pink")
        canvas.create_text(400,400,text="GAME OVER",fill="black", font='Arial 35 bold')
        canvas.create_rectangle(350,500,450,600,fill="black")
        canvas.create_text(400,550,text="restart",fill="white",font='Arial 20 bold')
    elif app.win==True:
        canvas.create_rectangle(0,0, 800, 800, fill="pink")
        canvas.create_text(400,400,text="You Win!",fill="black", font='Arial 35 bold')
        canvas.create_rectangle(350,500,450,600,fill="black")
        canvas.create_text(400,550,text="restart",fill="white",font='Arial 20 bold')
    
    elif app.firstpage:
        canvas.create_image(400,400, image=ImageTk.PhotoImage(app.background))
        canvas.create_image(430,250, image=ImageTk.PhotoImage(app.title))
        canvas.create_rectangle(500,400,660,460,fill="orange",outline="orange")
        canvas.create_text(580,430,text="Continue",fill="white", font='Arial 35 bold')
        text="""
        Press 's' to mute the music
        Press again to unmute"""
        canvas.create_text(570,500,text=text,fill="white")

    elif app.instructionpage:
        canvas.create_image(400,400, image=ImageTk.PhotoImage(app.background))
        drawInstuctionPage(app,canvas)

    elif app.selectCharacter:
        canvas.create_image(400,400, image=ImageTk.PhotoImage(app.characterbg))
        drawCharacterPage(app,canvas)

    elif app.gamestart:
        canvas.create_image(app.width//2,app.height//2, image=ImageTk.PhotoImage(app.bg))
        drawBridges(canvas, app)
        for r in range(app.rows):
            for c in range(app.cols):
                cx,cy=islandCenter(app,c,r)
                canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.cookie))
        ##draw character
        if app.playerC=='Kuromi':
            (row,col)=app.player
            (cx,cy)=islandCenter(app,row,col)
            canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.image1))
            ##draw ai
            row,col=app.ai1.row,app.ai1.col
            (cx,cy)=islandCenter(app,row,col)
            canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.cinnaAI))

            row,col=app.ai2.row,app.ai2.col
            (cx,cy)=islandCenter(app,row,col)
            canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.melodyAI))

            row,col=app.ai3.row,app.ai3.col
            (cx,cy)=islandCenter(app,row,col)
            canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.purinAI))
        if app.playerC=="Melody":
            (row,col)=app.player
            (cx,cy)=islandCenter(app,row,col)
            canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.melodyAI))
            ##draw ai
            row,col=app.ai1.row,app.ai1.col
            (cx,cy)=islandCenter(app,row,col)
            canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.cinnaAI))

            row,col=app.ai2.row,app.ai2.col
            (cx,cy)=islandCenter(app,row,col)
            canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.image1))

            row,col=app.ai3.row,app.ai3.col
            (cx,cy)=islandCenter(app,row,col)
            canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.purinAI))
        if app.playerC=="Cinna":
            (row,col)=app.player
            (cx,cy)=islandCenter(app,row,col)
            canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.cinnaAI))
            ##draw ai
            row,col=app.ai1.row,app.ai1.col
            (cx,cy)=islandCenter(app,row,col)
            canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.melodyAI))

            row,col=app.ai2.row,app.ai2.col
            (cx,cy)=islandCenter(app,row,col)
            canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.image1))

            row,col=app.ai3.row,app.ai3.col
            (cx,cy)=islandCenter(app,row,col)
            canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.purinAI))
        if app.playerC=="Purin":
            (row,col)=app.player
            (cx,cy)=islandCenter(app,row,col)
            canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.purinAI))
            ##draw ai
            row,col=app.ai1.row,app.ai1.col
            (cx,cy)=islandCenter(app,row,col)
            canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.cinnaAI))

            row,col=app.ai2.row,app.ai2.col
            (cx,cy)=islandCenter(app,row,col)
            canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.image1))

            row,col=app.ai3.row,app.ai3.col
            (cx,cy)=islandCenter(app,row,col)
            canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.melodyAI))

        for (c,r) in app.cake:
            cx,cy=islandCenter(app,c,r)
            (x0,y0,x1,y1)=getCellBounds(app,c,r)
            
            canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.cupcake))
        for bomb in app.bomb:
            bomb.redraw(app,canvas)

        for fire in app.fire:
            row,col=fire.row,fire.col
            redrawfire(app,canvas,row,col)


def mousePressed(app,event):
    if app.firstpage:
        if event.x<660 and event.x>500 and event.y<460 and event.y>400:
            app.firstpage=False
            app.instructionpage=True
    if  app.instructionpage==True :
        if event.x<760 and event.x>600 and event.y<630 and event.y>580:
            app.instructionpage=False
            app.selectCharacter=True
    if app.gameover or app.win:
        if event.x>=350 and event.x<=450 and event.y>=500 and event.y<=600:
            initgame(app)
        

def timerFired(app):
    gameOver(app)
    win(app)
    if app.gameover:
        return  
    if app.gamestart:
            app.count+=1
            die(app)
            for bomb in app.bomb:
                bomb.timerFired(app)    
            if len(app.bomb)>0:
                delete(app)
            for bomb in app.fire:
                bomb.timerFired(app)
                if len(app.fire)>0 and bomb.counter> app.delay*1.5:
                    app.fire.remove(bomb)
            
            if app.ai1die==False:
                app.ai1.decide(app)
            if app.ai2die==False:
                (playerow,playercol)=app.player
                if -1<=app.ai2.row-playerow<=1 and -1<=app.ai2.col-playercol<=1:
                     app.ai2.decide(app)
                else:
                    app.ai2.dumbdecide(app)
            if app.ai3die==False:  
                (playerow,playercol)=app.player
                if -2<=app.ai2.row-playerow<=2 and -2<=app.ai2.col-playercol<=2:
                     app.ai2.decide(app)
                else:
                    dumb=random.choice([True,False])
                    if dumb:
                        app.ai3.dumbdecide(app)
                    else: 
                        app.ai3.decide(app)
            
  
#delete the bomb from the bomb list after it exploded
def delete(app):
    for bomb in app.bomb:
        if bomb.counter>= app.delay:
            app.bomb.remove(bomb)
            app.fire.append(bomb) 
            removeCake(app,bomb.row,bomb.col)

#randomly scatter the cakes in the maze
def placeCake(app):
    count=0
    while count<=35:
        row=random.randint(0,app.rows-1)
        col=random.randint(0,app.cols-1)
        if (row,col) in [(0,0),(0,1),(0,2),(1,0),(1,1),
            (1,2),(2,0),(2,1),(2,2),
            (13,13),(13,12),(12,13),(12,12),
            (11,12),(11,13),(13,11),(12,11),
            (13,0),(13,1),(13,2),
            (12,0),(12,1),(12,2),
            (11,0),(11,1),(11,2),
            (0,13),(0,12),(0,11),
            (1,13),(1,12),(1,11),
            (2,13),(2,12),(2,11)]:
                continue
        elif (row,col) not in app.cake:
            app.cake.append((row,col))
            count+=1
        else: continue

#remove the cake when it get bombed
def removeCake(app,row,col):
    nearby=wallExist(app,row,col)
    for (r,c)in nearby:
        if (r,c) in app.cake:
            app.cake.remove((r,c))

#return the range the bomb fire can get to 
def wallExist(app,row,col):
    nearby=[(row,col)]
    #check right side
    if isValid(app, row,col,EAST) and app.maze[row][col].east:
        nearby.append((row,col+1))
    #check up
    if isValid(app, row-1,col,SOUTH) and app.maze[row-1][col].south:
        nearby.append((row-1,col))
    #check down
    if isValid(app, row,col,SOUTH) and app.maze[row][col].south:
        nearby.append((row+1,col))
    #check left
    if isValid(app, row,col-1,EAST) and app.maze[row][col-1].east:
        nearby.append((row,col-1))
    return nearby

#draw fire       
def redrawfire(app,canvas,row,col):
        nearby=wallExist(app,row,col)
        for (row,col) in nearby:
            (x0,y0,x1,y1)=getCellBounds(app, row, col)
            cx,cy=(x0+x1)/2,(y0+y1)/2
            canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.fireimage))


#create a class to keep track of the bombs
class Bomb:
    def  __init__(self,x0,y0,x1,y1,row,col,counter):
        self.x0=x0
        self.y0=y0
        self.x1=x1
        self.y1=y1
        self.row=row
        self.col=col
        self.counter=counter
    
    def redraw(self, app, canvas):
        cx,cy=(self.x1+self.x0)//2,(self.y1+self.y0)//2
        canvas.create_image(cx,cy, image=ImageTk.PhotoImage(app.image3))
                           
    def timerFired(self, app):
        self.counter += 1

###AI (smart, normal, dumb)
class AI:
    def  __init__(self,app,row,col):
        self.row=row
        self.col=col
        app.escape=False
    
##check if the indicated direction has a cake 
    def detectCake(self,app,direction):
        if direction==NORTH and (self.row-1,self.col) in app.cake:
            return False
        if direction==SOUTH and (self.row+1,self.col) in app.cake:
            return False
        if direction==WEST and (self.row,self.col-1) in app.cake:
            return False
        if direction==EAST and (self.row,self.col+1) in app.cake:
            return False
        return True

#to check whether are in the dangerous zone that might be bombed by the bombs         
    def detectBomb(self,app):
        neighbors=set([(self.row,self.col),(self.row-1,self.col),(self.row+1,self.col),
        (self.row,self.col-1),(self.row,self.col+1)
       ])
        row,col=self.row,self.col
        for bomb in app.bomb:
            bombrow,bombcol=bomb.row,bomb.col
            if (row,col)==(bombrow,bombcol):
                return True
            if (row-1,col)==(bombrow,bombcol):
                return app.maze[row-1][col].south
            if (row+1,col)==(bombrow,bombcol):
                return app.maze[row][col].south
            if (row,col-1)==(bombrow,bombcol):
                return app.maze[row][col-1].east
            if (row,col+1)==(bombrow,bombcol):
                return app.maze[row][col].east
            if (row-2,col)==(bombrow,bombcol):
                return app.maze[row-1][col].south and app.maze[row-2][col].south
            if (row+2,col)==(bombrow,bombcol):
                return app.maze[row][col].south and app.maze[row+1][col].south
            if (row,col-2)==(bombrow,bombcol):
                return app.maze[row][col-1].east and app.maze[row][col-2].east
            if (row,col+2)==(bombrow,bombcol):
                return app.maze[row][col].east and app.maze[row][col+1].east

##check whether threatened by the bomb
    def detectfire(self,app):
        firerange=self.firerange(app)
        neighbors=set([(self.row,self.col),(self.row-1,self.col),(self.row+1,self.col),
        (self.row,self.col-1),(self.row,self.col+1),
        (self.row-2,self.col),(self.row+2,self.col), (self.row,self.col-2),(self.row,self.col+2)])
        for neighbor in neighbors:
            if neighbor in firerange:   
                    return True
        return False

#decide the behavior of the AI
    def decide(self,app):
        self.firerange(app)
        direction=self.getDirection(app)
        if self.detectCake(app,direction)==False:
            if self.checkBombAdded(app)==False:
                (x0,y0,x1,y1)=getCellBounds(app,self.row,self.col)
                newBomb=Bomb(x0, y0, x1, y1, self.row,self.col, counter=0)
                app.bomb.append(newBomb)
                self.avoidBomb(app)
        elif self.corner(app) and self.detectBomb(app)!=True:
            pass
        elif self.detectBomb(app):
            self.avoidBomb(app)
        elif self.detectfire(app):
            pass
        elif self.detectCake(app,direction):
             self.Move(app)
    
#A dumb AI would consider its movement according to this function    
    def dumbdecide(self,app):
        self.firerange(app)
        direction=self.getDirection(app)
        if self.detectCake(app,direction)==False:
            if self.checkBombAdded(app)==False:
                (x0,y0,x1,y1)=getCellBounds(app,self.row,self.col)
                newBomb=Bomb(x0, y0, x1, y1, self.row,self.col, counter=0)
                app.bomb.append(newBomb)
                self.avoidBomb(app)
        elif self.corner(app) and self.detectBomb(app)!=True:
            pass
        elif self.detectBomb(app):
            self.avoidBomb(app)
        elif self.detectfire(app): 
            pass
        elif self.detectCake(app,direction) :
             self.dumbMove(app)

#a dumb way of move: ai move randomly instead of in the nearest path    
    def dumbMove(self,app):
        direction=random.choice([SOUTH,NORTH,EAST,WEST])
        (drow,dcol)=direction
        row,col=self.row,self.col
        if isValid(app,self.row,self.col,direction) and (row+drow,col+dcol) not in app.cake: 
            self.row+=drow
            self.col+=dcol
            if not self.inbound(app,self.row,self.col):
                self.row-=drow
                self.col-=dcol
        else: self.dumbMove(app)

#if a bomb is in the near corner, return True
    def corner(self,app):
        for bomb in app.bomb:
            bombrow,bombcol=bomb.row,bomb.col
            row,col=self.row,self.col
            if (bombrow,bombcol) in [(row-1,col-1),(row+1,row+1),(row-1,col+1),(row+1,col-1)]:
                return True
        return False

#don't add the bomb in the same position repeatedly
    def checkBombAdded(self,app):
        for bomb in app.bomb:
            if (self.row,self.col)==(bomb.row,bomb.col):
                return True
        return False

    def bombnearby(self,app):
        numofbomb=0
        bombset=set(app.bomb)
        row,col=self.row,self.col
        nearby=wallExist(app,row,col)
        for bomb in bombset:
            bombrow,bombcol=bomb.row,bomb.col
            if (bombrow,bombcol) in nearby:
                numofbomb+=1
        return numofbomb
                

##let the AI to go away from the bomb 
    def avoidBomb(self,app):
        row,col=self.row,self.col
        if self.bombnearby(app)>=3:
            pass
        for bomb in app.bomb:
            bombrow,bombcol=bomb.row,bomb.col
            if (row,col) ==(bombrow,bombcol):
                if app.maze[self.row][self.col].south and (row+1,col) not in app.cake and self.inbound(app,row+1,col) \
                    and (app.maze[row+1][col].south==True  or app.maze[row+1][col].east==True or app.maze[row+1][col-1].east==True):
                    self.row+=1
                elif app.maze[row][col].east and self.detectCake(app,EAST) and self.inbound(app,row,col+1) \
                    and  (app.maze[row][col+1].south==True or app.maze[row][col+1].east==True or app.maze[row-1][col+1].south==True):
                    self.col+=1
                elif app.maze[row][col-1].east and self.detectCake(app,WEST) and self.inbound(app,row,col-1):
                    self.col-=1
                elif app.maze[row-1][col].south and self.detectCake(app,NORTH) and self.inbound(app,row-1,col):
                    self.row-=1
                else:pass
            elif (row-1,col) ==(bombrow,bombcol) and app.maze[row-1][col].south:
                if app.maze[row][col-1].east and self.detectCake(app,WEST) and self.inbound(app,row,col-1):
                    self.col-=1  
                elif  self.row+1<app.rows and app.maze[self.row][self.col].south and self.detectCake(app,SOUTH) and self.inbound(app,row+1,col):
                    self.row+=1
                elif app.maze[row][col].east and self.detectCake(app,EAST) and self.inbound(app,row,col+1):
                    self.col+=1
                else:pass
            elif (row+1,col)  ==(bombrow,bombcol):
                if  app.maze[self.row][self.col].east and self.detectCake(app,EAST) and self.inbound(app,row,col+1):
                    self.col+=1
                elif app.maze[row][col-1].east and self.detectCake(app,WEST) and self.inbound(app,row,col-1):
                    self.col-=1
                elif self.row-1>=0 and app.maze[row-1][col].south and self.detectCake(app,NORTH) and self.inbound(app,row-1,col):
                    self.row-=1      
                else:pass   
            elif (row,col+1) ==(bombrow,bombcol) and app.maze[row][col].east:
                if app.maze[self.row-1][self.col].south and self.detectCake(app,NORTH) and self.inbound(app,row-1,col):
                    self.row-=1   
                elif app.maze[self.row][self.col].south and self.detectCake(app,SOUTH) and self.inbound(app,row+1,col):
                    self.row+=1
                elif  app.maze[row][col-1].east and self.detectCake(app,WEST) and self.inbound(app,row,col-1):
                    self.col-=1   
                else: pass
            elif (row,col-1) ==(bombrow,bombcol) and app.maze[row][col-1].east: 
                if app.maze[row][col].east and self.detectCake(app,EAST) and self.inbound(app,row,col+1):
                    self.col+=1
                elif app.maze[self.row][self.col].south and self.detectCake(app,SOUTH) and self.inbound(app,row+1,col):
                    self.row+=1    
                elif app.maze[row-1][col].south and self.detectCake(app,NORTH) and self.inbound(app,row-1,col):
                    self.row-=1  
                else: pass
            else: pass

##check whether the given row and col is in the grid
    def inbound(self,app,row,col):
        if row<0 or row>=app.rows or col<0 or col>=app.cols:
            return False
        else: return True

#return the cells with fire
    def firerange(self,app):
        firerange=[]
        for fire in app.fire:
                firerow,firecol=fire.row,fire.col
                nearby=wallExist(app,firerow,firecol)
                firerange.extend(nearby)
        return firerange

#move the character to the next cell according to the neart path
    def Move(self,app):
        direction= self.getDirection(app)
        if direction==NORTH:
            self.row-=1
        if direction==SOUTH:
            self.row+=1
        if direction==WEST:
            self.col-=1
        if direction==EAST:  
            self.col+=1

#find the direction of the next move
    def getDirection(self,app):
        if self.nextCell(app)!=None:
            nextcell=self.nextCell(app)
            xdir=nextcell[0]-self.row
            ydir=nextcell[1]-self.col
            for direction in  [NORTH,SOUTH,EAST,WEST]:
                if (xdir,ydir)==direction:
                    return direction

##return the next cell position the ai will move              
    def nextCell(self,app):
        (targetRow,targetCol)=app.player
        path=self.shortestPath(app,self.row,self.col,targetRow,targetCol)
        if len(path) <2:
            self.kill(app)
        else: return path[1]

#ShortestPath reference: 
#https://scs.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=dfed1c3d-259d-4c50-8d84-ae65013a6ffb
#https://www.youtube.com/watch?v=k1J9H_3oZWw
    def shortestPath(self,app,startrow,startcol,targetrow,targetcol):
        rows=app.rows
        cols=app.cols
        queue=[(startrow,startcol)]
        path=[]
        visited=[]
        while queue:
            current=queue[0]
            queue.remove(current)
            visited.append(current)
            if current==(targetrow,targetcol):
                break
            else: 
                currentRow=current[0]
                currentCol=current[1]
                for direction in [NORTH,SOUTH,EAST,WEST]: 
                    (drow,dcol) =direction
                    newRow,newCol=currentRow+drow,currentCol+dcol  
                    if newRow>=0 and newRow<rows and newCol>=0 and newCol<cols:
                        nextcell=(newRow,newCol)
                        if nextcell not in visited and isValid(app, currentRow,currentCol,direction):
                            queue.append(nextcell)
                            path.append({"current":current,"next":nextcell})    
        shortestPath=[(targetrow,targetcol)]
        while (targetrow,targetcol)!=(startrow,startcol):
            for edge in path:
                if edge["next"]==(targetrow,targetcol):
                    (targetrow,targetcol)=edge["current"]
                    shortestPath.insert(0,edge["current"])
        return shortestPath

##when the AI is closed to the player, put a bomb
    def kill(self,app):
        airow,aicol=self.row,self.col
        (x0,y0,x1,y1)=getCellBounds(app, airow, aicol)
        if self.checkBombAdded(app)==False:
            newBomb=Bomb(x0, y0, x1, y1, airow,aicol, counter=0)
            app.bomb.append(newBomb)


#sound citation from class notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html
#the music is from: https://music.163.com/song?id=1321512521&userid=550835056
import subprocess, threading, time

class Sound(object):
    def __init__(self, path):
        self.path = path
        self.process = None
        self.loop = False

    def isPlaying(self):
        return (self.process is not None)

    def checkProcess(self):
        while self.process is not None:
            if (self.process.poll() is not None):
                self.process = None
        if self.loop:
            self.start(loop=True)

    def start(self, loop=False):
        self.stop()
        self.loop = loop
        self.process = subprocess.Popen(['afplay', self.path])  
        threading.Thread(target=self.checkProcess).start()

    def stop(self):
        process = self.process
        self.loop = False
        self.process = None
        if (process is not None):
            try: process.kill()
            except: pass

def appStopped(app):
    app.sound.stop()



runApp(width=800, height=800)


