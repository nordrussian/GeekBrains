class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        
    
    def go(self):
        print("GO")
    
    def stop(self):
        print("stop")

    def turn(self, direction):
        print(f"Car turned to {direction}")

    def show_speed(self):
        print(f'Speed is {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Speed limit violated')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Speed limit violated')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

town = TownCar(100, 'red', 'Town')
sport = SportCar(120, 'green', 'Sport')
work = WorkCar(41, 'yellow', 'Work')
police = PoliceCar(150, 'blue', 'Police')
        
town.show_speed()
work.show_speed()

work.speed = 30
work.show_speed()

police.turn('Left')
 
 
 