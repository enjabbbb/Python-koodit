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
