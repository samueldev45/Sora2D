import pygame
from sora.math.Vector2 import Vector2

class Mouse:
    def __init__(self):
        self.__buttons = []

    def getPosition(self):
        pos = pygame.mouse.get_pos()
        return Vector2(pos[0], pos[1])

    def pressed(self, button : int):
        mouse = pygame.mouse.get_pressed(num_buttons=5)
        if mouse[button]:
            return True
        return False

    def click(self, button : int):
        mouse = pygame.mouse.get_pressed(num_buttons=5)
        if mouse[button]:
            if not button in self.__buttons:
                self.__buttons.append(button)
                return True
        return False

    def update(self):
        mouse = pygame.mouse.get_pressed(num_buttons=5)
        removeList = []
        for button in self.__buttons:
            if not mouse[button]:
                removeList.append(button)

        for button in removeList:
            self.__buttons.remove(button)