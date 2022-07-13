import RPi.GPIO as GPIO
import time

pwm_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin,50)

pwm.start(0)
pwm.ChangeDutyCycle(0)
while True:
    print('please enter')
    t = float(input())
    pwm.ChangeDutyCycle(t)
    time.sleep(0.1)
    if t == 0:
        break
pwm.stop()
GPIO.cleanup()
