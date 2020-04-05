import pygame


class Screen:
    screen = None
    background = None

    # Constructor for the screen object that uses the above screen size declarations
    # background should be an SDL_rect
    def __init__(self, w, h):
        # Screen settings
        self.screen = pygame.display.set_mode((w, h))

    # background should be an SDL_Rect
    def set_background(self, background):
        self.background = background

    def draw(self):
        if self.background is not None:
            self.screen.blit(self.background, (0, 0))
        pygame.display.flip()