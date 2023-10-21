import drivers
from time import sleep

display = drivers.Lcd()

try:
     while True:
         print("test")
         display.lcd_display_string("Testing", 1)
         sleep(2)
         display.lcd_display_string("Testing again",1)
         sleep(2)
         display.lcd_clear()
         sleep(2)
except KeyboardInterrupt:
    print("testing done")
    display.lcd_clear()