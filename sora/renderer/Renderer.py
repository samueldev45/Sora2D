import pygame

class Renderer:
    def __init__(self):
        self.__lastImage = None
        self.__lastSurface = None

    def render(self, assets, scene, surface):
        surface.fill(scene.backgroundColor)
        actors = [obj for obj in scene.getActors() if obj.image != None]

        for actor in sorted(actors, key=lambda actor : actor.zIndex):
            imgSurface = assets.getImage(actor.image)
            if imgSurface:
                if not actor.surface:
                    actor.surface = imgSurface

                # scale
                if actor.surface.get_size() != (actor.scale.x, actor.scale.y):
                    actor.surface = pygame.transform.scale(imgSurface, (actor.scale.x, actor.scale.y))
                rect = actor.surface.get_rect()
                rect.x, rect.y = actor.position.x, actor.position.y

                # rotation
                finalSurface = actor.surface
                if actor.rotation != 0:
                    finalSurface = pygame.transform.rotate(finalSurface, -actor.rotation)

                rect = finalSurface.get_rect(center=actor.surface.get_rect(center=(actor.position.x, actor.position.y)).center)
                finalSurface.set_colorkey((255, 0, 255))
                surface.blit(finalSurface, rect)
