import pygame.font


class Button:
    def __init__(self, screen, msg):
        """Initialize button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.msg_image = None
        self.msg_image_rect = None
        self.title1_image = None
        self.title1_image_rect = None
        self.title2_image = None
        self.title2_image_rect = None
        self.purp = None
        self.teal = None
        self.green = None
        self.red = None

        # Set the dimensions and properties of button
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.text_color = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Build the play button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.top = self.screen_rect.bottom - 100

        # The button needs to be prepped only once
        self.prep_msg(msg)
        self.prep_title()
        self.targetvalues()

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.msg_image_rect.top = self.screen_rect.bottom - 100

    def prep_title(self):
        """Turn game title display into image and place on screen"""
        self.font = pygame.font.SysFont(None, 120)
        title1 = "SPACE"
        self.title1_image = self.font.render(title1, True, (255, 255, 255), self.button_color)
        self.title1_image_rect = self.title1_image.get_rect()
        self.title1_image_rect.center = self.rect.center
        self.title1_image_rect.top = self.screen_rect.top + 50

        self.font = pygame.font.SysFont(None, 64)
        title2 = "INVADERS"
        self.title2_image = self.font.render(title2, True, (0, 255, 0), self.button_color)
        self.title2_image_rect = self.title2_image.get_rect()
        self.title2_image_rect.center = self.rect.center
        self.title2_image_rect.top = self.title1_image_rect.bottom

    def targetvalues(self):
        self.purp = pygame.image.load('images/purp1.png')
        self.teal = pygame.image.load('images/teal1.png')
        self.green = pygame.image.load('images/green1.png')
        self.red = pygame.image.load('images/ufo.png')

    def draw_button(self):
        # Draw blank button and then draw message
        self.screen.fill(self.button_color, self.screen_rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.title1_image, self.title1_image_rect)
        self.screen.blit(self.title2_image, self.title2_image_rect)
