import RPi.GPIO as GPIO
import time
import i2clcd

lcd = i2clcd.i2clcd(i2c_bus=1, i2c_addr=0x27, lcd_width=16)
lcd.init()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# setup PWM process
servo_pin = 23
GPIO.setup(servo_pin,GPIO.OUT)
pwm = GPIO.PWM(servo_pin,50) # 50 Hz (20 ms PWM period)
pwm.start(3)

input1 = 26
input2 = 19
 

GPIO.setup(input1 ,GPIO.IN ,pull_up_down=GPIO.PUD_UP) #input 1 pin number
GPIO.setup(input2 ,GPIO.IN ,pull_up_down=GPIO.PUD_UP) #input 2 pin number 

def print_on_lcd(msg):
    lcd.clear()
    lcd.print_line(msg,line=0)

while True:
    val1 = GPIO.input(input1) #reading input 1 val
    val2 = GPIO.input(input2) #reading input 1 val
    
    if(val1 == 0 and val2 == 1):
        print("how do you do")
        print_on_lcd("how do you do")
         
    elif(val1 == 1 and val2 == 0):
        print("where is bus stand")
        print_on_lcd("where is bus stand")
         
    elif(val1 == 0 and val2 == 0):
        print("had your food")
        print_on_lcd("had your food")
         
    else:
        lcd.clear()
        lcd.print_line("Make Gesture",line=0)
    
    print("input 1 value:",val1)
    print("input 2 value:",val2) 
    print("-------------------")
    time.sleep(1)

img.release()
