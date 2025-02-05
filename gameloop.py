#Primary Game Loop
from idle import idle
def gameloop():
  while True:
        front_wheel.update()
        rear_wheel.update()
        fuel.update()
        
        
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0,0,128)) #Clear scree. Blue backgrnd
        
        # Update and display timer in mm:ss:ms format
        if (not (fc and rc and tc)):
            millisc = floor((elapsed - floor(elapsed)) * 100)
            seconds = floor(elapsed) % 60
            minutes = floor(elapsed / 60)
            timestr = str(minutes).rjust(2, '0') + ":" + str(seconds).rjust(2, '0') + ":" + str(millisc).rjust(2, '0')
            #timestr is the time itself and stores any times
        clock_text = clock_font.render(timestr, True, (255, 255, 255)) #Renders and displays time
        clock_rect = clock_text.get_rect() #Get the area for position the time. Should be low center
        clock_rect.center = [screen.get_width() *0.5, screen.get_height()*0.875]
        screen.blit(clock_text, clock_rect)
        
        #Render the sensor data in the front wheel as either present, lcoked, new, valid, or complete
        fwp_text = indicators_font.render("FW PRESENT: " + str(front_wheel.get_present()), True, (255* int(not front_wheel.get_present()), 255 * int(front_wheel.get_present()), 0))
        fwp_rect = fwp_text.get_rect()
        fwp_rect.center = [screen.get_width() *0.25, screen.get_height()*0.25]
        screen.blit(fwp_text, fwp_rect)
        
        #Fron wheel present
        fwl_text = indicators_font.render("FW LOCKED: " + str(front_wheel.get_locked()), True, (255* int(not front_wheel.get_locked()), 255 * int(front_wheel.get_locked()), 0))
        fwl_rect = fwl_text.get_rect()
        fwl_rect.center = [screen.get_width() *0.25, screen.get_height()*0.30]
        screen.blit(fwl_text, fwl_rect)
        
        #Front wheel new
        fwn_text = indicators_font.render("FW NEW: " + str(front_wheel.new), True, (255* int(not front_wheel.new), 255 * int(front_wheel.new), 0))
        fwn_rect = fwn_text.get_rect()
        fwn_rect.center = [screen.get_width() *0.25, screen.get_height()*0.35]
        screen.blit(fwn_text, fwn_rect)
        
        #Front wheel valid
        fwv_text = indicators_font.render("FW VALID: " + str(front_wheel.get_valid()), True, (255* int(not front_wheel.get_valid()), 255 * int(front_wheel.get_valid()), 0))
        fwv_rect = fwv_text.get_rect()
        fwv_rect.center = [screen.get_width() *0.25, screen.get_height()*0.40]
        screen.blit(fwv_text, fwv_rect)
        
        #Front wheel complete
        fwc_text = indicators_font.render("FW COMPLETE: " + str(front_wheel.get_complete()), True, (255* int(not front_wheel.get_complete()), 255 * int(front_wheel.get_complete()), 0))
        fwc_rect = fwc_text.get_rect()
        fwc_rect.center = [screen.get_width() *0.25, screen.get_height()*0.45]
        screen.blit(fwc_text, fwc_rect)
        
        #Repeat for rear wheel. Same format as the front wheel
        rwp_text = indicators_font.render("RW PRESENT: " + str(rear_wheel.get_present()), True, (255* int(not rear_wheel.get_present()), 255 * int(rear_wheel.get_present()), 0))
        rwp_rect = rwp_text.get_rect()
        rwp_rect.center = [screen.get_width() *0.75, screen.get_height()*0.25]
        screen.blit(rwp_text, rwp_rect)
        
        rwl_text = indicators_font.render("RW LOCKED: " + str(rear_wheel.get_locked()), True, (255* int(not rear_wheel.get_locked()), 255 * int(rear_wheel.get_locked()), 0))
        rwl_rect = rwl_text.get_rect()
        rwl_rect.center = [screen.get_width() *0.75, screen.get_height()*0.30]
        screen.blit(rwl_text, rwl_rect)
        
        rwn_text = indicators_font.render("RW NEW: " + str(rear_wheel.new), True, (255* int(not rear_wheel.new), 255 * int(rear_wheel.new), 0))
        rwn_rect = rwn_text.get_rect()
        rwn_rect.center = [screen.get_width() *0.75, screen.get_height()*0.35]
        screen.blit(rwn_text, rwn_rect)
        
        rwv_text = indicators_font.render("RW VALID: " + str(rear_wheel.get_valid()), True, (255* int(not rear_wheel.get_valid()), 255 * int(rear_wheel.get_valid()), 0))
        rwv_rect = rwv_text.get_rect()
        rwv_rect.center = [screen.get_width() *0.75, screen.get_height()*0.40]
        screen.blit(rwv_text, rwv_rect)
        
        rwc_text = indicators_font.render("RW COMPLETE: " + str(rear_wheel.get_complete()), True, (255* int(not rear_wheel.get_complete()), 255 * int(rear_wheel.get_complete()), 0))
        rwc_rect = rwc_text.get_rect()
        rwc_rect.center = [screen.get_width() *0.75, screen.get_height()*0.45]
        screen.blit(rwc_text, rwc_rect)
        
        #Check for wheel complettion and record the time when complete
        if ((not fc) and front_wheel.get_complete()):
            fc = True
            fc_time = timestr
            #Records time of front wheel completion
        if ((not rc) and rear_wheel.get_complete()):
            rc = True
            rc_time = timestr
            #Records time of rear wheel completion
        #Display each time of completion per segment
        clock_fc_text = clock_font_comp.render(fc_time, True, (255, 255, 255))
        clock_fc_rect = clock_fc_text.get_rect()
        clock_fc_rect.center = [screen.get_width() *0.25, screen.get_height()*0.675]
        screen.blit(clock_fc_text, clock_fc_rect)
        
        clock_rc_text = clock_font_comp.render(rc_time, True, (255, 255, 255))
        clock_rc_rect = clock_rc_text.get_rect()
        clock_rc_rect.center = [screen.get_width() *0.75, screen.get_height()*0.675]
        screen.blit(clock_rc_text, clock_rc_rect)
        
        #Render data for the fuel tank. Whether it is present, full, and level
        tp_text = indicators_font.render("FUEL HOSE INSERTED: " + str(fuel.get_probe()), True, (255* int(not fuel.get_probe()), 255 * int(fuel.get_probe()), 0))
        tp_rect = tp_text.get_rect()
        tp_rect.center = [screen.get_width() *0.5, screen.get_height()*0.25]
        screen.blit(tp_text, tp_rect)
        
        tf_text = indicators_font.render("FUEL TANK FULL: " + str(fuel.get_full()), True, (255* int(not fuel.get_full()), 255 * int(fuel.get_full()), 0))
        tf_rect = tf_text.get_rect()
        tf_rect.center = [screen.get_width() *0.5, screen.get_height()*0.30]
        screen.blit(tf_text, tf_rect)
        
        tl_text = indicators_font.render("FUEL TANK LEVEL: " + str(floor(fuel.get_level())) +"%", True, (0,255,0))
        tl_rect = tf_text.get_rect()
        tl_rect.center = [screen.get_width() *0.5, screen.get_height()*0.35]
        screen.blit(tl_text, tl_rect)
        
        #Check if fuel tank full. If so, record completion time
        if ((not tc) and fuel.get_full()):
            tc = True
            tc_time = timestr
        #Render fuel tank completion time
        clock_tc_text = clock_font_comp.render(tc_time, True, (255, 255, 255))
        clock_tc_rect = clock_fc_text.get_rect()
        clock_tc_rect.center = [screen.get_width() *0.5, screen.get_height()*0.675]
        screen.blit(clock_tc_text, clock_tc_rect)
       
        # flip() the display to put your work on screen
        #Also updates the screen display
        pygame.display.flip()
        

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000
        elapsed += dt
    

idle()
