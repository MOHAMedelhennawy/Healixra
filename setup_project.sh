#!/usr/bin/env bash

# Exit on any error
set -e

# Prompt user for input
echo "Please enter username and password:"
read -p "username: " username
read -sp "password: " password
echo ""

if [[ -n $username && -n $password ]]; then
    # Check if Python is installed
    if ! command -v python3 &> /dev/null; then
        echo "Python is not installed. Installing Python..."
        sudo apt update
        sudo apt install python3 -y
        sudo apt install python3-pip -y
    else
        echo "Python is already installed."
    fi

    # Install all required packages
    if command -v pip3 &> /dev/null; then
        echo "Installing required packages..."
        pip3 install -r requirements.txt
    else
        echo "pip is not installed. Installing pip..."
        sudo apt install python3-pip -y
        pip3 install -r requirements.txt
    fi

    # Create database and replace username and password in SQL script
    echo "Setting up the database..."
    if sed -e "s/{{username}}/$username/g" -e "s/{{password}}/$password/g" setup_mysql_db.sql | sudo mysql -uroot; then
        echo "Database setup complete!"
    else
        echo "Database setup failed." && exit 1
    fi

    # Create fake data
    echo "Creating fake data..."
    for script in create_fake_locations.py create_fake_specializations.py create_fake_doctors.py; do
        if ! USER=$username PWD=$password HOST=localhost DB=Healixra TYPE_STORAGE=db python3 "$script"; then
            echo "Failed to execute $script." && exit 1
        fi
    done

    # Start app
    if USER=$username PWD=$password HOST=localhost DB=Healixra TYPE_STORAGE=db python3 routes.py; then
        echo "App started successfully!"
    else
        echo "Failed to start the app." && exit 1
    fi
else
    echo "Username or password cannot be empty."
    exit 1
fi