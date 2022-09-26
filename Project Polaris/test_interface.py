from tkinter import*
import tkinter.font

## Hardware

## GUI Definitions
# Create a tkinter window object
window = Tk()				
window.title("Interface")	
textFont = tkinter.font.Font(family = 'Helvetica', size = 20, weight = "bold")
subTitleFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")
spacing = Label(window, text = '               ')
spacing1 = Label(window, text = '               ')
spacing2 = Label(window, text = '               ')

#--------------------------------------------------------------------------------#
### Event Functions
#--------------------------------------------------------------------------------#
def loadDesiredValues():
	desAlt.configure(text = altitudeEntry.get())
	desYaw.configure(text = yawEntry.get())
	desRoll.configure(text = rollEntry.get())

def startCommand():
	startButton["text"] = "STARTED"
	stopButton["text"] = "STOP"
	startButton["bg"] = "#D1D1D1"
	landButton["bg"] = "#3CE1FF"	
	stopButton["bg"] = "red"	
	landButton["state"] = "normal"
	stopButton["state"] = "normal"
		
	startButton["relief"] = "sunken"
	startButton["state"] = "disabled"
	

def landCommand():		
	if landButton["text"] == "LAND":
		landButton["text"] = "LANDING"
		landButton["bg"] = "#2AEC30"	
		landButton["relief"] = "sunken"
		landingStatus = 0
	
	elif currentZVel == 0:
		landButton["text"] = "LANDED"
		landButton["bg"] = "#D1D1D1"
		landButton["state"] = "disabled"
		landingStatus = 1;

def stopCommand():
	stopButton["text"] = "STOPPED"
	stopButton["bg"] = "#D1D1D1"
	stopButton["relief"] = "raised"
	stopButton["state"] = "disabled"

	startButton["state"] = "normal"
	startButton["bg"] = "#2AEC30"
	startButton["relief"] = "raised"
	startButton["text"] = "START"	

	landButton["bg"] = "#D1D1D1"
	landButton["state"] = "disabled"
	landButton["relief"] = "raised"
	landButton["text"] = "LAND"
	
def resetCommand():
	desAlt.configure(text = " ")
	desYaw.configure(text = " ")
	desRoll.configure(text = " ")
	altitudeEntry.delete(0, END)
	yawEntry.delete(0, END)
	rollEntry.delete(0, END)
	
# This function can be used to update the necessary sensor/instrument status
def updateStatus(updatedStatus):
	if updatedStatus == "comStatus":
		comStatus["text"] = "ACTIVE"
		comStatus["fg"] = "#2AEC30"
	elif updatedStatus == "cameraStatus":
		cameraStatus["text"] = "ACTIVE"
		cameraStatus["fg"] = "#2AEC30"
	elif updatedStatus == "anemometerStatus":
		anemometerStatus["text"] = "ACTIVE"
		anemometerStatus["fg"] = "#2AEC30"
	elif updatedStatus == "gpsStatus":
		gpsStatus["text"] = "ACTIVE"
		gpsStatus["fg"] = "#2AEC30"
	elif updatedStatus == "senseHatStatus":
		senseHatStatus["text"] = "ACTIVE"
		senseHatStatus["fg"] = "#2AEC30"
	elif updatedStatus == "dht11Status":
		dht11Status["text"] = "ACTIVE"
		dht11Status["fg"] = "#2AEC30"
	elif updatedStatus == "baroStatus":
		baroStatus["text"] = "ACTIVE"
		baroStatus["fg"] = "#2AEC30"
	

## Widgets
#--------------------------------------------------------------------------------#
### Sensor Reading Section
#--------------------------------------------------------------------------------#

# Create title for the sensor reading section
readingTitle = Label(window, text = 'Sensor Readings', font = textFont) 
readingTitle.grid(row = 0, column = 0)

# Create velocity sensor display readings in 3 directions
currentXVelLabel = Label(window, text = 'Current Velocity (X): ')
currentXVel = Label(window, text = '0')
currentXVelUnits = Label(window, text = ' m/s')
currentXVelLabel.grid(row = 1, column = 0, sticky=W)
currentXVel.grid(row = 1, column = 1, sticky=W)
currentXVelUnits.grid(row = 1, column = 2, sticky=W)

currentYVelLabel = Label(window, text = 'Current Velocity (Y): ')
currentYVel = Label(window, text = '0')
currentYVelUnits = Label(window, text = ' m/s')
currentYVelLabel.grid(row = 2, column = 0, sticky=W)
currentYVel.grid(row = 2, column = 1, sticky = W)
currentYVelUnits.grid(row = 2, column = 2, sticky=W)


currentZVelLabel = Label(window, text = 'Current Velocity (Z): ')
currentZVel = Label(window, text = '0')
currentZVelUnits = Label(window, text = ' m/s')
currentZVelLabel.grid(row = 3, column = 0, sticky=W)
currentZVel.grid(row = 3, column = 1, sticky=W)
currentZVelUnits.grid(row = 3, column = 2, sticky=W)


# The code below creates the section where the user can read from the current altitude, yaw and roll sensor readings respectively.
currentAltLabel = Label(window, text = 'Current Altitude (z): ')
currentAlt = Label(window, text = '0')
currentAltUnits = Label(window, text = ' m')
currentAltLabel.grid(row = 6, column = 0, sticky=W)
currentAlt.grid(row = 6, column = 1, sticky=W)
currentAltUnits.grid(row = 6, column = 2, sticky=W)

currentYawLabel = Label(window, text = 'Current Rotation Z (yaw): ')
currentYaw = Label(window, text = '0')
currentYawUnits = Label(window, text = ' deg/rad')
currentYawLabel.grid(row = 7, column = 0, sticky=W)
currentYaw.grid(row = 7, column = 1, sticky=W)
currentYawUnits.grid(row = 7, column = 2, sticky=W)


currentRollLabel = Label(window, text = 'Current Rotation X (roll): ')
currentRoll = Label(window, text = '0')
currentRollUnits = Label(window, text = ' deg/rad')
currentRollLabel.grid(row = 8, column = 0, sticky=W)
currentRoll.grid(row = 8, column = 1, sticky=W)
currentRollUnits.grid(row = 8, column = 2, sticky=W)

# Create button to reset the sensor reading values to zero i.e calibrate. 
spacing.grid(row = 9, column = 0)
calibrationButton = Button(window, text = 'CALIBRATE')
calibrationButton.grid(row = 10, column = 0, sticky = E)
#--------------------------------------------------------------------------------#
### Commands Section
#--------------------------------------------------------------------------------#
#--------------------------------------------#
### Input Desired Values Section
#--------------------------------------------#
spacing1.grid(row = 0, column = 3)
# Create title for the commands section
commandTitle = Label(window, text = 'Commands', font = textFont) 
commandTitle.grid(row = 0, column = 4, sticky = W)
# Create title for the sensor reading section
commandTitle = Label(window, text = 'Input Desired Values', font = subTitleFont) 
commandTitle.grid(row = 1, column = 4)


# The code below creates the section where the user can enter the desired altitude, yaw and raw respectively. 
altitudeLabel = Label(window, text = 'Altitude (z): ')
altitudeLabel.grid(row = 2, column = 4, sticky=W)
altitudeEntry = Entry(window, bd = 5)
altitudeEntry.grid(row = 2, column = 5, sticky=W)
altitudeUnits = Label(window, text = ' m')
altitudeUnits.grid(row = 2, column = 6, sticky=W)

yawLabel = Label(window, text = 'Rotation Z (yaw): ')
yawLabel.grid(row = 3, column = 4, sticky=W)
yawEntry = Entry(window, bd = 5)
yawEntry.grid(row = 3, column = 5, sticky=W)
yawUnits = Label(window, text = ' deg/rad')
yawUnits.grid(row = 3, column = 6, sticky=W)

rollLabel = Label(window, text = 'Rotation X (roll): ')
rollLabel.grid(row = 4, column = 4, sticky=W)
rollEntry = Entry(window, bd = 5)
rollEntry.grid(row = 4, column = 5, sticky=W)
rollUnits = Label(window, text = ' deg/rad')
rollUnits.grid(row = 4, column = 6, sticky=W)

# Create button to confirm the desired values entered by user
loadCommands = Button(window, text = 'LOAD', command = loadDesiredValues)
loadCommands.grid(row = 5, column = 5)

#--------------------------------------------#
### Desired Values
#--------------------------------------------#
# Present the desired altitude, yaw and roll
desAltLabel = Label(window, text = 'Desired Altitude (z): ')
desAlt = Label(window, text = '')
desAltUnits = Label(window, text = ' m')
desAltLabel.grid(row = 6, column = 4, sticky=W)
desAlt.grid(row = 6, column = 5, sticky=W)
desAltUnits.grid(row = 6, column = 6, sticky=W)

desYawLabel = Label(window, text = 'Desired Rotation Z (yaw): ')
desYaw = Label(window, text = '')
desYawUnits = Label(window, text = ' deg/rad')
desYawLabel.grid(row = 7, column = 4, sticky=W)
desYaw.grid(row = 7, column = 5, sticky=W)
desYawUnits.grid(row = 7, column = 6, sticky=W)

desRollLabel = Label(window, text = 'Desired Rotation X (roll): ')
desRoll = Label(window, text = '')
desRollUnits = Label(window, text = ' deg/rad')
desRollLabel.grid(row = 8, column = 4, sticky=W)
desRoll.grid(row = 8, column = 5, sticky=W)
desRollUnits.grid(row = 8, column = 6, sticky=W)

#--------------------------------------------#
### Operational Section
#--------------------------------------------#
spacing.grid(row = 0, column = 7)
# Create title for the sensor reading section
operationTitle = Label(window, text = 'Operational Commands', font = subTitleFont) 
operationTitle.grid(row = 1, column = 8)

# Create buttons for operational section
startButton = Button(window, text = 'START', width = 10, bg = "#2AEC30", command = startCommand)
startButton.grid(row = 2, column = 8)
landButton = Button(window, text = 'LAND', width = 10, bg = "#D1D1D1", state = "disabled", command = landCommand)
landButton.grid(row = 3, column = 8)
stopButton = Button(window, text = 'STOP', width = 10, bg = "#D1D1D1", state = "disabled",command = stopCommand)
stopButton.grid(row = 4, column = 8)
resetButton = Button(window, text = 'RESET', width = 10, bg = "red", command = resetCommand)
resetButton.grid(row = 5, column = 8)

#--------------------------------------------------------------------------------#
### Status Section
#--------------------------------------------------------------------------------#
spacing2.grid(row = 0, column = 9)

# Create title for status sections
statusTitle = Label(window, text = "Status", font = textFont)
statusTitle.grid(row = 0, column = 10, sticky = W)

comStatusLabel = Label(window, text = "Communication Status: ")
comStatusLabel.grid(row = 1, column = 10, sticky = W)
cameraStatusLabel = Label(window, text = "Camera Status: ")
cameraStatusLabel.grid(row = 2, column = 10, sticky = W)
anemometerStatusLabel = Label(window, text = "Anemometer Status: ")
anemometerStatusLabel.grid(row = 3, column = 10, sticky = W)
gpsStatusLabel = Label(window, text = "GPS Status: ")
gpsStatusLabel.grid(row = 4, column = 10, sticky = W)
senseHatStatusLabel = Label(window, text = "Sense HAT Status: ")
senseHatStatusLabel.grid(row = 5, column = 10, sticky = W)
dht11StatusLabel = Label(window, text = "Temperature & Humidity Status: ")
dht11StatusLabel.grid(row = 6, column = 10, sticky = W)
baroStatusLabel = Label(window, text = "Barometer Status: ")
baroStatusLabel.grid(row = 7, column = 10, sticky = W)

comStatus = Label(window, text = "Inactive", fg = "red")
comStatus.grid(row = 1, column = 11, sticky = W)
cameraStatus = Label(window, text = "Inactive", fg = "red")
cameraStatus.grid(row = 2, column = 11, sticky = W)
anemometerStatus = Label(window, text = "Inactive", fg = "red")
anemometerStatus.grid(row = 3, column = 11, sticky = W)
gpsStatus = Label(window, text = "Inactive", fg = "red")
gpsStatus.grid(row = 4, column = 11, sticky = W)
senseHatStatus = Label(window, text = "Inactive", fg = "red")
senseHatStatus.grid(row = 5, column = 11, sticky = W)
dht11Status = Label(window, text = "Inactive", fg = "red")
dht11Status.grid(row = 6, column = 11, sticky = W)
baroStatus = Label(window, text = "Inactive", fg = "red")
baroStatus.grid(row = 7, column = 11, sticky = W)


mainloop()