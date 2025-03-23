# OrangeHRM Demo Website Automation (Pytest + Selenium Grid)

This repository contains automated test scripts for the **OrangeHRM Demo Website**, leveraging the **Pytest** framework and **Selenium Grid** for distributed execution. The automation covers various website features, including login, employee management, and more.

## Features Implemented

- **Pytest Framework** – A simple and powerful testing framework for automation.
- **Selenium Grid Integration** – Enables parallel test execution across multiple environments and browsers.
- **Page Object Model (POM)** – Organizes test scripts in a structured way for better maintainability.
- **Logging** – Captures test execution details for debugging and analysis.
- **Reporting** – Generates test execution reports for easy tracking of test results.
- **Screenshot Generation** – Captures screenshots on test failures to help with debugging.

## Setup Instructions

### Clone the Repository
```sh
git clone https://github.com/automatealchemist/Orange_OpenSource_Live_Pytest_Selenium_Grid.git
cd Orange_OpenSource_Live_Pytest_Selenium_Grid
```

### Create and Activate Virtual Environment
```sh
python -m venv venv  # Create virtual environment
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Setting Up Selenium Grid

1. **Start Selenium Grid Hub**
   ```sh
   java -jar selenium-server-4.29.0.jar hub --host 0.0.0.0 --port 4444
   ```

2. **Start a Node and Register it with the Hub**
   ```sh
   java -jar selenium-server-4.29.0.jar node --hub http://172.18.208.1:4444
   ```

## Running the Tests

### Local Execution
```sh
pytest
```

### Running Tests on Selenium Grid
```sh
pytest --grid-url http://172.18.208.1:4444/wd/hub --browser chrome
```

### Running Tests in Parallel on Multiple Browsers
```sh
pytest -n 3 --html=reports/report.html
```

### Generating Reports
For detailed reporting with logs and screenshots, run:
```sh
pytest -v --html=reports/report.html
```

## Project Structure
```
|-- tests/                 # Contains test cases
|-- pageObjects/           # Page Object Model (POM) classes
|-- logs/                  # Stores log files
|-- reports/               # Stores test execution reports
|-- TestData/              # Contains test data for script execution
|-- conftest.py            # Pytest configuration file
|-- requirements.txt       # List of dependencies
|-- README.md              # Project documentation
```

## Notes
- Ensure **ChromeDriver** or the required WebDriver is installed and compatible with your browser.
- Selenium Grid must be running before executing tests in a distributed environment.

## Contributions
Feel free to fork this repository and contribute improvements by creating a pull request.


