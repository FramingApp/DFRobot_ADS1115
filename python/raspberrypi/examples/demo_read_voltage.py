"""!
  @file demo_read_voltage.py
  @brief connect ADS1115 I2C interface with your board (please reference board compatibility)
  @n  The voltage value read by A0 A1 A2 A3 is printed through the serial port.
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author [luoyufeng](yufeng.luo@dfrobot.com)
  @version  V1.0
  @date  2019-06-19
  @url https://github.com/DFRobot/DFRobot_ADS1115
"""

import sys
import os

sys.path.append("../")
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from DFRobot_ADS1115 import ADS1115

ADS1115_REG_CONFIG_PGA_6_144V = 0x00  # 6.144V range = Gain 2/3
ADS1115_REG_CONFIG_PGA_4_096V = 0x02  # 4.096V range = Gain 1
ADS1115_REG_CONFIG_PGA_2_048V = 0x04  # 2.048V range = Gain 2 (default)
ADS1115_REG_CONFIG_PGA_1_024V = 0x06  # 1.024V range = Gain 4
ADS1115_REG_CONFIG_PGA_0_512V = 0x08  # 0.512V range = Gain 8
ADS1115_REG_CONFIG_PGA_0_256V = 0x0A  # 0.256V range = Gain 16


ads1115 = ADS1115()

# with ADS1115() as ads1115:
for i in range(2000):
    # Set the IIC address
    ads1115.set_addr_ADS1115(0x48)
    # Sets the gain and input voltage range.
    ads1115.set_gain(ADS1115_REG_CONFIG_PGA_6_144V)
    # Get the Digital Value of Analog of selected channel
    adc0 = ads1115.read_voltage(1)
    time.sleep(0.001)
    # adc1 = ads1115.read_voltage(1)
    # time.sleep(0.2)
    # adc2 = ads1115.read_voltage(2)
    # time.sleep(0.2)
    # adc3 = ads1115.read_voltage(3)
    # print(f"A0:{adc0['r']}mV A1:{adc1['r']}mV A2:{adc2['r']}mV A3:{adc3['r']}mV")
    print(f"v: {adc0['r']} mV   Code: {adc0['c']}")