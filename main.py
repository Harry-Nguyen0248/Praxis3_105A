import machine
import utime

numRows = 7
numCols = 5

rowPins = {
	machine.Pin(15, machine.Pin.Out),
	machine.Pin(14, machine.Pin.Out),
	machine.Pin(13, machine.Pin.Out),
	machine.Pin(12, machine.Pin.Out),
	machine.Pin(11, machine.Pin.Out),
	machine.Pin(10, machine.Pin.Out),
	machine.Pin(9, machine.Pin.Out)
}

colPins = {
	machine.Pin(16, machine.Pin.Out),
	machine.Pin(17, machine.Pin.Out),
	machine.Pin(18, machine.Pin.Out),
	machine.Pin(19, machine.Pin.Out),
	machine.Pin(20, machine.Pin.Out)
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