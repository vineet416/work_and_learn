class Vehicle:
    def __init__(self, vehicle_number, brand, driver_name, price_per_km):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.driver_name = driver_name
        self.price_per_km = price_per_km

    def calculate_fare(self, distance):
        return self.price_per_km * distance

    def display_info(self):
        print(f"Driver: {self.driver_name}")
        print(f"Vehicle: {self.brand}")
        print(f"Vehicle Number: {self.vehicle_number}")
        print(f"Price Per KM: ₹{self.price_per_km}")
    