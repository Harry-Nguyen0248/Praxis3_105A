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

# button to read data file
readData = machine.Pin(23, machine.Pin.IN)

# moisture sensor
moisture = machine.ADC(26)
goodSoil = False

conversion = 3.3 / 65535

storing = 0

while True:
    if startStop.value() == True:
        if storing == 0:
            storing += 1
            file = open("sensors.txt","w")
    
    while storing == 1:
        moistureRead = moisture.read_u16() 
        print(moistureRead) 
        
        if saveVal.value() == True:
            if (300 < moistureRead < 700):
                goodSoil = True
                file.write(str(moistureRead) + ", Soil is adequate. \n")
            else:
                goodSoil = False
                file.write(str(moistureRead) + ", Soil is poor. \n")
        
        if startStop.value() == True:
            storing -= 1
            file.close()
            
    if readData.value() == True:
        file = open("sensors.text")
        print(file.read())
        file.close()
  
    
    
    
'''
import machine
import time

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
calibration_data = {
    # Replace these values with your calibration data
    "dry": 1200,    # Analog voltage reading for dry soil
    "moist": 2000,  # Analog voltage reading for moist soil
    "wet": 2600     # Analog voltage reading for wet soil
}

# Function to convert analog voltage to moisture level
def voltage_to_moisture(voltage):
    # Use linear interpolation based on calibration data
    min_voltage = min(calibration_data.values())
    max_voltage = max(calibration_data.values())
    min_moisture = 0
    max_moisture = 100  # Assuming moisture levels range from 0 to 100
    return min_moisture + (voltage - min_voltage) * (max_moisture - min_moisture) / (max_voltage - min_voltage)

while True:
    moisture_read = moisture.read_u16()
    moisture_level = voltage_to_moisture(moisture_read)
    print("Moisture Level:", moisture_level)
    time.sleep(1)

'''