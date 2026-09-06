from .vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, vehicle_number, brand, driver_name, price_per_km):
        super().__init__(vehicle_number, brand, driver_name, price_per_km)

    def display_info(self):
        print("Vehicle Type: Bike")
        super().display_info()
