import pygame, cv2
from time import sleep
from pitstopsensors import *
from math import floor, sin, cos, pi
from idle import idle #Fall 25
from count import countdown
#from loading import load
from gameloop_initialize import initialize
from gameloop import gameloop


def main():
    #Calls functions
    load()
    idle()
    countdown()
    initialize()
    gameloop()


  
