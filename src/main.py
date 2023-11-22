from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
from hal import hal_led as hal_led
import led_control as led

#Empty list to store sequence of keypad presses
password = []

lcd = LCD.lcd()
lcd.lcd_clear()
hal_led.init()
#Call back function invoked when any key on keypad is pressed

def key_pressed(key):
    password.append(key)
    global delay
    print(password)
    if key == 1:
        led.led_control_init()
        lcd.lcd_clear()
        lcd.lcd_display_string("LED Control", 1)
        lcd.lcd_display_string("Blink LED", 2)
    if key == 0:
        lcd.lcd_clear()
        lcd.lcd_display_string("LED Control", 1)
        lcd.lcd_display_string("OFF LED", 2)
        while key != 1:
            hal_led.set_output(0,0)
            password.append(key)

def main():
    # Initialize LCD
    lcd = LCD.lcd()
    lcd.lcd_clear()

    # Display something on LCD
    lcd.lcd_display_string("LED Control", 1)
    lcd.lcd_display_string("0:Off 1:Blink", 2)

    # Initialize the HAL keypad driver
    keypad.init(key_pressed)

    # Start the keypad scanning which will run forever in an infinite while(True) loop in a new Thread "keypad_thread"
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()


# Main entry point
if __name__ == "__main__":
    main()
