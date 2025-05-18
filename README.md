# Playwright Cucumber Python Framework

This project is a test automation framework built using Playwright and Cucumber BDD with Python. It is designed to automate the login functionality and employee list retrieval for the OrangeHRM demo application.

## Project Structure

```
playwright-cucumber-python
├── features
│   ├── login.feature
│   ├── employee_list.feature
│   └── steps
│       ├── __init__.py
│       ├── login_steps.py
│       └── employee_steps.py
├── page_objects
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── pim_page.py
├── utils
│   ├── __init__.py
│   └── config.py
├── tests
│   └── __init__.py
├── environment.py
├── requirements.txt
└── README.md
```
# Playwright Cucumber Python Framework
...
## Features

- **Login Feature**: Automates the login process to the OrangeHRM application.
- **Employee List Feature**: Navigates to the PIM tab and retrieves the list of employees.

## Setup Instructions

1. **Clone the Repository**:
   ```
   git clone https://github.com/DAYASAGARDS/playwright-cucumber-python.git
   cd playwright-cucumber-python
   ```

2. **Install Dependencies**:
   
   Create virtual environment
   ```
   python -m venv venv
   ```
   Activate venv
   On Windows:
   ```
   venv\Scripts\activate
   ```
   On Mac/Linux:
   ```
   source venv/bin/activate
   ```
   Ensure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

4. **Run Tests**:
   You can run the tests using Behave:
   ```
   behave
   ```
   
   To generate Allure reports:
   ```
   behave -f allure_behave.formatter:AllureFormatter -o allure-results
   allure serve allure-results
   ```

## Usage Guidelines

- Modify the `utils/config.py` file to set your base URL and credentials.
- Add your feature scenarios in the `features` directory.
- Implement step definitions in the `features/steps` directory.
- Use the page object model in the `page_objects` directory to interact with the application.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.
