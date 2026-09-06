from vehicles.car import Car
from vehicles.bike import Bike


car1 = Car("MH12AB1234", "Hyundai", "Rahul", 20)
car2 = Car("MH12CD5678", "Maruti", "Amit",18)
bike1 = Bike("MH12EF1111", "Honda", "Ravi", 12)
bike2 = Bike("MH12GH2222", "TVS", "Vijay", 10)


def main():
    vehicle_type = input("Enter vehicle type (car/bike): ").strip().lower()
    distance = float(input("Enter travel distance (in KM): "))

    if vehicle_type == "car":
        print("\nAvailable Cars:")
        car1.display_info()
        print()
        car2.display_info()
        print()

        selected_car = input("Select a car (1 or 2): ").strip()
        if selected_car == "1":
            fare = car1.calculate_fare(distance)
            print(f"\nTotal Fare: ₹{fare}")
        elif selected_car == "2":
            fare = car2.calculate_fare(distance)
            print(f"\nTotal Fare: ₹{fare}")
        else:
            print("Invalid selection.")

    elif vehicle_type == "bike":
        print("\nAvailable Bikes:")
        bike1.display_info()
        print()
        bike2.display_info()
        print()

        selected_bike = input("Select a bike (1 or 2): ").strip()
        if selected_bike == "1":
            fare = bike1.calculate_fare(distance)
            print(f"\nTotal Fare: ₹{fare}")
        elif selected_bike == "2":
            fare = bike2.calculate_fare(distance)
            print(f"\nTotal Fare: ₹{fare}")
        else:
            print("Invalid selection.")
    else:
        print("Invalid vehicle type.")


if __name__ == "__main__":
    main()