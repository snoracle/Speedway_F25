import pygame, cv2
def initialize():
 ## main gameplay loop
    
    global sensors_dict
    #Creates wheel and fuel related objects from sensor data
    front_wheel = wheel("Front", sensors_dict["WHEEL_F_PRESENT"], sensors_dict["WHEEL_F_LOCKED"], sensors_dict["WHEEL_F_NEW"])
    rear_wheel = wheel("Rear", sensors_dict["WHEEL_R_PRESENT"], sensors_dict["WHEEL_R_LOCKED"], sensors_dict["WHEEL_R_NEW"])
    fuel = fueltank("Fuel Tank", sensors_dict["FUEL_PROBE"])
    
    global screen, dt, elapsed
    #Set up clock for frame rate control. 
    clock = pygame.time.Clock()
    #Set up fonts for rendering the time 
    clock_font = pygame.font.Font(pygame.font.match_font("7-segment", bold=True, italic=False), 128)
    indicators_font = pygame.font.Font(pygame.font.match_font("sans", bold=True, italic=False), 24)
    clock_font_comp = pygame.font.Font(pygame.font.match_font("7-segment", bold=True, italic=False), 48)
    #Initializing flags and times variables to track wheel and fuel status
    fc = False
    rc = False
    tc = False
    #fc = front wheel complete = false
    #rc = real wheel ...
    #tc = fuel tank complete
    
    fc_time = rc_time = tc_time = "--:--:--"
    #Stores timestamps for when tasks are complete. Probably for leaderboard 
