import os

app_name = os.getenv("APP_NAME", "Default Application")
environment = os.getenv("APP_ENV", "development")

print(f"Application: {app_name}")
print(f"Environment: {environment}")