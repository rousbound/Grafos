import pygame
from settings import*
import math
import random
from camera_class import *
from Input_class import *

from textClass import *

from object import *

class Main():

    def __init__(self):
        pygame.init()

        self.center = vec(winw/2,winh/2)

        #bg = pygame.image.load("águia_screen2.png")



        self.camera = Camera(winw+self.center.x,winh+self.center.y,pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a)

        self.input = Input()

        self.Transferencia = Text("Transferência",70,vec(winw*2,winh*2),self.camera)

        self.Inconsciente = Text("Inconsciente",70,vec(winw*2 + 300, winh*2 + 400),self.camera)

        self.FreeAsso = Text("Associação Livre",35,vec(winw*2 - 300, winh*2 + 400), self.camera)

        self.textGroup = TGroup()

        self.textGroup.add(self.Transferencia)
        self.textGroup.add(self.Inconsciente)
        self.textGroup.add(self.FreeAsso)
        #self.oDebug = Object((winw*2,winh*2))

    def fps_counter(self):
        clock.tick(fps)
        win_caption = pygame.display.set_caption("Grafos    FPS:%d"%clock.get_fps())

    def debug_mode(self):
        #self.camera.debug_mode()
        self.textGroup.debug()
        self.input.debug_mode()
        #self.oDebug.debug()
        pass



    def draw(self):
        win.fill([0,0,0])
        self.textGroup.draw(self.camera,self.input)
        self.camera.draw()
        #self.oDebug.draw(self.camera)
        self.input.draw(self.camera)
        pygame.display.update()


    def setup(self,camera,input,textGroup):
        self.input.setup(camera,textGroup,self)
        self.camera.setup()
        self.textGroup.setup(camera,input)


    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    run = False
                if event.type == pygame.KEYDOWN:
                    self.input.handle_keyboard(self.textGroup)

            self.draw()
            self.setup(self.camera,self.input,self.textGroup)
            self.fps_counter()


            self.debug_mode()



grafos = Main()
grafos.main()
