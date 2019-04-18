import random
import math

#Runs the program
def main():
    runRadiusRange(1000 , 10)

def runFullTrial(radius , num):
    circleRadius = radius
    numTrials = num
    trialList = []
    totalTrials = 0
    for i in range(0 , numTrials):
        trialList.append(runCalculation(circleRadius))
    for i in range (0 , numTrials):
        #print(trialList[i])
        totalTrials += trialList[i].numPoints
    #print()
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

#Determines the point's distance from 0 in an x,y plane
def getDistFromZero(point):
    return math.sqrt(math.pow(point[0] , 2) + math.pow(point[1] , 2))

#returns 1 runthrough of the circle Escape algorithm
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

#runs an experiemnt for each radius within a range
def runRadiusRange(numTrials , maxRadius):
    for i in range(2 , maxRadius + 1):
        print("Trials with radius: " + str(i) )
        runFullTrial(i , numTrials)
        print("")

#class containing the final coordinates of a trial, as well as the number of points used to escape
class trial():
    def __init__(self, coordinates , numPoints):
        self.coordinates = coordinates
        self.numPoints = numPoints

    #formats the return
    def __str__(self):
        return str(str(self.coordinates) + " | " + str(self.numPoints))

#TODO
#Create an output of the average number of trials for 
def makeCSV():
    print("j")

#Notes/Todo
#graph the number of points needed for each experiment (bar graph of #trials required for min to max number of trials in experiment)
#Look into simple random walk. This is a 2D version

main()