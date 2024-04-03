import machine
import utime

numRows = 7
numCols = 5

rowPins = {
	machine.Pin(15, machine.Pin.OUT),
	machine.Pin(14, machine.Pin.OUT),
	machine.Pin(13, machine.Pin.OUT),
	machine.Pin(12, machine.Pin.OUT),
	machine.Pin(11, machine.Pin.OUT),
	machine.Pin(10, machine.Pin.OUT),
	machine.Pin(9, machine.Pin.OUT)
}

colPins = {
	machine.Pin(16, machine.Pin.OUT),
	machine.Pin(17, machine.Pin.OUT),
	machine.Pin(18, machine.Pin.OUT),
	machine.Pin(19, machine.Pin.OUT),
	machine.Pin(20, machine.Pin.OUT)
}

for row in rowPins:
	row.value(0)
for col in colPins:
	col.value(0)
	
# button to show location
locButton = machine.Pin(7, machine.Pin.IN)

# button to save value
saveVal = machine.Pin(8, machine.Pin.IN)

# start and finish button
startStop = machine.Pin(22, machine.Pin.IN)

# moisture sensor
moisture = machine.ADC(26)
goodSoil = False

conversion = 3.3 / 65535

while True:
    moistureRead = moisture.read_u16() 
    print(moistureRead) # print to alphanumeric
    
    if saveVal.is_pressed():
        if (300 < moistureRead < 700):
            goodSoil = True
        else:
            goodSoil = False
    
