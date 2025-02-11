# Sauce Demo Automation

This project contains automated tests for the Sauce Demo website using Selenium with Python, implementing the Page Object Model (POM) pattern and Behavior-Driven Development (BDD) with Behave.

## Project Structure

```
sauce_demo_automation/
├── features/
│   ├── steps/
│   │   └── sauce_demo_steps.py
│   ├── environment.py
│   └── sauce_demo.feature
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── requirements.txt
└── README.md
```

## Test Scenarios

The automation covers the following test scenarios:

1. **Add item to cart** (@tc-1)
   - Login with standard user
   - Add Sauce Labs Backpack to cart
   - Verify item count in cart
   - Verify item details in cart

2. **Navigate to About page** (@tc-2)
   - Login with standard user
   - Open hamburger menu
   - Click About link
   - Verify redirection to Sauce Labs website

## Prerequisites

- Python 3.7 or higher
- Chrome browser installed

## Setup Instructions

1. Clone this repository
2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Tests

To run all tests:
```bash
behave
```

To run with more detailed output:
```bash
behave -v
```

To run with HTML reports:
```bash
behave --format behave_html_formatter:HTMLFormatter -o reports/report.html
```

### Running Tests with Different Speeds

You can control the execution speed by adding a delay between steps:

```bash
# Run tests with 1 second delay between steps
behave -D DELAY=1

# Run tests with 2 seconds delay between steps
behave -D DELAY=2

# Run tests with 0.5 second delay between steps
behave -D DELAY=0.5

# Run specific test with delay
behave --tags=tc-1 -D DELAY=1
```

### Running Specific Test Cases

You can run specific test cases using tags:

```bash
# Run only the Add to Cart test
behave --tags=tc-1

# Run only the About Page Navigation test
behave --tags=tc-2

# Run multiple specific tags
behave --tags=tc-1,tc-2
```

## Project Components

- **features/**: Contains BDD feature files and step definitions
  - `sauce_demo.feature`: Test scenarios in Gherkin syntax
  - `steps/sauce_demo_steps.py`: Step implementations
  - `environment.py`: Test setup and teardown hooks

- **pages/**: Page Object Model implementation
  - `base_page.py`: Common web element interactions
  - `login_page.py`: Login page elements and actions
  - `inventory_page.py`: Product list page elements and actions
  - `cart_page.py`: Shopping cart page elements and actions

## Reports

Test reports are generated in HTML format and saved in the `reports/` directory. Open `reports/report.html` in a web browser to view the test results.
