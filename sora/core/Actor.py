from sora.core.Component import Component
from sora.math.Vector2 import Vector2
import time

class Actor:
    def __init__(self, name="Actor"):
        self.name = name
        self.properties = {}
        self.started = False
        self.scene = None

        # Transform properties
        self.position = Vector2()
        self.scale = Vector2(32, 32)
        self.rotation = 0

        # Sprite properties
        self._image = None
        self.surface = None
        self.color = (255, 255, 255)
        self.zIndex = 0

        self.__id = id(self)
        self.__tags = []
        self.__components = {}

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value : str):
        self.surface = None
        self._image = value

    def add(self, *components):
        for component in components:
            if isinstance(component, Component):
                if not component.name in self.__components:
                    component.actor = self
                    self.__components[component.name] = component

    def get(self, component : str):
        if component in self.__components:
            return self.__components[component]

    def getId(self):
        return self.__id

    def remove(self, component : str):
        if component in self.__components:
            component.actor = None
            del self.__components[component]

    def addTag(self, tag : str):
        if not tag in self.__tags:
            self.__tags.append(tag)

    def hasTag(self, tag : str):
        if tag in self.__tags:
            return True
        return False

    def removeTag(self, tag : str):
        if tag in self.__tags:
            self.__tags.remove(tag)

    def start(self):
        if not self.started:
            for component in self.__components:
                self.__components[component].start()
            self.started = True

    def update(self):
        if not self.started: self.start()
        else:
            for component in self.__components:
                self.__components[component].update()

    def end(self):
        if self.scene:
            self.scene.remove(self.__id)
