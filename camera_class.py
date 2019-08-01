import pygame
#from settings import *
#from subject_base_class import *

from settings import *

class Camera():
    def __init__(self,x,y,up,down,right,left):
        self.x = x
        self.y = y
        self.z = 1
        self.acc = vec3(0,0,0)
        self.vel = vec3(0,0,0)
        self.POS = vec3(self.x,self.y,self.z)
        self.up = up
        self.down= down
        self.right = right
        self.left = left
        self.maximum_values = vec3(10,10,1)
        self.maximum_zoom = 2
        self.slack = 180
        self.player_acc = 1
        self.zoom_acc = 0.01




    def adjust(self, player):
        if player.pos.x > self.pos.x + winw - self.slack:
            self.acc.x = self.player_acc
        if player.pos.x < self.pos.x + self.slack - player.rect.w:
            self.acc.x = -self.player_acc
        if player.pos.y > self.pos.y + winh - self.slack:
            self.acc.y = self.player_acc
        if player.pos.y < self.pos.y + self.slack - player.rect.h:
            self.acc.y = -self.player_acc
            #player.acc.x -= player.player_acc



    def debug_mode(self):
        print("Camera:  ", "Acc:", self.acc, "Vel:", self.vel, "POS:", self.POS)


    def dynamics(self):
        self.vel += self.acc
        self.vel *= 0.90
        self.vel.z *= 0.99
        self.POS += self.vel

        #self.pos *= self.totalZoom/100


    def handle_controls(self):
        keys = pygame.key.get_pressed()
        self.acc = vec3(0,0,0)
        self.scaling = False
        if keys[self.up]:
            self.acc.y = -self.player_acc
        if keys[self.down]:
            self.acc.y = self.player_acc
        if keys[self.left]:
            self.acc.x = -self.player_acc
        if keys[self.right]:
            self.acc.x = self.player_acc
        if keys[pygame.K_o]:
            self.acc.z += self.zoom_acc
        if keys[pygame.K_p]:
            self.acc.z -= self.zoom_acc



    def limits(self):
        if self.acc.x >= self.maximum_values.x:
            self.acc.x = self.maximum_values.x
        if self.acc.y >= self.maximum_values.y:
            self.acc.y = self.maximum_values.y
        if self.vel.x >= self.maximum_values.x:
            self.vel.x = self.maximum_values.x
        if self.vel.y >= self.maximum_values.y:
            self.vel.y = self.maximum_values.y
        if self.acc.z >= self.maximum_values.z:
            self.acc.z = self.maximum_values.z
        if self.vel.z >= self.maximum_values.z:
            self.vel.z = self.maximum_values.z

        if self.POS.z >= self.maximum_zoom:
            self.POS.z = self.maximum_zoom
        if self.POS.z <= -self.maximum_zoom:
            self.POS.z = -self.maximum_zoom

    def setup(self):
        self.dynamics()
        self.handle_controls()
        self.limits()

        #self.debug_mode()

    def draw(self):
        #self.centerDebug()
        pass
