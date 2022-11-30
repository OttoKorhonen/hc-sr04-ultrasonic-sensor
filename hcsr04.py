import RPi.GPIO as GPIO
from time import sleep, time_ns


class Hcsr04:

    '''
     This is a driver for HC-SR04 ultrasonic sensor written in Python 3 programming language.
     This driver was tested and run on Raspberry Pi 3 model b+ and it works well.
     The measurements have a deviation of a few centimeters, so the results are indicative.
    '''

    def __init__(self, trigger_pin: int, echo_pin: int):
        self.time = None
        self.echo_time = 0
        self.echo_pin = echo_pin
        self.trigger_pin = trigger_pin
        self.echo_speed = 343  # speed of sound in air is 343m/s


    def setup(self):
        '''
        This function is for pin setup and needs to be called before other functions.
        '''
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)


    def calclulate_distance(self):
        '''
        This function calculates the distance to the object.
        self.echo_speed is divided by 10000 to get cm/microsecond.
        Value returned by pulse_time is divided by 1000 to get time in microseconds.
        '''
        pulse_time = self.trigger_on_and_wait()
        print(f'{(self.echo_speed/10000) * (pulse_time/1000)/2:.2f} cm')
        return f'{(self.echo_speed/10000) * (pulse_time/1000)/2:.2f}'


    def time_pulse(self):
        '''
        Function checks if echo pin is on and while it is on counts time in nanoseconds.
        If echo pin is off the function calls itself.
        '''
        if GPIO.input(self.echo_pin) == 1:
            self.time = time_ns()
            while GPIO.input(self.echo_pin) == 1:
                pass

            self.echo_time = time_ns() - self.time

        else:
            self.time_pulse()

        return self.echo_time


    def trigger_on_and_wait(self):
        '''
        This function sets trigger pin on and off and then calls for the function that
        counts the pulse length and returns the time in nanoseconds.
        '''
        GPIO.output(self.trigger_pin, 0)
        sleep(0.000005)  # 5 microseconds
        GPIO.output(self.trigger_pin, 1)
        sleep(0.00001)  # 10 microseconds
        GPIO.output(self.trigger_pin, 0)

        pulse_time = self.time_pulse()
        return pulse_time


