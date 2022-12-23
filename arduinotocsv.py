import serial
import pandas as pd
from datetime import datetime

arduino_port = "COM6"
baud = 115200
fileName = "arduino_data.csv"
print_labels = False


# ser = serial.Serial(arduino_port, baud)
# print("Connected to Arduino port:" + arduino_port)
sensor_data = pd.DataFrame(columns =['yaw','pitch','roll','timestamp'])
current_time = datetime.now()

with serial.Serial(arduino_port, baud) as ser:
    while True:
        try:
            getData = ser.readline()
            dataString = getData.decode('utf-8')
            print(dataString)
            data = dataString[0:][:-2]
            print(data)

            readings = data.split(",")
            now = datetime.now()
            now_time = now - current_time
            readings.append(now_time)
            sensor_data.loc[len(sensor_data)] = readings
        except:
            print("Keyboard Interrupt")
            break
            # 'datetime.timedelta' object has no attribute 'strftime'sensor_data.loc[len(sensor_data.index)] = readings
sensor_data.to_csv(fileName, index=False)