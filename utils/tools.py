import pygame, sys

def game_intro(screen_size, colors, fonts, screen):
    intro = True
    game = None
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit('You exited the game')

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game = 'slither_class'
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit('You exited the game')

        screen.fill(colors['white'])
        msg2screen("Welcome to Game of Snake", colors['green'], -120, "large",\
                    fonts, screen_size, screen)
        msg2screen(("You are Slither the Snake and you can't wait to taste "
                   "those forbidden fruits!"),\
                    colors['black'], -30, "small", fonts, screen_size, screen)
        msg2screen("The more apples you eat, the longer you get...",\
                    colors['black'], 10, "small", fonts, screen_size, screen)
        msg2screen("Don't bite into yourself, because you will die!",\
                    colors['black'], 50, "small", fonts, screen_size, screen)
        msg2screen("press S to start Slither",\
                    colors['black'], 150, "small", fonts, screen_size, screen)
        msg2screen("Press Q to quit",\
                    colors['black'], 180, "small", fonts, screen_size, screen)
        pygame.display.update()
    return game

# general text object
def text_obj(text, color, size, fonts):
    if size == 'small':
        textSurf = fonts['smallfont'].render(text, True, color)
    elif size == 'medium':
        textSurf = fonts['medfont'].render(text, True, color)
    elif size == 'large':
        textSurf = fonts['bigfont'].render(text, True, color)
    return textSurf, textSurf.get_rect()

# general message on screen
def msg2screen(msg, color, y_displace, size, fonts, screen_size, screen):
    textSurf, textRect = text_obj(msg, color, size, fonts)
    textRect.center = (screen_size[0] / 2), (screen_size[1] / 2) + y_displace
    screen.blit(textSurf, textRect)

def pause(score, colors, fonts, screen_size, screen):
    paused = True
    switch = True
    msg2screen("Paused", colors['green'], -100, "large", fonts, screen_size, screen)
    msg2screen("Press C to continue or Q to quit the current game.", \
        colors['green'], 25, "medium", fonts, screen_size, screen)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    game_over(score, colors, fonts, screen_size, screen)
                    switch = False
                    paused = False
    return switch

def game_over(score, colors, fonts, screen_size, screen):
    gameover = True
    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit('You exited the game')
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    gameover = False

        screen.fill(colors['white'])
        msg2screen("Game Over", colors['green'], -120, "large",\
                    fonts, screen_size, screen)
        if score == 1:
            msg2screen(("Slither has eaten only 1 apple.".format(score)),\
                       colors['red'], -30, "small", fonts, screen_size, screen)
        else:
            msg2screen(("Slither has eaten {} apples.".format(score)),\
                       colors['red'], -30, "small", fonts, screen_size, screen)

        msg2screen("Press M to return to the Main Menu",\
                    colors['black'], 180, "small", fonts, screen_size, screen)

        pygame.display.update()

def score_menu(width, score, level, colors, fonts, screen_size, screen):
    scoretext = text_obj("Score {0}".format(score), \
                colors['black'], 'medium', fonts)
    pygame.draw.lines(screen, colors['black'], False, \
     [(0, screen_size[1] - width), (screen_size[0], screen_size[1] - width)], 1)
    screen.blit(scoretext[0], (1, screen_size[1] - width + 1))
    
    leveltext = text_obj("Level {0}".format(level), \
                colors['black'], 'medium', fonts)
    screen.blit(leveltext[0], (screen_size[0] - leveltext[1][2], screen_size[1] - width + 1))
