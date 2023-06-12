import pygame
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
game_title = '12 Beads'
pygame.display.set_caption(game_title)
icon = pygame.image.load('images/GameIcon.png')
pygame.display.set_icon(icon)
main_menu_screen = pygame.image.load('images/MainMenu.png')
font = pygame.font.Font('fonts/Bristone.ttf', 30)
text_grey = [font.render('PLAY',True,'grey'), font.render('ONLINE',True,'grey'), font.render('QUIT',True,'grey')]
text_red = [font.render('PLAY',True,'red'), font.render('ONLINE',True,'red'), font.render('QUIT',True,'red')]
game_background = pygame.image.load('images/GameBackground.png')
player_bead = pygame.image.load('images/player_bead.png')
opponent_bead = pygame.image.load('images/opponent_bead.png')
buttons = [pygame.image.load('images/Player1.png'),pygame.image.load('images/Player2.png'),pygame.image.load('images/YesButton.png'),pygame.image.load('images/NoButton.png')]
selection = pygame.image.load('images/selection.png')
prompt_scr = pygame.image.load('images/ExitToMainMenuPrompt.png').convert_alpha()