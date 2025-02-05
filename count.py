#Countdown after display.py

def countdown():
    global screen
    ## play coutndown video from here
    
    
    ## find some multimedia library that can call back to here when the video is done playing, then initiate the game
    ## for now there is just gonna be a cute little for loop here
    
    ## using cv2
    
    intro_video = cv2.VideoCapture(INTRO_VIDEO_FILE)
    success, video_frame = intro_video.read()
    playback = success
    clock = pygame.time.Clock()
    
#    fps = video.get(cv2.CAP_PROP_FPS)
    while playback:
        clock.tick(23.976024)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playback = false
        success, video_frame = intro_video.read()
        if success:
            #print(str(video_frame.shape[1::-1]))
            video_blit = pygame.image.frombuffer(video_frame.tobytes(), video_frame.shape[1::-1], "BGR")
            video_blit = pygame.transform.scale(video_blit, (screen.get_width(),screen.get_height()))
        else:
            print("huh")
            playback = False
        screen.blit(video_blit, (0,0))
        pygame.display.flip()
                
    
    
    
    countdown_font = pygame.font.Font(pygame.font.match_font("sans", bold=True, italic=False), 160)
    screen.fill((128,0,0))
    pygame.display.flip()
    
    for i in range(1, 4):
        screen.fill((128,0,0))
        cd_text = countdown_font.render(str(4- i), True, (255,255,255))
        cd_rect = cd_text.get_rect()
        cd_rect.center = [screen.get_width() *0.5, screen.get_height()*0.5]
        screen.blit(cd_text, cd_rect)
        pygame.display.flip()
        sleep(1)
