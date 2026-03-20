class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, license_plate, maximum_speed, battery_capacity):
        super().__init__(license_plate, maximum_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, license_plate, maximum_speed, tank_volume):
        super().__init__(license_plate, maximum_speed)
        self.tank_volume = tank_volume

e = ElectricCar("ELEC-1", 180, 75.0)
g = GasolineCar("GAS-1", 160, 50.0)

e.accelerate(200)
g.accelerate(74)

e.drive(2)
g.drive(3)

print(e.travelled_distance, g.travelled_distance)
