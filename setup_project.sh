#!/usr/bin/env bash

# Create database and create fake data

cat setup_mysql_db.sql | sudo mysql -uroot
USER=Name PWD=Password HOST=localhost DB=Healixra TYPE_STORAGE=db python3 create_fake_locations.py
USER=Name PWD=Password HOST=localhost DB=Healixra TYPE_STORAGE=db python3 create_fake_specializations.py
USER=Name PWD=Password HOST=localhost DB=Healixra TYPE_STORAGE=db python3 create_fake_doctors.py
