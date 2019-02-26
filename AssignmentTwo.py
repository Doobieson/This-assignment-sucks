# DATA 211
# ASSIGNMENT 2
# RICARDO CRUZ (30074052) AND COOPER CHUNG (30061289)
# RICARDO CRUZ 50%, COOPER CHUNG 50%
# LAB: B03
# DATE: FEBRUARY 28th, Winter 2019

from SimpleGraphics import *

# Introduce program, make user aware of choices (Add more comments)
print("There are two types of charts:")
print("1 = Bar Chart")
print("2 = Pie Chart")

# Gather user input on what chart to produce
graphType = int(input("What type of chart would you like to create?: "))

# Makes a loop to create either a bar chart or pie chart based on the value of "graphType"
if graphType == 1:

    # Establishes useful constants (SUBJECT TO CHANGE, BAR SPACING IS INCOMPLETE)
    BAR_WIDTH = 100
    X_AXIS_LENGTH = 500
    X_AXIS_CENTER = 250
    Y_AXIS_HEIGHT = 400
    Y_AXIS_CENTER = 200
    BAR_SPACING = 50 ### MAKE CHANGE
    X_ORIGIN = 165
    Y_ORIGIN = 500
    LABEL_SPACING = 30
    LINE_SPACING = 15

    # Gathers user input for title and number of bars
    barChartName = input("Enter a title for the chart: ")
    yAxisName = input("Enter a name for the y-axis: ")
    barCount = int(input("How many bars would you like?: "))

    setColor("black") # TITLE
    setFont("Arial", "24", "bold")
    text(X_ORIGIN + X_AXIS_CENTER, Y_ORIGIN - 450, barChartName)

    setColor("white") # CHART BACKGROUND
    rect(X_ORIGIN, Y_ORIGIN, X_AXIS_LENGTH, -Y_AXIS_HEIGHT)

    setColor("black") # X-AXIS
    line(X_ORIGIN, Y_ORIGIN, X_ORIGIN + X_AXIS_LENGTH, Y_ORIGIN)

    setColor("black") # Y-AXIS
    line(X_ORIGIN, Y_ORIGIN, X_ORIGIN, Y_ORIGIN - Y_AXIS_HEIGHT)

    setColor("black") # Y-AXIS LABEL
    setFont("Arial", "10", "bold")
    text(X_ORIGIN - LABEL_SPACING, Y_ORIGIN - Y_AXIS_CENTER, yAxisName)

    setColor("black") # Y-AXIS ON THE OTHER SIDE
    line(X_ORIGIN + X_AXIS_LENGTH, Y_ORIGIN, X_ORIGIN + X_AXIS_LENGTH, Y_ORIGIN - Y_AXIS_HEIGHT)

    setColor("black") # CREATES GRIDLINE FOR 100
    line(X_ORIGIN, Y_ORIGIN - 100, X_ORIGIN + X_AXIS_LENGTH, Y_ORIGIN - 100)

    setColor("black") # CREATES GRIDLINE FOR 200
    line(X_ORIGIN, Y_ORIGIN - 200, X_ORIGIN + X_AXIS_LENGTH, Y_ORIGIN - 200)

    setColor("black") # CREATES GRIDLINE FOR 300
    line(X_ORIGIN, Y_ORIGIN - 300, X_ORIGIN + X_AXIS_LENGTH, Y_ORIGIN - 300)

    setColor("black") # CREATES GRIDLINE FOR 400
    line(X_ORIGIN, Y_ORIGIN - 400, X_ORIGIN + X_AXIS_LENGTH, Y_ORIGIN - 400)

    setColor("black") # 0 Y-AXIS MARKER
    setFont("Arial", "10")
    text(X_ORIGIN + X_AXIS_LENGTH + LABEL_SPACING, Y_ORIGIN, "0")

    setColor("black") # 100 Y-AXIS MARKER
    setFont("Arial", "10")
    text(X_ORIGIN + X_AXIS_LENGTH + LABEL_SPACING, Y_ORIGIN - 100, "100")

    setColor("black") # 200 Y-AXIS MARKER
    setFont("Arial", "10")
    text(X_ORIGIN + X_AXIS_LENGTH + LABEL_SPACING, Y_ORIGIN - 200, "200")

    setColor("black") # 300 Y-AXIS MARKER
    setFont("Arial", "10")
    text(X_ORIGIN + X_AXIS_LENGTH + LABEL_SPACING, Y_ORIGIN - 300, "300")

    setColor("black") # 400 Y-AXIS MARKER
    setFont("Arial", "10")
    text(X_ORIGIN + X_AXIS_LENGTH + LABEL_SPACING, Y_ORIGIN - 400, "400")

    # These "if/elif barCount == #:" loops (line 72 - 191) are used to create the number of bars the user specifies (INCOMPLETE, GOAL IS TO SHRINK THIS DOWN TO MORE EFFICIENT CODE)
    if barCount == 2:
        barOneHeight = int(input("Enter a height for the first bar: "))
        barOneColour = input("Pick a colour for the first bar: ")

        barTwoHeight = int(input("Enter a height for the second bar: "))
        barTwoColour = input("Pick a colour for the second bar: ")

        setFill(barOneColour)
        rect(X_ORIGIN + BAR_SPACING, Y_ORIGIN - barOneHeight, BAR_WIDTH, barOneHeight)

        setFill(barTwoColour)
        rect(X_ORIGIN + BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barTwoHeight, BAR_WIDTH, barTwoHeight)
    elif barCount == 3:
        barOneHeight = int(input("Enter a height for the first bar: "))
        barOneColour = input("Pick a colour for the first bar: ")

        barTwoHeight = int(input("Enter a height for the second bar: "))
        barTwoColour = input("Pick a colour for the second bar: ")

        barThreeHeight = int(input("Enter a height for the third bar: "))
        barThreeColour = input("Pick a colour for the third bar: ")

        setFill(barOneColour)
        rect(X_ORIGIN + BAR_SPACING, Y_ORIGIN - barOneHeight, BAR_WIDTH, barOneHeight)

        setFill(barTwoColour)
        rect(X_ORIGIN + BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barTwoHeight, BAR_WIDTH, barTwoHeight)

        setFill(barThreeColour)
        rect(X_ORIGIN + 2 * BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barThreeHeight, BAR_WIDTH, barThreeHeight)
    elif barCount == 4: 
        barOneHeight = int(input("Enter a height for the first bar: "))
        barOneColour = input("Pick a colour for the first bar: ")

        barTwoHeight = int(input("Enter a height for the second bar: "))
        barTwoColour = input("Pick a colour for the second bar: ")

        barThreeHeight = int(input("Enter a height for the third bar: "))
        barThreeColour = input("Pick a colour for the third bar: ")

        barFourHeight = int(input("Enter a height for the fourth bar: "))
        barFourColour = input("Pick a colour for the fourth bar: ")

        setFill(barOneColour)
        rect(X_ORIGIN + BAR_SPACING, Y_ORIGIN - barOneHeight, BAR_WIDTH, barOneHeight)

        setFill(barTwoColour)
        rect(X_ORIGIN + BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barTwoHeight, BAR_WIDTH, barTwoHeight)

        setFill(barThreeColour)
        rect(X_ORIGIN + 2 * BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barThreeHeight, BAR_WIDTH, barThreeHeight)

        setFill(barFourColour)
        rect(X_ORIGIN + 3 * BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barFourHeight, BAR_WIDTH, barFourHeight)
    elif barCount == 5: 
        barOneHeight = int(input("Enter a height for the first bar: "))
        barOneColour = input("Pick a colour for the first bar: ")

        barTwoHeight = int(input("Enter a height for the second bar: "))
        barTwoColour = input("Pick a colour for the second bar: ")

        barThreeHeight = int(input("Enter a height for the third bar: "))
        barThreeColour = input("Pick a colour for the third bar: ")

        barFourHeight = int(input("Enter a height for the fourth bar: "))
        barFourColour = input("Pick a colour for the fourth bar: ")

        barFiveHeight = int(input("Enter a height for the fifth bar: "))
        barFiveColour = input("Pick a colour for the fifth bar: ")

        setFill(barOneColour)
        rect(X_ORIGIN + BAR_SPACING, Y_ORIGIN - barOneHeight, BAR_WIDTH, barOneHeight)

        setFill(barTwoColour)
        rect(X_ORIGIN + BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barTwoHeight, BAR_WIDTH, barTwoHeight)

        setFill(barThreeColour)
        rect(X_ORIGIN + 2 * BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barThreeHeight, BAR_WIDTH, barThreeHeight)

        setFill(barFourColour)
        rect(X_ORIGIN + 3 * BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barFourHeight, BAR_WIDTH, barFourHeight)

        setFill(barFiveColour)
        rect(X_ORIGIN + 4 * BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barFiveHeight, BAR_WIDTH, barFiveHeight)
    elif barCount == 6: 
        barOneHeight = int(input("Enter a height for the first bar: "))
        barOneColour = input("Pick a colour for the first bar: ")

        barTwoHeight = int(input("Enter a height for the second bar: "))
        barTwoColour = input("Pick a colour for the second bar: ")

        barThreeHeight = int(input("Enter a height for the third bar: "))
        barThreeColour = input("Pick a colour for the third bar: ")

        barFourHeight = int(input("Enter a height for the fourth bar: "))
        barFourColour = input("Pick a colour for the fourth bar: ")

        barFiveHeight = int(input("Enter a height for the fifth bar: "))
        barFiveColour = input("Pick a colour for the fifth bar: ")

        barSixHeight = int(input("Enter a height for the sixth bar: "))
        barSixColour = input("Pick a colour for the sixth bar: ")

        setFill(barOneColour)
        rect(X_ORIGIN + BAR_SPACING, Y_ORIGIN - barOneHeight, BAR_WIDTH, barOneHeight)

        setFill(barTwoColour)
        rect(X_ORIGIN + BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barTwoHeight, BAR_WIDTH, barTwoHeight)

        setFill(barThreeColour)
        rect(X_ORIGIN + 2 * BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barThreeHeight, BAR_WIDTH, barThreeHeight)

        setFill(barFourColour)
        rect(X_ORIGIN + 3 * BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barFourHeight, BAR_WIDTH, barFourHeight)

        setFill(barFiveColour)
        rect(X_ORIGIN + 4 * BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barFiveHeight, BAR_WIDTH, barFiveHeight)

        setFill(barSixColour)
        rect(X_ORIGIN + 5 * BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barSixHeight, BAR_WIDTH, barSixHeight)
    print("Your chart is completed")
elif graphType == 2:

    pieChartName = input("Enter a title for the chart: ")

    setFont("Arial", "24", "bold")
    text(400, 50, pieChartName)

    diameter = int(input("What would you like the diameter of the pie chart to be?: "))
    width = height = diameter

    ORIGIN = 360

    sliceCount = int(input("How many pie slices would you like the chart to have?: "))
    
    if sliceCount == 2:
        sliceOneName = input("What would you like to name the first pie slice?: ")
        sliceOneSize = int(input("From 0 to 359, how large would you like your first pie slice to be?: "))
        sliceOneColour = input("What would you like the colour of the first slice to be?: ")

        print("The second slice size will be based off your first slice")
        sliceTwoName = input("What would you like to name the second pie slice?: ")
        sliceTwoColour = input("What would you like the colour of the second slice to be?: ")

        setFill(sliceOneColour)
        pieSlice(200, 100, width, height, 0, sliceOneSize)

        setFill(sliceTwoColour)
        pieSlice(200, 100, width, height, sliceOneSize, ORIGIN - sliceOneSize)

        setFont("Arial", "18")
        text(60, 50, sliceOneName)
        text(60, 140, sliceTwoName)

        setFill(sliceOneColour)
        rect(42, 75, 40, 40)

        setFill(sliceTwoColour)
        rect(42, 165, 40, 40)
    elif sliceCount == 3:
        sliceOneName = input("What would you like to name the first pie slice?: ")
        sliceOneSize = int(input("From 0 to 358, how large would you like your first pie slice to be?: "))
        sliceOneColour = input("What would you like the colour of the first slice to be?: ")

        sliceTwoName = input("What would you like to name the second pie slice?: ")
        sliceTwoSize = int(input("From size of the first slice to 359, how large would you like your second pie slice to be?: "))
        sliceTwoColour = input("What would you like the colour of the second slice to be?: ")

        print("The third slice size will be based off your other two slices")
        sliceThreeName = input("What would you like to name the third pie slice?: ")
        sliceThreeColour=input("what would you like the colour of the second slice to be?: ")

        setFill(sliceOneColour)
        pieSlice(200, 100, width, height, 0, sliceOneSize)

        setFill(sliceTwoColour)
        pieSlice(200, 100, width, height, sliceOneSize, sliceTwoSize - sliceOneSize)

        setFill(sliceThreeColour)
        pieSlice(200, 100, width, height, sliceTwoSize, ORIGIN - sliceTwoSize)
        
        setFont("Arial", "18")
        text(60, 50, sliceOneName)
        text(60, 140, sliceTwoName)
        text(60, 230, sliceThreeName)

        setFill(sliceOneColour)
        rect(42, 75, 40, 40)

        setFill(sliceTwoColour)
        rect(42, 165, 40, 40)

        setFill(sliceThreeColour)
        rect(42, 255, 40, 40)
    elif sliceCount == 4:
        sliceOneName = input("What would you like to name the first pie slice?: ")
        sliceOneSize = int(input("From 0 to 357, how large would you like your first pie slice to be?: "))
        sliceOneColour = input("What would you like the colour of the first slice to be?: ")

        sliceTwoName = input("What would you like to name the second pie slice?: ")
        sliceTwoSize = int(input("From size of the first slice to 358, how large would you like your second pie slice to be?: "))
        sliceTwoColour = input("What would you like the colour of the second slice to be?: ")

        sliceThreeName = input("What would you like to name the third pie slice?: ")
        sliceThreeSize = int(input("From size of the second slice to 359, how large would you like your third pie slice to be?: "))
        sliceThreeColour = input("What would you like the colour of the third slice to be?: ")

        print("The fourth slice size will be based off your other three slices")
        sliceFourName = input("What would you like to name the fourth pie slice?: ")
        sliceFourColour = input("What would you like the colour of the fourth slice to be?: ")

        setFill(sliceOneColour)
        pieSlice(200, 100, width, height, 0, sliceOneSize)

        setFill(sliceTwoColour)
        pieSlice(200, 100, width, height, sliceOneSize, sliceTwoSize - sliceOneSize)

        setFill(sliceThreeColour)
        pieSlice(200, 100, width, height, sliceTwoSize, sliceThreeSize - sliceTwoSize)

        setFill(sliceFourColour)
        pieSlice(200, 100, width, height, sliceThreeSize, ORIGIN - sliceThreeSize)

        setFont("Arial", "18")
        text(60, 50, sliceOneName)
        text(60, 140, sliceTwoName)
        text(60, 230, sliceThreeName)
        text(60, 320, sliceFourName)

        setFill(sliceOneColour)
        rect(42, 75, 40, 40)

        setFill(sliceTwoColour)
        rect(42, 165, 40, 40)

        setFill(sliceThreeColour)
        rect(42, 255, 40, 40)

        setFill(sliceFourColour)
        rect(42, 345, 40, 40)
    elif sliceCount == 5:
        sliceOneName = input("What would you like to name the first pie slice?: ")
        sliceOneSize = int(input("From 0 to 355, how large would you like your first pie slice to be?: "))
        sliceOneColour = input("What would you like the colour of the first slice to be?: ")

        sliceTwoName = input("What would you like to name the second pie slice?: ")
        sliceTwoSize = int(input("From size of the first slice to 356, how large would you like your second pie slice to be?: "))
        sliceTwoColour = input("What would you like the colour of the second slice to be?: ")

        sliceThreeName = input("What would you like to name the third pie slice?: ")
        sliceThreeSize = int(input("From size of the second slice to 357, how large would you like your third pie slice to be?: "))
        sliceThreeColour = input("What would you like the colour of the third slice to be?: ")

        sliceFourName = input("What would you like to name the fourth pie slice?: ")
        sliceFourSize = int(input("From size of the third slice to 358, how large would you like your fourth pie slice to be?: "))
        sliceFourColour = input("What would you like the colour of the fourth slice to be?: ")

        print("The fifth slice size will be based off your other four slices")
        sliceFiveName = input("What would you like to name the fifth pie slice?: ")
        sliceFiveColour = input("What would you like the colour of the fifth slice to be?: ")

        setFill(sliceOneColour)
        pieSlice(200, 100, width, height, 0, sliceOneSize)

        setFill(sliceTwoColour)
        pieSlice(200, 100, width, height, sliceOneSize, sliceTwoSize - sliceOneSize)

        setFill(sliceThreeColour)
        pieSlice(200, 100, width, height, sliceTwoSize, sliceThreeSize - sliceTwoSize)

        setFill(sliceFourColour)
        pieSlice(200, 100, width, height, sliceThreeSize, sliceFourSize - sliceThreeSize)

        setFill(sliceFiveColour)
        pieSlice(200, 100, width, height, sliceFourSize, ORIGIN - sliceFourSize)

        setFont("Arial", "18")
        text(60, 50, sliceOneName)
        text(60, 140, sliceTwoName)
        text(60, 230, sliceThreeName)
        text(60, 320, sliceFourName)
        text(60, 410, sliceFiveName)

        setFill(sliceOneColour)
        rect(42, 75, 40, 40)

        setFill(sliceTwoColour)
        rect(42, 165, 40, 40)

        setFill(sliceThreeColour)
        rect(42, 255, 40, 40)

        setFill(sliceFourColour)
        rect(42, 345, 40, 40)

        setFill(sliceFiveColour)
        rect(42, 435, 40, 40)
    elif sliceCount == 6:
        sliceOneName = input("What would you like to name the first pie slice?: ")
        sliceOneSize = int(input("From 0 to 355, how large would you like your first pie slice to be?: "))
        sliceOneColour = input("What would you like the colour of the first slice to be?: ")

        sliceTwoName = input("What would you like to name the second pie slice?: ")
        sliceTwoSize = int(input("From size of the first slice to 356, how large would you like your second pie slice to be?: "))
        sliceTwoColour = input("What would you like the colour of the second slice to be?: ")

        sliceThreeName = input("What would you like to name the third pie slice?: ")
        sliceThreeSize = int(input("From size of the second slice to 357, how large would you like your third pie slice to be?: "))
        sliceThreeColour = input("What would you like the colour of the third slice to be?: ")

        sliceFourName = input("What would you like to name the fourth pie slice?: ")
        sliceFourSize = int(input("From size of the third slice to 358, how large would you like your fourth pie slice to be?: "))
        sliceFourColour = input("What would you like the colour of the fourth slice to be?: ")

        sliceFiveName = input("What would you like to name the fifth pie slice?: ")
        sliceFiveSize = int(input("From size of the fourth slice to 359, how large would you like your fifth pie slice to be?: "))
        sliceFiveColour = input("What would you like the colour of the fifth slice to be?: ")

        print("The sixth slice size will be based off your other five slices")
        sliceSixName = input("What would you like to name the sixth pie slice?: ")
        sliceSixColour = input("What would you like the colour of the sixth slice to be?: ")

        setFill(sliceOneColour)
        pieSlice(200, 100, width, height, 0, sliceOneSize)

        setFill(sliceTwoColour)
        pieSlice(200, 100, width, height, sliceOneSize, sliceTwoSize - sliceOneSize)

        setFill(sliceThreeColour)
        pieSlice(200, 100, width, height, sliceTwoSize, sliceThreeSize - sliceTwoSize)

        setFill(sliceFourColour)
        pieSlice(200, 100, width, height, sliceThreeSize, sliceFourSize - sliceThreeSize)

        setFill(sliceFiveColour)
        pieSlice(200, 100, width, height, sliceFourSize, sliceFiveSize - sliceFourSize)

        setFill(sliceSixColour)
        pieSlice(200, 100, width, height, sliceFiveSize, ORIGIN - sliceFiveSize)

        setFont("Arial", "18")
        text(60, 50, sliceOneName)
        text(60, 140, sliceTwoName)
        text(60, 230, sliceThreeName)
        text(60, 320, sliceFourName)
        text(60, 410, sliceFiveName)
        text(60, 500, sliceSixName)

        setFill(sliceOneColour)
        rect(42, 75, 40, 40)

        setFill(sliceTwoColour)
        rect(42, 165, 40, 40)

        setFill(sliceThreeColour)
        rect(42, 255, 40, 40)

        setFill(sliceFourColour)
        rect(42, 345, 40, 40)

        setFill(sliceFiveColour)
        rect(42, 435, 40, 40)

        setFill(sliceSixColour)
        rect(42, 525, 40, 40)
    print("Your chart is completed")
else:
    print("You have entered an invalid number. Please try again")