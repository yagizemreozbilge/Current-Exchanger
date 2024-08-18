### README

# Currency Converter Application

## Overview

This project is a simple currency converter web application built with Flask. The application includes a basic frontend for user interaction and a backend that simulates currency conversion.

## Setup Instructions

### On Windows

1. **Install Python and Pip**

   Ensure Python and pip are installed on your Windows system. You can download Python from the [official website](https://www.python.org/downloads/).

2. **Install Flask**

   Open Command Prompt or PowerShell and install Flask and coverage with the following commands:

   ```bash
   pip install flask coverage
   ```

3. **Run the Application**

   Navigate to the project directory and start the Flask application:

   ```bash
   cd C:\Users\yagiz\Desktop\My works\Current Exchanger
   python app.py
   ```

   The application will be accessible at `http://127.0.0.1:5000/`.

4. **Run Tests and Coverage**

   Run the tests and generate a coverage report:

   ```bash
   coverage run -m unittest discover
   coverage report
   coverage html
   ```

   View the HTML coverage report by opening `htmlcov/index.html` in your browser.

### On Linux (WSL)

1. **Install Python and Pip**

   Ensure Python and pip are installed. If not, install them using:

   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **Install Flask and Coverage**

   Use pip to install Flask and coverage:

   ```bash
   pip3 install flask coverage
   ```

3. **Run the Application**

   Navigate to the project directory and start the Flask application:

   ```bash
   cd /mnt/c/Users/yagiz/Desktop/My\ works/Current\ Exchanger
   python3 app.py
   ```

   The application will be accessible at `http://127.0.0.1:5000/`.

4. **Run Tests and Coverage**

   Run the tests and generate a coverage report:

   ```bash
   coverage run -m unittest discover
   coverage report
   coverage html
   ```

   View the HTML coverage report by opening `htmlcov/index.html` in your browser.

## Project Structure

- **app.py**: The main application file containing the Flask app, routes, and the simulated currency conversion logic.
- **test_app.py**: Contains unit tests for the application.
- **templates/index.html**: HTML template used for rendering the frontend (included in `app.py` as a string).

## Notes

- Ensure that you have the necessary permissions and environment settings to run the application and tests.
- If you encounter issues with missing modules, double-check the installation of dependencies.

Feel free to reach out if you have any questions or issues.
