# PARENT CLASS - CAMERA
class Camera:
    def take_photo(self):
        print("Photo captured successfully.")

    def record_video(self):
        print("Video recording started.")




# PARENT CLASS - MUSIC PLAYER
class MusicPlayer:
    def play_music(self):
        print("Music is playing.")

    def stop_music(self):
        print("Music stopped.")




# PARENT CLASS - GPS
class GPS:
    def current_location(self):
        print("Current location: Palghar, Maharashtra, India.")

    def navigate(self):
        print("Navigation started.")




# CHILD CLASS - SMARTPHONE
# MULTIPLE INHERITANCE
class SmartPhone(Camera, MusicPlayer, GPS):
    def __init__(self, brand, model, price, storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage

    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price:,.2f}")
        print(f"Storage: {self.storage} GB")




# CREATE SMARTPHONE OBJECTS
phone1 = SmartPhone("Samsung", "Galaxy S25", 79999, "256 GB")
phone2 = SmartPhone("Apple", "iPhone 17", 99999, "256 GB")
phone3 = SmartPhone("OnePlus", "OnePlus 13", 69999, "512 GB")


print("\n" + "-" * 50)
# DISPLAY PHONE 1
print("Phone 1 Details:")
print("\n" + "-" * 50)
phone1.display_details()

# CAMERA FUNCTIONALITY
print("\nCamera Functionality:")
phone1.take_photo()
phone1.record_video()

# MUSIC PLAYER FUNCTIONALITY
print("\nMusic Player Functionality:")
phone1.play_music()
phone1.stop_music()

# GPS FUNCTIONALITY
print("\nGPS Functionality:")
phone1.current_location()
phone1.navigate()


print("\n" + "-" * 50)
# DISPLAY PHONE 2
print("\nPhone 2 Details:")
print("\n" + "-" * 50)
phone2.display_details()

# CAMERA FUNCTIONALITY
print("\nCamera Functionality:")
phone2.take_photo()
phone2.record_video()

# MUSIC PLAYER FUNCTIONALITY
print("\nMusic Player Functionality:")
phone2.play_music()
phone2.stop_music()

# GPS FUNCTIONALITY
print("\nGPS Functionality:")
phone2.current_location()
phone2.navigate()


# DEMONSTRATE ALL SMARTPHONES
smartphones = [phone1, phone2, phone3]
print("\n" + "-" * 50)
print("\nAll Smartphones:")
for phone in smartphones:
    print("\n" + "-" * 50)
    phone.display_details()