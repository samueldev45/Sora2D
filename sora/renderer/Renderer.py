import pygame

class Renderer:
    def __init__(self):
        self.__lastImage = None
        self.__lastSurface = None

    def render(self, assets, scene, surface):
        surface.fill(scene.backgroundColor)
        actors = [obj for obj in scene.getActors() if obj.image != None]

        for actor in sorted(actors, key=lambda actor: actor.zIndex):
            baseImage = assets.getImage(actor.image)
            image = pygame.transform.scale(baseImage, (actor.scale.x, actor.scale.y))
            rect = image.get_rect()
            rect.x = actor.position.x
            rect.y = actor.position.y

            if actor.rotation != 0:
                image = pygame.transform.rotate(image, -actor.rotation).convert_alpha()
                rect = image.get_rect(center=image.get_rect(center = (actor.position.x, actor.position.y)).center)

            if image:
                if actor.color != (255,255,255):
                    image.fill(actor.color, special_flags=pygame.BLEND_RGB_MULT)
                image.set_colorkey((255, 0, 255))
                surface.blit(image, rect)