from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's Drive")
    print(MENU)
    user_input = input(">>>").lower()
    while user_input != "q":
        if user_input == "c":
            print("Taxis available")
        elif user_input == "d":
            print("Drive")
        else:
            print("Invalid option")
        print(MENU)
        user_input = input(">>> ").lower()


main()
