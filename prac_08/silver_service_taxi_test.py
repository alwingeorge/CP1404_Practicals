from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    new_taxi = SilverServiceTaxi("Test Silver Taxi", 100, 1)
    new_taxi.drive(20)
    print(new_taxi)
    print(new_taxi.get_fare())


main()
