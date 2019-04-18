import random
import math
from PyInstaller import *

#Runs the program
def main():
    for i in range(0 , 3):
        
        runTrial()

#Generates a coordinate values for a given x
def calcCoordinates(x , dimensions):
    coordinates = [x]
    for i in range (1 , dimensions):
        y = math.sqrt( 1 - (math.pow(x , 2)))
        y = y * random.choice([-1 , 1])
        coordinates.append(y)
    return coordinates

def getDistFromZero(point):
    return math.pow(point[0] , 2) + math.pow(point[1] , 2)

def runTrial():
    trials = 0
    currentCoordinates = [0] * 2
    #radius = input("Enter radius of the circle: \n")
    
    radius = 2
    currentDistance = 0
    print ("radius: " + str(radius))
    while currentDistance < radius:
        xVal = random.uniform(-1 , 1)
        thePoint = calcCoordinates(xVal , 2)
        for j in range (0 , 2):
            currentCoordinates[j] += thePoint[j]
        trials += 5
        currentDistance = getDistFromZero(currentCoordinates)
        print ("Point: " + str(thePoint))
        print ("Current Coordinates: " + str(currentCoordinates))
        print ("Current Distance: " + str(currentDistance) + "\n")
    print ("Trials: " + str(trials))
    return currentCoordinates , trials

#def trial:
#    current

main()