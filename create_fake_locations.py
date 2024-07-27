import models
from models.location import Location
"""
Create fake locations

command:
USER=Name PWD=Password HOST=localhost DB=Healixra TYPE_STORAGE=db python3 create_fake_locations.py  

"""


egyptian_governorates = [
    "Cairo",
    "Alexandria",
    "Giza",
    "Qalyubia",
    "Port Said",
    "Suez",
    "Dakahlia",
    "Sharqia",
    "Kafr El Sheikh",
    "Gharbia",
    "Monufia",
    "Beheira",
    "Ismailia",
    "Beni Suef",
    "Fayoum",
    "Minya",
    "Asyut",
    "Sohag",
    "Qena",
    "Aswan",
    "Luxor",
    "Red Sea",
    "New Valley",
    "Matrouh",
    "North Sinai",
    "South Sinai"
]

for location in egyptian_governorates:
    location = Location(location_name=location)
    location.save()

models.storage.save()
print('Fake locations created successfully!')