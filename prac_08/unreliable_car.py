from random import randint
from prac_08.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            # if the rng is bad, the car goes nowhere.
            distance = 0
        distance_drove = super().drive(distance)
        return distance_drove
