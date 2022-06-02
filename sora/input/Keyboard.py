import pygame

class Keyboard:
    def __init__(self):
        self.__keys = []

    def pressed(self, key : str):
        keyboard = pygame.key.get_pressed()
        code = pygame.key.key_code(key)
        if code and keyboard[code]:
            return True
        return False

    def keyDown(self, key : str):
        keyboard = pygame.key.get_pressed()
        code = pygame.key.key_code(key)

        if code and keyboard[code] and not code in self.__keys:
            self.__keys.append(code)
            return True
        return False

    def update(self):
        keyboard = pygame.key.get_pressed()
        removeList = []
        for code in self.__keys:
            if not keyboard[code]:
                removeList.append(code)
        for code in removeList:
            self.__keys.remove(code)