import RPi.GPIO as GPIO
import time

class BitBangI2C:
    def __init__(self, SCL, SDA):
        self.SCL = SCL
        self.SDA = SDA
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.SCL, GPIO.OUT)
        GPIO.setup(self.SDA, GPIO.OUT)

    def start(self):
        GPIO.output(self.SDA, True)
        time.sleep(0.001)  # Some delay to stabilize
        GPIO.output(self.SCL, True)
        time.sleep(0.001)
        GPIO.output(self.SDA, False)
        time.sleep(0.001)
        GPIO.output(self.SCL, False)

    def stop(self):
        GPIO.output(self.SDA, False)
        time.sleep(0.001)
        GPIO.output(self.SCL, True)
        time.sleep(0.001)
        GPIO.output(self.SDA, True)
        time.sleep(0.001)

    # def write_byte(self, byte):
    #     for i in range(8):
    #         GPIO.output(self.SCL, False)
    #         bit = (byte >> (7 - i)) & 0x01
    #         GPIO.output(self.SDA, bit)
    #         time.sleep(0.001)
    #         GPIO.output(self.SCL, True)
    #         time.sleep(0.001)
    #         GPIO.output(self.SCL, False)
    #     # Acknowledge bit
    #     GPIO.setup(self.SDA, GPIO.IN)
    #     GPIO.output(self.SCL, True)
    #     ack = GPIO.input(self.SDA)
    #     GPIO.output(self.SCL, False)
    #     GPIO.setup(self.SDA, GPIO.OUT)
    #     return not ack

    # def read_byte(self, ack=True):
    #     byte = 0x00
    #     GPIO.setup(self.SDA, GPIO.IN)
    #     for i in range(8):
    #         GPIO.output(self.SCL, True)
    #         time.sleep(0.001)
    #         bit = GPIO.input(self.SDA)
    #         byte = (byte << 1) | bit
    #         GPIO.output(self.SCL, False)
    #         time.sleep(0.001)
    #     GPIO.setup(self.SDA, GPIO.OUT)
    #     GPIO.output(self.SDA, not ack)
    #     GPIO.output(self.SCL, True)
    #     time.sleep(0.001)
    #     GPIO.output(self.SCL, False)
    #     GPIO.output(self.SDA, True)
    #     return byte

    def cleanup(self):
        GPIO.cleanup()
