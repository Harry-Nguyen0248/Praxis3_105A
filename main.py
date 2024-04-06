import machine
import time
import find_coord


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
	row.value(1)
for col in colPins:
	col.value(1)
	
# button to show location
locButton = machine.Pin(8, machine.Pin.IN)

# button to save value
saveVal = machine.Pin(6, machine.Pin.IN)

# start and finish button
start = machine.Pin(5, machine.Pin.IN)
stop = machine.Pin(7, machine.Pin.IN)

# moisture sensor
moisture = machine.ADC(26)
goodSoil = False

storing = 0
dataSheetNum = 0

while True:
    location = get_coord() # FIGURE OUT WHERE THE COORDS ARE 3:
        
    if locButton.value() == 1:
        print("Currently located at: " + str(location))
            
        
    if start.value() == 1:
        print("Data recording started.")
        dataSheetNum += 1
        storing = 1
        file_name="sensorData{}.txt".format(dataSheetNum)
        file = open(file_name,"w")
        file.write("Starting coordinates: " + str(location) + "\n\n")

    while (storing == 1):
        moistureRead = moisture.read_u16() / 682
        print(moistureRead)
            
        if saveVal.value() == 1:
            print("Data point recorded.")
            if (47 <= moistureRead <= 62):
                goodSoil = True
                file.write(str(moistureRead) + "%, Soil is adequate. Coordinates from origin: \n")
            else:
                goodSoil = False
                file.write(str(moistureRead) + "%, Soil is poor. Coordinates from origin: \n")
            
        if stop.value() == 1:
            print("Data recording ended.")
            storing = 0
            file.close()
        time.sleep(1)
            
    time.sleep(1)
        


        
        


        
        



    
    
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