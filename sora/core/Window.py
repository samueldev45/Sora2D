import sys, pygame
from sora.input import *
from sora.renderer.Renderer import Renderer

class Window:
    def __init__(self, assets):
        if not pygame.get_init():
            pygame.init()

        self.assets = assets
        self.fps = 60
        self.pygameEvents = None
        self.mouse = Mouse()
        self.keyboard = Keyboard()

        self.__scene = None
        self.__display = None
        self.__shouldClose = False
        self.__clock = pygame.time.Clock()
        self.__renderer = Renderer()

    def setScene(self, scene):
        scene.window = self
        self.__scene = scene

    def getScene(self):
        return self.__scene

    def create(self, width, height, title, flags=0):
        self.__display = pygame.display.set_mode((width, height), flags)
        pygame.display.set_caption(title)

    def events(self):
        self.pygameEvents = pygame.event.get()

        for event in self.pygameEvents:
            if event.type == pygame.QUIT:
                self.__shouldClose = True

    def update(self):
        self.mouse.update()
        self.keyboard.update()
        
        if self.__scene:
            self.__scene.update()

    def render(self):
        if self.__scene:
            self.__renderer.render(self.assets, self.__scene, self.__display)

    def playSound(self, name, volume=1.0):
        sound = self.assets.getSound(name)
        if sound:
            sound.set_volume(volume)
            sound.play()

    def stopSound(self, name):
        sound = self.assets.getSound(name)
        if sound:
            sound.stop()

    def mainLoop(self):
        if not self.__display:
            print("Error: <Window> (mainLoop) -> The window was not created.")
            sys.exit(0)
            
        while not self.__shouldClose:
            self.events()
            self.update()
            self.render()

            self.__clock.tick(self.fps)
            pygame.display.update()