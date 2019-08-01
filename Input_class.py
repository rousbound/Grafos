import pygame
from settings import *


class Input():
    def __init__(self):
        self.button1 = 0
        self.button2 = 0
        self.button3 = 0
        self.pos = vec(0,0)
        self.POS = vec(0,0)
        self.drawing = False
        self.Rect = None

    def debug_mode(self):
        print("INPUT:" ,"Button1:",self.button1,"Button2:",self.button2,"Button3:",self.button3)
        print("INPUT: pos:",self.pos, "POS:",self.POS)

    def handle_mouse(self,camera):
        self.x,self.y = pygame.mouse.get_pos()
        self.pos = vec(self.x,self.y)

        self.X,self.Y = self.x+camera.POS.x, self.y+camera.POS.y
        self.POS = vec(self.X,self.Y)

    def mouse_pressed(self):
        self.button1,self.button2,self.button3 = pygame.mouse.get_pressed()


    def handle_keyboard(self,textGroup):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_v]:
            textGroup.connect()


    def draw_rect(self,camera):
        global ini
        if self.button3 == 1:
            if self.drawing == False:
                ini = self.pos
                self.drawing = True
            elif self.drawing == True:
                #print("RECTRECT")
                self.Rect = pygame.Rect(ini.x,ini.y,self.pos.x-ini.x,self.pos.y-ini.y)
                pygame.draw.rect(win,(255,255,255),self.Rect,1)
        elif self.button3 == 0:
            self.drawing = False
            self.Rect = None

    def checkClick(self,textGroup,main):
        if self.button1 == 1:
            for text in textGroup.texts:
                if text.highlighted:
                    print("SELECT")
                    text.move(self)
                    text.selected = True
            if textGroup.isInside(input) == False:
                textGroup.deselectAll()


            #main.oDebug.move(self)

    def rectSelect(self,textGroup):
        if self.drawing == True and self.Rect != None:
            for text in textGroup.texts:
                if text.text_rect.colliderect(self.Rect)  == True:
                    text.selected=True
                    textGroup.addSelected(text)

    def setup(self,camera,textGroup,main):
        self.handle_mouse(camera)
        self.checkClick(textGroup,main)
        self.mouse_pressed()
        self.rectSelect(textGroup)
        #self.debug_mode()

    def draw(self,camera):
        self.draw_rect(camera)

input = Input()
