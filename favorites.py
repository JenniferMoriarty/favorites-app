#favortes toolbar prototype
#Programmed by Jen Moriarty, August 2022
#CSU Global CSC 505, Critical Thinking Module 3, option 2
#This program demos how the icons for various "game"
#will appear on a phone's toolbar based on their popularity.
#the top 4 most recently clicked on games will appear on the phone's toolbar


import pygame #module to help with graphics
import math #my favorite module!
pygame.init()#initializes Pygame
pygame.display.set_caption("Favorites Demo")#sets the window title
screen = pygame.display.set_mode((400, 800))#creates game screen
screen.fill((0, 0, 0))#paint background black
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #tuple to hold mouse position
doExit = False


class App:#-----------------------------------------------------------------------------
    def __init__(self, xpos, ypos, color):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.clickNum = 0 #keeps track of number of times it has been "played" by user

    def draw(self):
        pygame.draw.circle(screen, (self.color), (self.xpos, self.ypos), 50)
    
    def isClicked(self, x, y): #is passed mouse coords, returns true if its within radius
        if math.sqrt((self.xpos-x)*(self.xpos-x) + (self.ypos-y)*(self.ypos-y))<50: #good ol' distance formula!
            print("clicked!") #just for testing
            self.clickNum += 1
            return True
        else:
            return False
        
    def giveColor(self): #used to draw favorites on top
        return (self.color)
    
    def addClick(self): #used when app has been clicked from favorites bar
        self.clickNum += 1
        
#end class app---------------------------------------------------------------------------

AppList = list()

#instantiate the apps:
#row1
game1 = App(100, 400, (200, 200, 0))
AppList.append(game1)
game2 = App(200, 400, (0, 200, 200))
AppList.append(game2)
game3 = App(300, 400, (200, 0, 200))
AppList.append(game3)
#row2
game4 = App(100, 500, (200, 0, 0))
AppList.append(game4)
game5 = App(200, 500, (0, 200, 0))
AppList.append(game5)
game6 = App(300, 500, (0, 0, 200))
AppList.append(game6)
#row3
game7 = App(100, 600, (50, 0, 100))
AppList.append(game7)
game8 = App(200, 600, (100, 100, 100))
AppList.append(game8)
game9 = App(300, 600, (255, 255, 255))
AppList.append(game9)

#gameloop###################################################
while not doExit:
#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()
#update/timer section---------------------------------------    

#input section----------------------------------------------
    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        #check if one of the apps has been clicked ============================
        for i in range(0, len(AppList)):
            AppList[i].isClicked(mousePos[0], mousePos[1]) #check which app has been clicked
        AppList.sort(key = lambda x: x.clickNum) #resort favorites list after every click
        for i in range(0, len(AppList)):
            print(AppList[i].clickNum)
        #check if one of the favorites has been clicked =========================
        if math.sqrt((mousePos[0]-100)*(mousePos[0]-100) + (mousePos[1]-50)*(mousePos[1]-50))<50: #first fav clicked
            print("first fav clicked!") #just for testing
            AppList[len(AppList1)-1].addClick()
        if math.sqrt((mousePos[0]-200)*(mousePos[0]-200) + (mousePos[1]-50)*(mousePos[1]-50))<50: #2nd fav clicked
            print("second fav clicked!") #just for testing
            AppList[len(AppList)-2].addClick()
        if math.sqrt((mousePos[0]-300)*(mousePos[0]-300) + (mousePos[1]-50)*(mousePos[1]-50))<50: #3rd fav clicked
            print("third fav clicked!") #just for testing
            AppList[len(AppList)-3].addClick() 

    if event.type == pygame.MOUSEMOTION: #update mouse position
        mousePos = event.pos
        
#render section---------------------------------------------
    #draw the apps:
    for i in range(0, len(AppList)):
        AppList[i].draw()

    #draw the favorite apps above favorites bar:
    pygame.draw.circle(screen, (AppList[len(AppList)-1].giveColor()), (100, 50), 50)
    pygame.draw.circle(screen, (AppList[len(AppList)-2].giveColor()), (200, 50), 50)
    pygame.draw.circle(screen, (AppList[len(AppList)-3].giveColor()), (300, 50), 50)

    #draw the favorites bar:
    pygame.draw.line(screen, (255, 255, 255), (0, 100), (400, 100), 2)

    pygame.display.flip()


#end game loop##############################################

pygame.quit()
