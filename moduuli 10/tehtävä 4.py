import random

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


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"{'Plate':<12}{'Max':<12}{'Speed':<12}{'Distance':<12}")
        for car in self.cars:
            print(f"{car.license_plate:<12}{car.maximum_speed:<12}{car.current_speed:<12}{car.travelled_distance:<12}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False
