# Healixra

**Healixra** is a web application designed to help users find doctors based on their specialization, location, and name. Users can register, log in, search for doctors, book appointments, and leave reviews. The application is built using Flask with MySQL as the database backend.

## Features

- **User Authentication**: Users can register and log in to access features like booking appointments and writing reviews.
- **Doctor Search**: Users can search for doctors by name, specialization, and location.
- **Appointments**: Book appointments with doctors and view upcoming bookings in the user profile.
- **Reviews**: Write and view reviews for doctors, with a rating system from 1 to 5.
- **User Profile**: Manage appointments and update profile information, including uploading profile pictures.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- MySQL Database
- Flask and related libraries (specified in `requirements.txt`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/MOHAMedelhennawy/Healixra.git
    cd Healixra
    ```

2. Create Virtual Environment
    ```bash
    python3 -m venv Healixra
    source Healixra/bin/activate
    ```

3. Install dependencies and set up the MySQL database:
    ```bash
    ./setup_project.sh
    ```

4. To run the application:
    ```bash
    python3 routes.py
    ```

## Usage

- **Home Page**: The home page allows users to search for doctors by filtering with their name, specialization, or location.
- **Doctor Profiles**: View individual doctor profiles, including available appointment slots and reviews.
- **Booking**: Authenticated users can book appointments with doctors and manage them from their profile.
- **Review System**: After a consultation, users can leave reviews with a rating of 1 to 5 stars.

### Example Commands

To run the app locally, use the following command:
```bash
USER=your_username PWD=your_password HOST=localhost DB=Healixra TYPE_STORAGE=db python3 routes.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.