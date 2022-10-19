import time
import board
import adafruit_dht
#Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D17)
while True:
    try:
         # Print the values to the serial port
         humidity = dhtDevice.humidity
# check for excess humidity
         print (" Humidity: {}%".format(humidity))
         if (humidity >80):
             print("Its Humid!")
         else:
             print("Its Dry")
    except RuntimeError as error:     # Errors happen fairly often, DHT's are hard to read, just keep going
         print(error.args[0])
    except KeyboardInterrupt:
         print('interrupted!')
         GPIO.cleanup()
    time.sleep(5.0)


