from prac_08.unreliable_car import UnreliableCar


def main():
    """Test some UnreliableCars."""
    # Different Cars
    good_car = UnreliableCar("Not Bad Boss", 100, 89)
    bad_car = UnreliableCar("Git Gud", 100, 9)
    # Testing who can get to x distance first
    for i in range(1, 30):  # Range of KM
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))
    # print the final stats of the cars
    print(good_car)
    print(bad_car)


main()
