# import wiringpi

# # _pi = pigpio.pi()
# # if not _pi.connected:
# #     raise IOError("Can't connect to pigpio")

# # # Motor speeds for this library are specified as numbers between -MAX_SPEED and
# # # MAX_SPEED, inclusive.
# # # This has a value of 480 for historical reasons/to maintain compatibility with
# # # older libraries for other Pololu boards (which used WiringPi to set up the
# # # hardware PWM directly).
# _max_speed = 480
# MAX_SPEED = _max_speed

# _pin_M1DIAG = 5
# _pin_M2DIAG = 6
# _pin_M1PWM = 12
# _pin_M2PWM = 13
# _pin_M1EN = 22
# _pin_M2EN = 23
# _pin_M1DIR = 24
# _pin_M2DIR = 25

# io_initialized = False
# def io_init():
#   global io_initialized
#   if io_initialized:
#     return

#   wiringpi.wiringPiSetupGpio()
#   wiringpi.pinMode(12, wiringpi.GPIO.PWM_OUTPUT)
#   wiringpi.pinMode(13, wiringpi.GPIO.PWM_OUTPUT)

#   wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
#   wiringpi.pwmSetRange(MAX_SPEED)
#   wiringpi.pwmSetClock(2)

#   wiringpi.pinMode(5, wiringpi.GPIO.OUTPUT)
#   wiringpi.pinMode(6, wiringpi.GPIO.OUTPUT)

#   io_initialized = True

# class Motor(object):
#     MAX_SPEED = _max_speed

#     def __init__(self, pwm_pin, dir_pin, en_pin, diag_pin):
#         io_init()
#         self.pwm_pin = pwm_pin
#         self.dir_pin = dir_pin
#         self.en_pin = en_pin
#         self.diag_pin = diag_pin
#         wiringpi.pullUpDnControl(diag_pin, wiringpi.PUD_UP)
#         # _pi.set_pull_up_down(diag_pin, pigpio.PUD_UP) # make sure DIAG is pulled up
#         wiringpi.digitalWrite(en_pin, 1)
#         # _pi.write(en_pin, 1) # enable driver by default

#     def setSpeed(self, speed):
#         if speed < 0:
#             speed = -speed
#             dir_value = 1
#         else:
#             dir_value = 0

#         if speed > MAX_SPEED:
#             speed = MAX_SPEED

#         io_init()
#         wiringpi.digitalWrite(self.dir_pin, dir_value)
#         wiringpi.pwmWrite(self.pwm_pin, int(speed))
#         # _pi.write(self.dir_pin, dir_value)
#         # _pi.hardware_PWM(self.pwm_pin, 20000, int(speed * 6250 / 3));
#           # 20 kHz PWM, duty cycle in range 0-1000000 as expected by pigpio

#     def enable(self):
#         wiringpi.digitalWrite(self.en_pin, 1)
#         # _pi.write(self.en_pin, 1)

#     def disable(self):
#         wiringpi.digitalWrite(self.en_pin, 0)
#         # _pi.write(self.en_pin, 0)

#     def getFault(self):
#         # return not _pi.read(self.diag_pin)
#         return not wiringpi.digitalRead(self.diag_pin)

# class Motors(object):
#     MAX_SPEED = _max_speed

#     def __init__(self):
#         self.motor1 = Motor(_pin_M1PWM, _pin_M1DIR, _pin_M1EN, _pin_M1DIAG)
#         self.motor2 = Motor(_pin_M2PWM, _pin_M2DIR, _pin_M2EN, _pin_M2DIAG)

#     def setSpeeds(self, m1_speed, m2_speed):
#         self.motor1.setSpeed(m1_speed)
#         self.motor2.setSpeed(m2_speed)

#     def enable(self):
#         self.motor1.enable()
#         self.motor2.enable()

#     def disable(self):
#         self.motor1.disable()
#         self.motor2.disable()

#     def getFaults(self):
#         return self.motor1.getFault() or self.motor2.getFault()

#     def forceStop(self):
#         # reinitialize the pigpio interface in case we interrupted another command
#         # (so this method works reliably when called from an exception handler)
#         # global _pi
#         # _pi.stop()
#         # _pi = pigpio.pi()
#         io_init()
#         self.setSpeeds(0, 0)

# motors = Motors()

import pigpio

_pi = pigpio.pi()
if not _pi.connected:
    raise IOError("Can't connect to pigpio")

# Motor speeds for this library are specified as numbers between -MAX_SPEED and
# MAX_SPEED, inclusive.
# This has a value of 480 for historical reasons/to maintain compatibility with
# older libraries for other Pololu boards (which used WiringPi to set up the
# hardware PWM directly).
_max_speed = 480
MAX_SPEED = _max_speed

_pin_M1DIAG = 5
_pin_M2DIAG = 6
_pin_M1PWM = 12
_pin_M2PWM = 13
_pin_M1EN = 22
_pin_M2EN = 23
_pin_M1DIR = 24
_pin_M2DIR = 25

class Motor(object):
    MAX_SPEED = _max_speed

    def __init__(self, pwm_pin, dir_pin, en_pin, diag_pin):
        self.pwm_pin = pwm_pin
        self.dir_pin = dir_pin
        self.en_pin = en_pin
        self.diag_pin = diag_pin

        _pi.set_pull_up_down(diag_pin, pigpio.PUD_UP) # make sure DIAG is pulled up
        _pi.write(en_pin, 1) # enable driver by default

    def setSpeed(self, speed):
        if speed < 0:
            speed = -speed
            dir_value = 1
        else:
            dir_value = 0

        if speed > MAX_SPEED:
            speed = MAX_SPEED

        _pi.write(self.dir_pin, dir_value)
        _pi.hardware_PWM(self.pwm_pin, 20000, int(speed * 6250 / 3));
          # 20 kHz PWM, duty cycle in range 0-1000000 as expected by pigpio

    def enable(self):
        _pi.write(self.en_pin, 1)

    def disable(self):
        _pi.write(self.en_pin, 0)

    def getFault(self):
        return not _pi.read(self.diag_pin)

class Motors(object):
    MAX_SPEED = _max_speed

    def __init__(self):
        self.motor1 = Motor(_pin_M1PWM, _pin_M1DIR, _pin_M1EN, _pin_M1DIAG)
        self.motor2 = Motor(_pin_M2PWM, _pin_M2DIR, _pin_M2EN, _pin_M2DIAG)

    def setSpeeds(self, m1_speed, m2_speed):
        self.motor1.setSpeed(m1_speed)
        self.motor2.setSpeed(m2_speed)

    def enable(self):
        self.motor1.enable()
        self.motor2.enable()

    def disable(self):
        self.motor1.disable()
        self.motor2.disable()

    def getFaults(self):
        return self.motor1.getFault() or self.motor2.getFault()

    def forceStop(self):
        # reinitialize the pigpio interface in case we interrupted another command
        # (so this method works reliably when called from an exception handler)
        global _pi
        _pi.stop()
        _pi = pigpio.pi()
        self.setSpeeds(0, 0)

motors = Motors()
