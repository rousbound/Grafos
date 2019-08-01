import pygame
from settings import*

class Text():
    def __init__(self,string,size,posIni,camera):
        self.GREEN = (84, 216, 61)
        self.WHITE = [255,255,255]
        self.color = self.WHITE

        self.string = string
        self.POS = vec(posIni.x,posIni.y)#vec(posIni.x,posIni.y)#

        self.selected = False
        self.textSize = size
        self.connected = False
        self.highlighted = False


        #self.text_rect = None


    def draw(self,camera,input):
        self.pos = vec(self.POS.x-camera.POS.x,self.POS.y-camera.POS.y)

        font = pygame.font.SysFont('Courier', int(self.textSize-(camera.POS.z*10)))
        text = font.render(self.string, True, (255,255,255))
        self.text_rect = text.get_rect()
        self.text_rect.centerx = (self.pos.x)
        self.text_rect.centery = (self.pos.y)

        if self.highlighted:
            self.color = self.WHITE
            pygame.draw.rect(win,self.color,self.text_rect,1)
        if self.selected:
            self.color = self.GREEN
            pygame.draw.rect(win,self.color,self.text_rect,1)


        win.blit(text, (self.text_rect))









    def deselect(self):
        self.selected = False

    def checkHighlight(self,input):
        if self.text_rect.collidepoint(input.pos):
            self.highlighted = True
        else:
            self.highlighted = False


    def move(self,input):
        if self.text_rect.collidepoint(input.pos):
            print("Moving")
            self.POS = input.POS

    def setup(self,camera,input):
        self.checkHighlight(input)
        pass

    def debug(self):
        print("Text object:",self.string,"pos:", self.pos, "POS:",self.POS, "Rect_POS:", self.text_rect.center, "SELECTED:?",self.selected)


class TGroup():
    def __init__(self):
        self.texts = []
        self.lSelected = []
        self.lConnected = []

        self.WHITE = [255,255,255]


    def draw(self,camera,input):
        for text in self.texts:
            text.draw(camera,input)
        for i in range(len(self.lConnected)):
            if i <= len(self.lConnected)-2:
                pygame.draw.line(win, self.WHITE, self.lConnected[i].pos,self.lConnected[i+1].pos,2)
            if i == len(self.lConnected)-1:
                pygame.draw.line(win, self.WHITE, self.lConnected[i].pos,self.lConnected[0].pos,2)

        #camera.scaleObjects(self.texts)

    def setup(self,camera,input):
        for text in self.texts:
            text.setup(camera,input)

    def debug(self):
        for text in self.texts:
            text.debug()

    def add(self,text):
        self.texts.append(text)

    def addSelected(self,text):
        self.lSelected.append(text)

    def isInside(self,input):
        for text in self.texts:
            if text.highlighted == True:
                print("Is inside")
                return True
        print("not inside")
        return False


    def deselectAll(self):
        for text in self.texts:
            text.deselect()
        self.lSelected = []

    def connect(self):
        for text in self.texts:
            if text.selected == True:
                if text.connected != True:
                    self.lConnected.append(text)
                    text.connected = True
                    text.deselect()

                elif text.connected == True:
                    text.connected = False
                    if text in self.lConnected:
                        self.lConnected.remove(text)
                    text.deselect()
