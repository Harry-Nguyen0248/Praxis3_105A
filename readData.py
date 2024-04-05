dataSheetNum = input("Enter the selected data sheet number: ")
print(dataSheetNum)

file = open("sensorData{dataSheetNum}.text")
print(file.read())
file.close()