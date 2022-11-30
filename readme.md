# HC-SR04 Ultrasonic sensor

This driver for HC-SR04 Ultrasonic sensor is written in Python 3 programming language.

## Overview
HC-SR04 ultrasonic sensor can detect distances between 2cm to 400cm.
When powered the sensors trigger pin is set HIGH for 10 microseconds. While set HIGH the sensor transmits pattern of 8 pulses.

After transmitting pulses the trigger pin is set LOW and the echo pin is set HIGH until it receives the echo signal sent by trigger pin. The echo pin will be automatically set LOW after 38 ms if pulses are not reflected back.
