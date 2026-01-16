import pygame
from random import randint

class Screen:
    def __init__(self):
        pygame.init()

        self.SCREEN_WIDTH = 600
        self.SCREEN_HEIGHT = 400
        self.screen = pygame.display.set_mode((600, 400))
        self.clock = pygame.time.Clock()
        self.fps = 60

        # --- Game State
        self.state = "HOME"

        # --- BACKGROUND ---
        self.background = pygame.image.load('images/nfbg.jpg').convert()
        self.background = pygame.transform.scale(self.background, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # --- Player ---
        self.frog = pygame.image.load('images/idle01.png').convert_alpha()
        self.frog = pygame.transform.scale(self.frog, (96, 96))
        self.frog_rect = self.frog.get_rect(topleft=(100, 300))

        # --- SAW ---
        self.saw = pygame.image.load('images/saw01.png').convert_alpha()
        saw_size = randint(32,50)
        self.saw = pygame.transform.scale(self.saw, (saw_size, saw_size))
        self.saw_rect = self.saw.get_rect(topleft=(randint(0, self.SCREEN_WIDTH), randint(0, self.SCREEN_HEIGHT)))

        # ---Text---

        self.font1 = pygame.font.SysFont('fonts/dpcomic.ttf', 40)
        self.font2 = pygame.font.SysFont('fonts/minecraft.ttf', 40)

        self.press_text = self.font1.render("Press <s> to start", False, "green")
        self.press_rect = self.press_text.get_rect(center=(300, 300))

        self.how_play_text = self.font1.render("d = moves\n space = jump", False, "green")
        self.how_play_rect = self.how_play_text.get_rect(center=(200, 50))



    def run(self):
        while True:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        pygame.quit()
                        return
                    if event.key == pygame.K_s:
                        self.state = "START"
                    if event.key == pygame.K_SPACE:
                        self.state = "INSTRUCTIONS"
                    if event.key == pygame.K_d:
                        self.state = "HOME"

            if self.state == "HOME":
                self.screen.blit(self.press_text, self.press_rect)

            elif self.state == "INSTRUCTIONS":
                self.screen.blit(self.how_play_text, self.how_play_rect)

            elif self.state == "START":
                self.screen.blit(self.background, (0, 0))
                self.screen.blit(self.frog, self.frog_rect)
                self.screen.blit(self.saw, self.saw_rect)

            pygame.display.update()
            self.clock.tick(self.fps)

Screen().run()
