# 9DoF_IMU
Interfaced Arduino with Adafruit BNO055 9DoF IMU and Raspberry Pi to create a mobile IMU sensor that records rotations in roll, pitch and yaw. Project was for work to be used as part of a larger project.

## How to set-up/use the IMU Build ##

Materials: <br />

--> Arduino UNO <br />

--> Adafruit BNO055 9DoF IMU <br />

--> Male to male jumper wires <br />

--> Printer cord (USB-A to USB-B) <br />

--> Raspberry Pi 3 or 4 (I have the raspberry pi 3) <br />

--> USB-C cable (if Pi 4) <br />

--> Mini-USB (if Pi 3) <br />

--> 5V output, preferably battery pack (mobile) <br />

--> Monitor, Keyboard, Mouse optional. <br />

## Set-Up ##

Arduino to BNO055 pin-out: (the IMU has already been soldered to the breadboard)<br />

Arduino UNO --> BNO055<br />

GND --> GND<br />

5V --> Vin<br />

A5 --> SCL <br />

A4 --> SDA <br />

1. Connect the Raspberry Pi to the Arduino UNO using the USB to USB-A cable <br />

2. Plug the Raspberry Pi to a voltage source with the mini-USB cord. Optimal output voltage for the pi is 5V <br />

3. a. If you have a monitor, you could test the pi by plugging the hdmi cable into the port on the Raspberry Pi and trying to run Arduino IDE (should be installed on the Pi) <br />

3. b. For mobile connectivity, and if you do not have a separate display, keyboard and mouse, you can run the Pi using VNC Viewer and remote desktop the Pi. <br />

4. Download this repository and send files via bluetooth to arduino from host computer. <br />

5. To collect the data output from the Arduino, run the python script arduinotocsv.py either from terminal with the command ‘python3 /home/pi/Downloads/arduinotocsv.py' in the Pi’s terminal, or open the file in Thonny Python IDE (for Rasperry Pi) <br />

  5. a. As of now, the python script is having challenges running each time on the raspberry pi, it seems to work sometimes not all the time, while the exact same script always works on the Laptop, so I’m looking into reasons why the python script is not working on the Raspberry Pi. <br />

6. The main purpose of the python script is to automate recording the serial output from the arduino to a csv. It also allows for keyboard interruption to stop the script from running at a specific time. <br />

## Send Files ## 
1. Once there is a file of values (either a text file or csv), use the send files over Bluetooth feature to transfer the file from the raspberry pi (on VNC Viewer) to the host computer. Could do this by logging into Google Drive via Chromium and uploading the file there. Alternatively send the file via Bluetooth to the host computer. First connect your computer to the raspberry pi in Bluetooth settings/Bluetooth manager.  Then right click on the device and click ‘Send Files to Device’, while also opening the Bluetooth settings on the host computer and enabling receive files. <br /> 

2. This is what the host computer’s Bluetooth settings should look like. ![image](https://user-images.githubusercontent.com/111996917/209395997-bb47eaea-6335-4519-9b7e-17dbdfb8f434.png)
<br />

3. The most efficient/fastest way to send files is through the VNC server’s file transfer system. Right click the VNC viewer icon on the Raspberry Pi VNC viewer. Then select File Transfer and select the steps to select your file and it’s destination on the local computer. ![image](https://user-images.githubusercontent.com/111996917/209396050-a51a3bcf-8b9c-458a-816d-13ee47700edd.png)
<br />

If you get stuck along the way, follow these steps:  https://youtu.be/JZveSiTlq1U <br />
