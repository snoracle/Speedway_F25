
## Change background in future

def idle():
    ## Idle screen. Plays after completion and before start of new game
    global screen
    
    idle_font = pygame.font.Font(pygame.font.match_font("sans", bold=True, italic=False), 96)
    screen.fill((128,0,0))
    idle_text = idle_font.render("Indy 500 Pit Stop Simulator", True, (255,255,255))
    idle_rect = idle_text.get_rect()
    idle_rect.center = [screen.get_width() *0.5, screen.get_height()*0.5]
    screen.blit(idle_text, idle_rect)
    pygame.display.flip()
    
    global sensors_dict
    game_start_input = Button(sensors_dict["GAME_START"])
    while True:
        #print("idling")

        if game_start_input.value:
            #print("countdown")
            countdown()
        
        sleep(1)
