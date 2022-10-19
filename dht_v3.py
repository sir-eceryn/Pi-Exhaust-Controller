import time
import board
import adafruit_dht
import os
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

#Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D17)

#initialise LCD Pins
lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D19)
lcd_d7 = digitalio.DigitalInOut(board.D27)
lcd_d6 = digitalio.DigitalInOut(board.D22)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_backlight = digitalio.DigitalInOut(board.D4)

lcd_columns = 16
lcd_rows = 2

lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight
)

lcd.backlight = True

while True:
    try:
         # Print the values to the serial port
         humidity = dhtDevice.humidity
# check for excess humidity
         print (" Humidity: {}%".format(humidity))
         lcd.message = " \nHumidity : {}%".format(humidity)
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
    time.sleep(10.0)


