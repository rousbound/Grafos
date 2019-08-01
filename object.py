from settings import *
import pygame

class Object():
    def __init__(self,pos):
        self.POS = vec(pos)

    def draw(self,camera):
        self.pos = vec(self.POS.x-camera.POS.x,self.POS.y-camera.POS.y)
        self.rect = pygame.Rect(0,0,100,100)
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y

        pygame.draw.rect(win,(255,255,255),self.rect,2)
        #self.draw(camera)

    def move(self,input):
        print("MOVE OBJECT")
        if self.rect.collidepoint(input.pos):
            self.POS = input.POS

    def debug(self):
        print("CENTER DEBUG:", "ṕos:", self.pos, "POS:", self.POS )
