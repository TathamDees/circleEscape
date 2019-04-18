import random
import math

#Runs the program
def main():
    numTrials = 1000
    circleRadius = 15
    trialList = []
    totalTrials = 0
    for i in range(0 , numTrials):
        trialList.append(runCalculation(circleRadius))
    for i in range (0 , numTrials):
        print(trialList[i])
        totalTrials += trialList[i].numPoints
    print()
    print("Total Trials: " + str(totalTrials))
    print ("Average Number of Trials: " + str(totalTrials / numTrials))

#Generates a coordinate values for a given x
def calcCoordinates(x , dimensions):
    coordinates = [x]
    for i in range (1 , dimensions):
        y = math.sqrt( 1 - (math.pow(x , 2)))
        y = y * random.choice([-1 , 1])
        coordinates.append(y)
    return coordinates

def getDistFromZero(point):
    return math.sqrt(math.pow(point[0] , 2) + math.pow(point[1] , 2))

def runCalculation(circleRadius):
    trials = 0
    currentCoordinates = [0] * 2
    #radius = input("Enter radius of the circle: \n")
    radius = circleRadius
    currentDistance = 0
    #print ("radius: " + str(radius))
    while currentDistance < radius:
        xVal = random.uniform(-1 , 1)
        thePoint = calcCoordinates(xVal , 2)
        for j in range (0 , 2):
            currentCoordinates[j] += thePoint[j]
        trials += 1
        currentDistance = getDistFromZero(currentCoordinates)
        #print ("Point: " + str(thePoint))
        #print ("Current Coordinates: " + str(currentCoordinates))
        #print ("Current Distance: " + str(currentDistance) + "\n")
    #print ("Trials: " + str(trials) + "\n")
    outputTrial = trial(currentCoordinates ,trials )
    return outputTrial

class trial():
    def __init__(self, coordinates , numPoints):
        self.coordinates = coordinates
        self.numPoints = numPoints

    def __str__(self):
        return str(str(self.coordinates) + " | " + str(self.numPoints))

def makeCSV():
    print("j")

main()