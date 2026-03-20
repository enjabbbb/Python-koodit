class Elevator:
    def __init__(self, bottom, top):
        self.bottom_floor = bottom
        self.top_floor = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(self.current_floor)

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(self.current_floor)

    def go_to_floor(self, target):
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()


class Building:
    def __init__(self, bottom, top, elevator_count):
        self.bottom_floor = bottom
        self.top_floor = top
        self.elevators = []

        for _ in range(elevator_count):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, index, target_floor):
        self.elevators[index].go_to_floor(target_floor)
