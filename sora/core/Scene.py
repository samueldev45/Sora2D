from sora.core.Actor import Actor

class Scene:
    def __init__(self, name="Scene"):
        self.name = name
        self.window = None
        self.backgroundColor = (0, 0, 0)

        self.__actors = {}
        self.__appendQueue = []
        self.__removeQueue = []

    def add(self, actor):
        if isinstance(actor, Actor):
            if not actor in self.__appendQueue:
                self.__appendQueue.append(actor)

    def remove(self, actorId : int):
        if not actorId in self.__removeQueue:
            if actorId in self.__actors:
                self.__removeQueue.append(actorId)

    def get(self, actorId : int):
        if actorId in self.__actors:
            return self.__actors[actorId]
        return None

    def get(self, name : str):
        for actorId in self.__actors:
            if self.__actors[actorId].name == name:
                return self.__actors[actorId]
        return None

    def getActors(self):
        actors = []
        for actorId in self.__actors:
            actors.append(self.__actors[actorId])
        return actors

    def start(self):
        for actorId in self.__actors:
            self.__actors[actorId].start()

    def update(self):
        for actorId in self.__actors:
            if not self.__actors[actorId].started:
                self.__actors[actorId].start()

            if hasattr(self.__actors[actorId], "update"):
                self.__actors[actorId].update()

        for actor in self.__appendQueue:
            actor.scene = self
            self.__actors[actor.getId()] = actor
        self.__appendQueue.clear()

        for actorId in self.__removeQueue:
            self.__actors[actorId].scene = None
            del self.__actors[actorId]
        self.__removeQueue.clear()