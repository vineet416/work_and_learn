import os

app_name = os.getenv("APP_NAME", "Default Application")
environment = os.getenv("APP_ENV", "development")
database_password = os.getenv("DB_PASSWORD", "")

print(f"Application: {app_name}")
print(f"Environment: {environment}")
print(f"Database password configured: {bool(database_password)}")