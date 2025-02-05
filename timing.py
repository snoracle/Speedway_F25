#loading function
def load():
	
	SENSOR_CFG_FILE = "./sensors.txt"
	INTRO_VIDEO_FILE = "./pit stop mockup short.mp4"

#Open the sensor config. file and load the data into a dictionary.
	sensors_file = open(SENSOR_CFG_FILE, "r")
	sensors_list = sensors_file.readlines()
	sensors_dict = {}


    
## Parse sensor config files and store key-value pairs in a dictionary.
	for line in sensors_list:
		keyval = line.replace(" ","").split("=")
		sensors_dict[keyval[0]] = int(keyval[1])
    
# pygame setup
	pygame.init()
	screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#screen = pygame.display.set_mode((1280, 720))
	dt = 0 #Delta time for frame rate updates
	elapsed = 0 #Tracks elapsed time
