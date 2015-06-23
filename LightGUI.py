# This project requires PyBluez
from Tkinter import *
import bluetooth

#Look for all Bluetooth devices
#the computer knows about.
print "Searching for devices..."
print ""
#Create an array with all the MAC
#addresses of the detected devices
nearby_devices = bluetooth.discover_devices()
#Run through all the devices found and list their name
num = 0
print "Select your device by entering its coresponding number..."
for i in nearby_devices:
	num+=1
	print num , ": " , bluetooth.lookup_name( i )

#Allow the user to select their Arduino
#bluetooth module. They must have paired
#it before hand.
selection = input("> ") - 1
print "You have selected", bluetooth.lookup_name(nearby_devices[selection])
bd_addr = nearby_devices[selection]

port = 1

#Create the GUI
class Application(Frame):

#Create a connection to the socket for Bluetooth
#communication
    sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

    def disconnect(self):
    	#Close socket connection to device
        self.sock.close()
        
    def on(self):
    	#Send 'H' which the Arduino
    	#detects as turning the light on
        data = "H"
        self.sock.send(data)

    def off(self):
    	#Send 'L' to turn off the light
    	#attached to the Arduino
        data = "L"
        self.sock.send(data)

    def createWidgets(self):
    	#Form all the buttons.
    	#Look at a Tkinter reference
    	#for explanations.
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.disconnectFrom = Button(self)
        self.disconnectFrom["text"] = "Disconnect"
        self.disconnectFrom["fg"]   = "darkgrey"
        self.disconnectFrom["command"] =  self.disconnect

        self.disconnectFrom.pack({"side": "left"})

        self.turnOn = Button(self)
        self.turnOn["text"] = "On",
        self.turnOn["fg"] = "green"
        self.turnOn["command"] = self.on

        self.turnOn.pack({"side": "left"})

        self.turnOff = Button(self)
        self.turnOff["text"] = "Off"
        self.turnOff["fg"] = "red"
        self.turnOff["command"] = self.off

        self.turnOff.pack({"side": "left"})

    def __init__(self, master=None):
    	#Connect to the bluetooth device
    	#and initialize the GUI
        self.sock.connect((bd_addr, port))
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

#Begin the GUI processing
root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
