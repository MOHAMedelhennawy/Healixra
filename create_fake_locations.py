import models
from models.location import Location
"""
Cairo
Alexandria
Giza
Qalyubia
Port Said
Suez
Dakahlia
Sharqia
Kafr El Sheikh
Gharbia
Monufia
Beheira
Ismailia
Beni Suef
Fayoum
Minya
Asyut
Sohag
Qena
Aswan
Luxor
Red Sea
New Valley
Matrouh
North Sinai
South Sinai

command:
HBNB_MYSQL_USER=Name HBNB_MYSQL_PWD=Password HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=Healixra HBNB_TYPE_STORAGE=db python3 create_fake_locations.py  

"""
name = ' '
while name != '':
    name = input()
    if name is not None:
        location = Location(location_name=name)
        location.save()

models.storage.save()
print('Ok')