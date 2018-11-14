'''

@author: colinoriordan
@StudentID: R00133939
@Email: colin.r.oriordan@mycit.ie

Application is a basic data analysis application that enables us to
examine information on the rainfall in various parts of Ireland for each month over the past half
century.

'''

# import modules
import sys
import numpy as np

# create global dictionary of file paths
file_locations = {
    1: "CorkRainfall.txt",
    2: "BelfastRainfall.txt",
    3: "DublinRainfall.txt",
    4: "GalwayRainfall.txt",
    5: "LimerickRainfall.txt"
}

# create global dictionary of location names
locations = {
    1: "Cork",
    2: "Belfast",
    3: "Dublin",
    4: "Galway",
    5: "Limerick"
}


# main function of the application
def main_menu():
    # Verifies the program is being run with python version 3.0 or later
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or a more recent version is required.")

    # create the boolean variable close to decide when our loop ends
    close = False

    while close is False:

        # create the boolean variable valid_int to decide when our loop ends
        valid_int = False

        # we display our menu on screen
        print("\n\n Menu")
        print("\n1. Basic Statistics for Total Rainfall (Millimetres)")
        print("\n2. Basic Statistics for Most Rainfall in a Day (Millimetres)")
        print("\n3. Basic Statistics for Number of Rain days (0.2mm or More)")
        print("\n4. Wettest Location")
        print("\n5. Percentage of Rain Days")
        print("\n6. Exit")

        # loop the users input until a valid int is entered in range 1-6
        while valid_int is False:

            # throws exception if the response is not an integer
            try:
                choice = int(input("\nPlease select one of the above options:"))
            except ValueError:
                print("\nThis is not a valid option. Integer 1-6")
                continue

            # print error if response is not in correct range 1-6
            if choice in range(1, 7):
                valid_int = True
            else:
                print("\nThis is not a valid option. Integer 1-6")

        # select a function call based on user's response'
        if choice in range(1, 4):
            calculateMaxAvg(choice)
        elif choice == 4:
            wettest_location()
        elif choice == 5:
            pc_rain_days()
        elif choice == 6:
            close = True

    sys.exit()


def calculateMaxAvg(selection):

    # display our menu to user
    print("\n1. Cork")
    print("\n2. Belfast")
    print("\n3. Dublin")
    print("\n4. Galway")
    print("\n5. Limerick")

    # create the boolean variable valid_int to decide when our loop ends
    valid_int = False
    choice = -1

    # loop the users input until a valid int is entered in range 1-5
    while valid_int is False:

        # throws exception if the response is not an integer
        try:
            choice = int(input("\nPlease select a location:"))
        except ValueError:
            print("\nThis is not a valid option. Integer 1-5")
            continue

        # print error if response is not in correct range 1-5
        if choice in range(1, 6):
            valid_int = True
        else:
            print("\nThis is not a valid option. Integer 1-5")

    # declare global dictionary file_locations and locations in this function's scope
    global file_locations, locations

    # retrieve appropriate values from dictionaries
    fileLocation = file_locations[choice]
    location = locations[choice]

    # generate MD array from .txt file
    data = np.genfromtxt(fileLocation, dtype=float, delimiter=None)

    # determine column of which the array is to be made
    column = (selection+1)

    # create array of:
    # col 2- total rainfall of months
    # col 3- most rainfall in a day
    # col 4- number of rain days
    arr = data[:, column]

    # calculate max (total rainfall of months / most rainfall in a day / number of rain days)
    max = np.amax(arr)

    # calculate avg (total rainfall of months / most rainfall in a day / number of rain days)
    avg = np.mean(arr)

    # print max & avg
    if selection==1:
        print("\n%s: Max Total Rainfall = %.2f" % (location, max))
        print("\n%s: Avg Total Rainfall = %.2f" % (location, avg))
    elif selection==2:
        print("\n%s: Max Most Rainfall in a Day = %.2f" % (location, max))
        print("\n%s: Avg Most Rainfall in a Day = %.2f" % (location, avg))
    elif selection==3:
        print("\n%s: Max Number of Rain days = %.2f" % (location, max))
        print("\n%s: Avg Number of Rain days = %.2f" % (location, avg))


def wettest_location():

    # declare global dictionary file_locations and locations in this function's scope
    global file_locations, locations

    # declare our max values to be assigned
    maxCumulativeRainfall=0
    wettestLocation=""

    # We traverse our locations
    for counter in range(1, 6):

        # retrieve appropriate values from dictionaries
        filelocation = file_locations[counter]
        location = locations[counter]

        # generate MD array from .txt file
        data = np.genfromtxt(filelocation, dtype=float, delimiter=None)

        # create array of total rainfall of month values
        arr = data[:, 2]

        # calculate the cumulative rainfall of the current location by getting the sum of it's total rainfall values
        currentCumulativeRainfall = np.sum(arr)

        # if the current cumulative rainfall is greater than our max, then it becomes the max
        if currentCumulativeRainfall > maxCumulativeRainfall:
            maxCumulativeRainfall = currentCumulativeRainfall
            wettestLocation = location

        # print the current month's cumulative rainfall
        print("%d. %s %.2fmm" % (counter, location, currentCumulativeRainfall))

    # print what we found to be the wettest month
    print("The wettest location in Ireland is %s with a rainfall figure of %.2fmm" % (wettestLocation, maxCumulativeRainfall))


def pc_rain_days():

    # create the boolean variable valid_int to decide when our loop ends
    valid_int = False
    threshold = -1

    # loop the users input until a valid int is entered in range 1-32
    while valid_int is False:

        # throws exception if the response is not an integer
        try:
            threshold = int(input("\nPlease enter maximum threshold value for number of rain days: "))
        except ValueError:
            print("\nThis is not a valid option. Integer 1-32")
            continue

        # print error if response is not in correct range
        if threshold in range(1, 32):
            valid_int = True
        else:
            print("\nThis is not a valid option. Integer 1-32")

    # print our header
    print("The following are the percentage of rain days less than or equal to %d:" % threshold)

    # We traverse our locations
    for counter in range(1, 6):

        # retrieve appropriate values from dictionaries
        filelocation = file_locations[counter]
        location = locations[counter]

        # generate MD array from .txt file
        data = np.genfromtxt(filelocation, dtype=float, delimiter=None)

        # create array of all rain day values of this location
        arr = data[:, 4]

        # create a results array of rain days less than or equal to our threshold for this location
        result = (arr <= threshold)

        # determine % by the number of days below threshold divided by total number of days and multiplied by 100
        percentage = ((len(data[result])/len(arr))*100.00)

        # print our current locations results
        print("%d. %s %.2f%%" % (counter, location, percentage))



main_menu()
