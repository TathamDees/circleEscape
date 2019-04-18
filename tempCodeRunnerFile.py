import random
import math
from PyInstaller import *

#Runs the program
def main():
    trials = 0
    currentCoordinates = [0] * 2
    #radius = input("Enter radius of the circle: \n")
    radius = 2
    while getDistFromZero(currentCoordinates) < radius:
        xVal = random.random()
        thePoint = calcCoordinates(xVal , 2)
        for j in range (0 , 1):
            currentCoordinates[j] += thePoint[j]
        print (thePoint)
        print (currentCoordinates)
        print (radius)
        trials += 1
    print ("Trials: " + str(trials))

#Generates a coordinate values for a given x
def calcCoordinates(x , dimensions):
    coordinates = [x]
    for i in range (1 , dimensions):
        y = math.sqrt( 1 - (math.pow(x , 2)))
        coordinates.append(y)
    return coordinates

def getDistFromZero(point):
    return math.pow(point[0] , 2) + math.pow(point[1] , 2)

main()