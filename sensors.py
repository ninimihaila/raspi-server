import gpiozero
from time import sleep

import db

conn = db.connect('sensors.sql')


class Sensor:
    def __init__(self, *args):
        self._sensor = self._sensor_type(*args)
        self._value = self._sensor_value
    
    def log(self):
        db.log_value(conn, self.name, self.value)

    @property
    def name(self):
        return self._name
    
    @property
    def value(self):
        return self._value(self._sensor)
    

class Pir(Sensor):
    _sensor_type = gpiozero.MotionSensor
    _name = 'ir'
    _sensor_value = lambda self, x: x.motion_detected


pir = Pir(17)

sensors = [pir]

while True:
    for sensor in sensors:
        #sensor.log()
        print(sensor.value)
    
    sleep(1)