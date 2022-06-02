import os, pygame

class AssetManager:
    def __init__(self):
        self.__images = {}
        self.__sounds = {}
        self.__musics = {}

    def loadImage(self, name, filePath):
        if os.path.exists(filePath):
            if not name in self.__images:
                image = pygame.image.load(filePath).convert_alpha()
                image.set_colorkey((255, 0, 255))
                self.__images[name] = image
        else:
            print("Error: <AssetManager> (loadImage) -> The path '{}' dont exists.".format(filePath))

    def loadSound(self, name, filePath):
        if os.path.exists(filePath):
            if not name in self.__sounds:
                self.__sounds[name] = pygame.mixer.Sound(filePath)
        else:
            print("Error: <AssetManager> (loadSound) -> The path '{}' dont exists.".format(filePath))

    def getImage(self, name):
        if name in self.__images:
            return self.__images[name]
        return None

    def getSound(self, name):
        if name in self.__sounds:
            return self.__sounds[name]
        return None

    def deleteImage(self, name):
        if name in self.__images:
            del self.__images[name]

    def deleteSound(self, name):
        if name in self.__sounds:
            del self.__sounds[name]