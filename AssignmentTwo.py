# DATA 211
# ASSIGNMENT 2
# NAME (ID): RICARDO CRUZ (30074052) AND COOPER CHUNG (30061289)
# RICARDO CRUZ 50%, COOPER CHUNG 50%
# LAB: B03
# DATE: FEBRUARY 28th, 2019

# Bar chart: line 21 - 303
# Pie chart: line 306 - 564

from SimpleGraphics import *

# Introduce program, notify user of choices
print("There are two types of charts:")
print("1 = Bar Chart")
print("2 = Pie Chart")

graphType = int(input("What type of chart would you like to create?: ")) # Gather user input on what chart type to produce

# Makes a loop to create a bar chart or pie chart based on the value of "graphType" (1 for bar, 2 for pie)
if graphType == 1:

    # Establishes useful constants
    BAR_WIDTH = 80
    X_AXIS_LENGTH = 500 # 500 pixels long to ensure 100 pixel margin on both sides
    X_AXIS_CENTER = 250
    Y_AXIS_HEIGHT = 400 # 400 pixels tall because maximum height is 400
    Y_AXIS_CENTER = 200
    X_ORIGIN = 165
    Y_ORIGIN = 500
    LABEL_SPACING = 25  # Universal spacing for all labels on chart for continuity

    # Gathers user input for title, number of bars, gridline interval, and y-axis label
    barChartName = input("Enter a title for the chart: ")
    barCount = int(input("How many bars would you like?: "))
    intervalValue = int(input("What increment would you like the gridlines to increase by?: "))
    yAxisName = input("Enter a name for the y-axis: ")

    setColor("black") # Creates title (Height was arbitrary, subtracted 450 pixels instead of adding beacause the y-axis is flipped, also to make it look clean)
    setFont("Arial", "24", "bold")
    text(X_ORIGIN + X_AXIS_CENTER, Y_ORIGIN - 450, barChartName)

    setColor("white") # Creates a white background for the chart for ease of vision
    rect(X_ORIGIN, Y_ORIGIN, X_AXIS_LENGTH, -Y_AXIS_HEIGHT)

    setColor("black") # Creates x-axis, also uses the X_AXIS_LENGTH constant to ensure chart is 500 pixels wide
    line(X_ORIGIN, Y_ORIGIN, X_ORIGIN + X_AXIS_LENGTH, Y_ORIGIN)

    setColor("black") # Creates left-most y-axis. Subtracted the y-axis height because y-axis is flipped, also to ensure chart is exactly 400 pixels tall
    line(X_ORIGIN, Y_ORIGIN, X_ORIGIN, Y_ORIGIN - Y_AXIS_HEIGHT)

    setColor("black") # Creates the label for the leftmost y-axis, adjusted 25 pixels to the left using LABEL_SPACING to make it look clean.
    setFont("Arial", "10", "bold")
    text(X_ORIGIN - LABEL_SPACING, Y_ORIGIN - Y_AXIS_CENTER, yAxisName)

    setColor("black") # Creates right-most y-axis to complete the look of the graph
    line(X_ORIGIN + X_AXIS_LENGTH, Y_ORIGIN, X_ORIGIN + X_AXIS_LENGTH, Y_ORIGIN - Y_AXIS_HEIGHT)

    intervalCount = 0 # Establishes a count to be used in the while loop for creating user input gridlines

    # Establishes a while loop that creates gridlines and rulings from user input for interval
    # Also uses 400 as the sentinel value because the maximum height of the chart is 400 pixels
    while intervalCount <= 400:
        setColor("black") # Creates gridlines
        line(X_ORIGIN, Y_ORIGIN - intervalCount, X_ORIGIN + X_AXIS_LENGTH, Y_ORIGIN - intervalCount)

        setColor("black") # Creates rulings
        setFont("Arial", "10", "bold")
        text(X_ORIGIN + X_AXIS_LENGTH + LABEL_SPACING, Y_ORIGIN - intervalCount, intervalCount)

        intervalCount = intervalCount + intervalValue                   # This line is necessary to make the gridlines and rulings properly draw at the user specified interval

    # These "if/elif barCount == #: " loops (line 74 - 303) are used to create the entire bar chart based on user input
    if barCount == 2:
        BAR_SPACING = 170                                               # Establishes calculated useful constants to make chart look clean
        BAR_ONE_CENTER = 210                                            # (different depending on how many bars must be drawn)
        BAR_TWO_CENTER = 290

        barOneLabel = input("Enter a name for the first bar: ")         # Gathers user input for bar labels, height, and colour (more bars = more user inputs)
        barOneHeight = int(input("Enter a value for the first bar: "))
        barOneColour = input("Pick a colour for the first bar: ")

        barTwoLabel = input("Enter a name for the second bar: ")
        barTwoHeight = int(input("Enter a value for the second bar: "))
        barTwoColour = input("Pick a colour for the second bar: ")

        # Draws the chart using rectangles and user specified values
        setFill(barOneColour)
        rect(X_ORIGIN + BAR_SPACING, Y_ORIGIN - barOneHeight, BAR_WIDTH, barOneHeight)

        setFill(barTwoColour)
        rect(X_ORIGIN + BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barTwoHeight, BAR_WIDTH, barTwoHeight)

        # Creates the labels under and on top of the bars
        setColor("black")
        setFont("Arial", "10", "bold")
        text(X_ORIGIN  + BAR_ONE_CENTER, Y_ORIGIN + LABEL_SPACING, barOneLabel)
        text(X_ORIGIN  + BAR_ONE_CENTER, Y_ORIGIN - barOneHeight + LABEL_SPACING, barOneHeight)
        text(X_ORIGIN  + BAR_TWO_CENTER, Y_ORIGIN + LABEL_SPACING, barTwoLabel)
        text(X_ORIGIN  + BAR_TWO_CENTER, Y_ORIGIN - barTwoHeight + LABEL_SPACING, barTwoHeight)

        # This process is repeated for up to 6 bars. More bars = Different constants =  More user inputs = More rectangles = More labels
    elif barCount == 3:
        BAR_SPACING = 130
        BAR_ONE_CENTER = 170
        BAR_TWO_CENTER = 250
        BAR_THREE_CENTER = 330

        barOneLabel = input("Enter a name for the first bar: ")
        barOneHeight = int(input("Enter a value for the first bar: "))
        barOneColour = input("Pick a colour for the first bar: ")

        barTwoLabel = input("Enter a name for the second bar: ")
        barTwoHeight = int(input("Enter a value for the second bar: "))
        barTwoColour = input("Pick a colour for the second bar: ")

        barThreeLabel = input("Enter a name for the third bar: ")
        barThreeHeight = int(input("Enter a value for the third bar: "))
        barThreeColour = input("Pick a colour for the third bar: ")

        setFill(barOneColour)
        rect(X_ORIGIN + BAR_SPACING, Y_ORIGIN - barOneHeight, BAR_WIDTH, barOneHeight)

        setFill(barTwoColour)
        rect(X_ORIGIN + BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barTwoHeight, BAR_WIDTH, barTwoHeight)

        setFill(barThreeColour)
        rect(X_ORIGIN + 2 * BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barThreeHeight, BAR_WIDTH, barThreeHeight)

        setColor("black")
        setFont("Arial", "10", "bold")
        text(X_ORIGIN  + BAR_ONE_CENTER, Y_ORIGIN + LABEL_SPACING, barOneLabel)
        text(X_ORIGIN  + BAR_ONE_CENTER, Y_ORIGIN - barOneHeight + LABEL_SPACING, barOneHeight)
        text(X_ORIGIN  + BAR_TWO_CENTER, Y_ORIGIN + LABEL_SPACING, barTwoLabel)
        text(X_ORIGIN  + BAR_TWO_CENTER, Y_ORIGIN - barTwoHeight + LABEL_SPACING, barTwoHeight)
        text(X_ORIGIN  + BAR_THREE_CENTER, Y_ORIGIN + LABEL_SPACING, barThreeLabel)
        text(X_ORIGIN  + BAR_THREE_CENTER, Y_ORIGIN - barThreeHeight + LABEL_SPACING, barThreeHeight)
    elif barCount == 4:
        BAR_SPACING = 90
        BAR_ONE_CENTER = 130
        BAR_TWO_CENTER = 210
        BAR_THREE_CENTER = 290
        BAR_FOUR_CENTER = 370

        barOneLabel = input("Enter a name for the first bar: ")
        barOneHeight = int(input("Enter a value for the first bar: "))
        barOneColour = input("Pick a colour for the first bar: ")

        barTwoLabel = input("Enter a name for the second bar: ")
        barTwoHeight = int(input("Enter a value for the second bar: "))
        barTwoColour = input("Pick a colour for the second bar: ")

        barThreeLabel = input("Enter a name for the third bar: ")
        barThreeHeight = int(input("Enter a value for the third bar: "))
        barThreeColour = input("Pick a colour for the third bar: ")

        barFourLabel = input("Enter a name for the fourth bar: ")
        barFourHeight = int(input("Enter a value for the fourth bar: "))
        barFourColour = input("Pick a colour for the fourth bar: ")

        setFill(barOneColour)
        rect(X_ORIGIN + BAR_SPACING, Y_ORIGIN - barOneHeight, BAR_WIDTH, barOneHeight)

        setFill(barTwoColour)
        rect(X_ORIGIN + BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barTwoHeight, BAR_WIDTH, barTwoHeight)

        setFill(barThreeColour)
        rect(X_ORIGIN + 2 * BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barThreeHeight, BAR_WIDTH, barThreeHeight)

        setFill(barFourColour)
        rect(X_ORIGIN + 3 * BAR_WIDTH + BAR_SPACING, Y_ORIGIN - barFourHeight, BAR_WIDTH, barFourHeight)

        setColor("black")
        setFont("Arial", "10", "bold")
        text(X_ORIGIN  + BAR_ONE_CENTER, Y_ORIGIN + LABEL_SPACING, barOneLabel)
        text(X_ORIGIN  + BAR_ONE_CENTER, Y_ORIGIN - barOneHeight + LABEL_SPACING, barOneHeight)
        text(X_ORIGIN  + BAR_TWO_CENTER, Y_ORIGIN + LABEL_SPACING, barTwoLabel)
        text(X_ORIGIN  + BAR_TWO_CENTER, Y_ORIGIN - barTwoHeight + LABEL_SPACING, barTwoHeight)
        text(X_ORIGIN  + BAR_THREE_CENTER, Y_ORIGIN + LABEL_SPACING, barThreeLabel)
        text(X_ORIGIN  + BAR_THREE_CENTER, Y_ORIGIN - barThreeHeight + LABEL_SPACING, barThreeHeight)
        text(X_ORIGIN  + BAR_FOUR_CENTER, Y_ORIGIN + LABEL_SPACING, barFourLabel)
        text(X_ORIGIN  + BAR_FOUR_CENTER, Y_ORIGIN - barFourHeight + LABEL_SPACING, barFourHeight)
    elif barCount == 5:
        BAR_SPACING = 50
        BAR_ONE_CENTER = 90
        BAR_TWO_CENTER = 170
        BAR_THREE_CENTER = 250
        BAR_FOUR_CENTER = 330
        BAR_FIVE_CENTER = 410

        barOneLabel = input("Enter a name for the first bar: ")
        barOneHeight = int(input("Enter a value for the first bar: "))
        barOneColour = input("Pick a colour for the first bar: ")

        barTwoLabel = input("Enter a name for the second bar: ")
        barTwoHeight = int(input("Enter a value for the second bar: "))
        barTwoColour = input("Pick a colour for the second bar: ")

        barThreeLabel = input("Enter a name for the third bar: ")
        barThreeHeight = int(input("Enter a value for the third bar: "))
        barThreeColour = input("Pick a colour for the third bar: ")

        barFourLabel = input("Enter a name for the fourth bar: ")
        barFourHeight = int(input("Enter a value for the fourth bar: "))
        barFourColour = input("Pick a colour for the fourth bar: ")

        barFiveLabel = input("Enter a name for the fifth bar: ")
        barFiveHeight = int(input("Enter a value for the fifth bar: "))
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

        setColor("black")
        setFont("Arial", "10", "bold")
        text(X_ORIGIN  + BAR_ONE_CENTER, Y_ORIGIN + LABEL_SPACING, barOneLabel)
        text(X_ORIGIN  + BAR_ONE_CENTER, Y_ORIGIN - barOneHeight + LABEL_SPACING, barOneHeight)
        text(X_ORIGIN  + BAR_TWO_CENTER, Y_ORIGIN + LABEL_SPACING, barTwoLabel)
        text(X_ORIGIN  + BAR_TWO_CENTER, Y_ORIGIN - barTwoHeight + LABEL_SPACING, barTwoHeight)
        text(X_ORIGIN  + BAR_THREE_CENTER, Y_ORIGIN + LABEL_SPACING, barThreeLabel)
        text(X_ORIGIN  + BAR_THREE_CENTER, Y_ORIGIN - barThreeHeight + LABEL_SPACING, barThreeHeight)
        text(X_ORIGIN  + BAR_FOUR_CENTER, Y_ORIGIN + LABEL_SPACING, barFourLabel)
        text(X_ORIGIN  + BAR_FOUR_CENTER, Y_ORIGIN - barFourHeight + LABEL_SPACING, barFourHeight)
        text(X_ORIGIN  + BAR_FIVE_CENTER, Y_ORIGIN + LABEL_SPACING, barFiveLabel)
        text(X_ORIGIN  + BAR_FIVE_CENTER, Y_ORIGIN - barFiveHeight + LABEL_SPACING, barFiveHeight)
    elif barCount == 6:
        BAR_SPACING = 10
        BAR_ONE_CENTER = 50
        BAR_TWO_CENTER = 130
        BAR_THREE_CENTER = 210
        BAR_FOUR_CENTER = 290
        BAR_FIVE_CENTER = 370
        BAR_SIX_CENTER = 450

        barOneLabel = input("Enter a name for the first bar: ")
        barOneHeight = int(input("Enter a value for the first bar: "))
        barOneColour = input("Pick a colour for the first bar: ")

        barTwoLabel = input("Enter a name for the second bar: ")
        barTwoHeight = int(input("Enter a value for the second bar: "))
        barTwoColour = input("Pick a colour for the second bar: ")

        barThreeLabel = input("Enter a name for the third bar: ")
        barThreeHeight = int(input("Enter a value for the third bar: "))
        barThreeColour = input("Pick a colour for the third bar: ")

        barFourLabel = input("Enter a name for the fourth bar: ")
        barFourHeight = int(input("Enter a value for the fourth bar: "))
        barFourColour = input("Pick a colour for the fourth bar: ")

        barFiveLabel = input("Enter a name for the fifth bar: ")
        barFiveHeight = int(input("Enter a value for the fifth bar: "))
        barFiveColour = input("Pick a colour for the fifth bar: ")

        barSixLabel = input("Enter a name for the sixth bar: ")
        barSixHeight = int(input("Enter a value for the sixth bar: "))
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

        setColor("black")
        setFont("Arial", "10", "bold")
        text(X_ORIGIN  + BAR_ONE_CENTER, Y_ORIGIN + LABEL_SPACING, barOneLabel)
        text(X_ORIGIN  + BAR_ONE_CENTER, Y_ORIGIN - barOneHeight + LABEL_SPACING, barOneHeight)
        text(X_ORIGIN  + BAR_TWO_CENTER, Y_ORIGIN + LABEL_SPACING, barTwoLabel)
        text(X_ORIGIN  + BAR_TWO_CENTER, Y_ORIGIN - barTwoHeight + LABEL_SPACING, barTwoHeight)
        text(X_ORIGIN  + BAR_THREE_CENTER, Y_ORIGIN + LABEL_SPACING, barThreeLabel)
        text(X_ORIGIN  + BAR_THREE_CENTER, Y_ORIGIN - barThreeHeight + LABEL_SPACING, barThreeHeight)
        text(X_ORIGIN  + BAR_FOUR_CENTER, Y_ORIGIN + LABEL_SPACING, barFourLabel)
        text(X_ORIGIN  + BAR_FOUR_CENTER, Y_ORIGIN - barFourHeight + LABEL_SPACING, barFourHeight)
        text(X_ORIGIN  + BAR_FIVE_CENTER, Y_ORIGIN + LABEL_SPACING, barFiveLabel)
        text(X_ORIGIN  + BAR_FIVE_CENTER, Y_ORIGIN - barFiveHeight + LABEL_SPACING, barFiveHeight)
        text(X_ORIGIN  + BAR_SIX_CENTER, Y_ORIGIN + LABEL_SPACING, barSixLabel)
        text(X_ORIGIN  + BAR_SIX_CENTER, Y_ORIGIN - barSixHeight + LABEL_SPACING, barSixHeight)
    print("Your chart is completed") # To notify user the completion of their chart

# The process for making a pie chart starts here
elif graphType == 2:

    # Gathers user input for title
    pieChartName = input("Enter a title for the chart: ")
    # Sets title font, size and attributes
    setFont("Arial", "24", "bold")
    text(400, 50, pieChartName)

    # Establishes useful constants
    # Pie chart details
    DIAMETER = int(input("What would you like the diameter of the pie chart to be?: ")) # This asks the user for input on the diameter of the pie chart
    WIDTH = HEIGHT = DIAMETER  # This establishes how wide and how tall the pie chart should be, based off the diamater 
    TOTALANGLE = 360 # 360 degrees in a full pie chart rotation
    X_PIE_ORIGIN=200 # 200 pixels away from the left portion of the window, to relatively place the pie chart in the middle of the window
    Y_PIE_ORIGIN=100 # 200 pixels away from the top portion of the window, to relatively place the pie chart in the middle of the window
    
    # asks the user for input on the quanitity of slices for pie chart
    sliceCount = int(input("How many pie slices would you like the chart to have?: "))
    
    # Sets an if-elif loop for each specific number of slices you input
    if sliceCount == 2:

        # Asks for user input regarding the name, size and colour of the slice
        sliceOneName = input("What would you like to name the first pie slice?: ")
        sliceOneSize = int(input("From 0 to 359, how large would you like your first pie slice to be?: "))
        sliceOneColour = input("What would you like the colour of the first slice to be?: ")

        # Tells the user that the size of the slice remaining is already stablished
        print("The second slice size will be based off your first slice")
        sliceTwoName = input("What would you like to name the second pie slice?: ")
        sliceTwoColour = input("What would you like the colour of the second slice to be?: ")

        # Creates each slice based on the constants, and variables set, such as colour and size
        setFill(sliceOneColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, 0, sliceOneSize)

        setFill(sliceTwoColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, sliceOneSize, TOTALANGLE - sliceOneSize)

        # Creates a word legend with specific locations set to the left of the chart, specific font and size
        setFont("Arial", "18")
        text(60, 50, sliceOneName)
        text(60, 140, sliceTwoName)

        # Creates a colour legend to go along with the word legend, based on colour chosen for each slice
        setFill(sliceOneColour)
        rect(42, 75, 40, 40)

        setFill(sliceTwoColour)
        rect(42, 165, 40, 40)
        
        # Repeats process for each "elif" statement, adding depending on the additional slices
    elif sliceCount == 3:
        sliceOneName = input("What would you like to name the first pie slice?: ")
        sliceOneSize = int(input("From 0 to 358, how large would you like your first pie slice to be?: "))
        sliceOneColour = input("What would you like the colour of the first slice to be?: ")

        sliceTwoName = input("What would you like to name the second pie slice?: ")
        sliceTwoSize = int(input("From 0 to (359-size of the first slice), how large would you like your second pie slice to be ?: "))
        sliceTwoColour = input("What would you like the colour of the second slice to be?: ")

        print("The third slice size will be based off your other two slices")
        sliceThreeName = input("What would you like to name the third pie slice?: ")
        sliceThreeColour=input("what would you like the colour of the third slice to be?: ")

        setFill(sliceOneColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, 0, sliceOneSize)

        setFill(sliceTwoColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, sliceOneSize, sliceTwoSize)

        setFill(sliceThreeColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, sliceTwoSize + sliceOneSize, TOTALANGLE - sliceTwoSize - sliceOneSize)
        
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
        sliceTwoSize = int(input("From 0 to (358-size of the first slice), how large would you like your second pie slice to be?: "))
        sliceTwoColour = input("What would you like the colour of the second slice to be?: ")

        sliceThreeName = input("What would you like to name the third pie slice?: ")
        sliceThreeSize = int(input("From 0 to (359-size of the first and second slice), how large would you like your third pie slice to be?: "))
        sliceThreeColour = input("What would you like the colour of the third slice to be?: ")

        print("The fourth slice size will be based off your other three slices")
        sliceFourName = input("What would you like to name the fourth pie slice?: ")
        sliceFourColour = input("What would you like the colour of the fourth slice to be?: ")

        setFill(sliceOneColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, 0, sliceOneSize)

        setFill(sliceTwoColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, sliceOneSize, sliceTwoSize)

        setFill(sliceThreeColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, sliceTwoSize + sliceOneSize, sliceThreeSize)

        setFill(sliceFourColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, sliceThreeSize + sliceTwoSize + sliceOneSize, TOTALANGLE - sliceThreeSize - sliceTwoSize - sliceOneSize)

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
        sliceOneSize = int(input("From 0 to 356, how large would you like your first pie slice to be?: "))
        sliceOneColour = input("What would you like the colour of the first slice to be?: ")

        sliceTwoName = input("What would you like to name the second pie slice?: ")
        sliceTwoSize = int(input("From 0 to (357-size of the first slice), how large would you like your second pie slice to be?: "))
        sliceTwoColour = input("What would you like the colour of the second slice to be?: ")

        sliceThreeName = input("What would you like to name the third pie slice?: ")
        sliceThreeSize = int(input("From 0 to (358-size of the first and second slice), how large would you like your third pie slice to be?: "))
        sliceThreeColour = input("What would you like the colour of the third slice to be?: ")

        sliceFourName = input("What would you like to name the fourth pie slice?: ")
        sliceFourSize = int(input("From 0 to (359-size of the first, second and third slice), how large would you like your fourth pie slice to be?: "))
        sliceFourColour = input("What would you like the colour of the fourth slice to be?: ")

        print("The fifth slice size will be based off your other four slices")
        sliceFiveName = input("What would you like to name the fifth pie slice?: ")
        sliceFiveColour = input("What would you like the colour of the fifth slice to be?: ")

        setFill(sliceOneColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, 0, sliceOneSize)

        setFill(sliceTwoColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, sliceOneSize, sliceTwoSize)

        setFill(sliceThreeColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, sliceTwoSize + sliceOneSize, sliceThreeSize)

        setFill(sliceFourColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, sliceThreeSize + sliceTwoSize + sliceOneSize, sliceFourSize)

        setFill(sliceFiveColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, sliceFourSize + sliceThreeSize +sliceTwoSize + sliceOneSize, TOTALANGLE - sliceFourSize - sliceThreeSize - sliceTwoSize - sliceOneSize)

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
        sliceTwoSize = int(input("From 0 to (356-size of the first slice), how large would you like your second pie slice to be?: "))
        sliceTwoColour = input("What would you like the colour of the second slice to be?: ")

        sliceThreeName = input("What would you like to name the third pie slice?: ")
        sliceThreeSize = int(input("From 0 to (357-size of the first and second slice), how large would you like your third pie slice to be?: "))
        sliceThreeColour = input("What would you like the colour of the third slice to be?: ")

        sliceFourName = input("What would you like to name the fourth pie slice?: ")
        sliceFourSize = int(input("From 0 to (358-size of the first, second and third slice), how large would you like your fourth pie slice to be?: "))
        sliceFourColour = input("What would you like the colour of the fourth slice to be?: ")

        sliceFiveName = input("What would you like to name the fifth pie slice?: ")
        sliceFiveSize = int(input("From 0 to (359-size of the first, second, third and fourth slice), how large would you like your fifth pie slice to be?: "))
        sliceFiveColour = input("What would you like the colour of the fifth slice to be?: ")

        print("The sixth slice size will be based off your other five slices")
        sliceSixName = input("What would you like to name the sixth pie slice?: ")
        sliceSixColour = input("What would you like the colour of the sixth slice to be?: ")

        setFill(sliceOneColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, 0, sliceOneSize)

        setFill(sliceTwoColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, sliceOneSize, sliceTwoSize)

        setFill(sliceThreeColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, sliceTwoSize + sliceOneSize, sliceThreeSize)

        setFill(sliceFourColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, sliceThreeSize + sliceTwoSize + sliceOneSize, sliceFourSize)

        setFill(sliceFiveColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, sliceFourSize + sliceThreeSize + sliceTwoSize + sliceOneSize, sliceFiveSize)

        setFill(sliceSixColour)
        pieSlice(X_PIE_ORIGIN, Y_PIE_ORIGIN, WIDTH, HEIGHT, sliceFiveSize + sliceFourSize + sliceThreeSize + sliceTwoSize + sliceOneSize, TOTALANGLE - sliceFiveSize - sliceFourSize - sliceThreeSize - sliceTwoSize - sliceOneSize)

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
    print("Your chart is completed") # To notify user the completion of their chart
else:
    print("You have entered an invalid number. Please try again") # Just in case user actually DOES mis-input a number