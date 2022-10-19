import time
import board
import adafruit_dht
import os
#Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D17)
while True:
    try:
         # Print the values to the serial port
         humidity = dhtDevice.humidity
# check for excess humidity
         print (" Humidity: {}%".format(humidity))
         if (humidity >60):
             print("Its Humid!")
             os.system("kasa --type plug --host '192.168.1.53' on")
         else:
             print("Its Dry")
             os.system("kasa --type plug --host '192.168.1.53' off")
    except RuntimeError as error:     # Errors happen fairly often, DHT's are hard to read, just keep going
         print(error.args[0])
    except KeyboardInterrupt:
         print('interrupted!')
         GPIO.cleanup()
    time.sleep(60.0)
