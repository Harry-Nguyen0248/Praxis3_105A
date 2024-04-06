while True:
    dataSheetNum = input("Enter the selected data sheet number: ")
    
    file_name="sensorData{}.txt".format(dataSheetNum)
    file = open(file_name)
    print(file.read())
    file.close()