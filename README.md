# E-commerce Automation Testing Framework

This project is a Selenium + Python automation framework designed to test an e-commerce website.

## Features Automated
- User Registration
- Login
- Add to Cart
- Checkout & Address Verification
- Payment & Order Confirmation
- Logout

## Technologies Used
- Python
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- HTML Test Reports

## Project Structure
pages/  -> Page Objects  
tests/  -> Test cases  
requirements.txt -> Dependencies  

## How to Run
1. Install Python  
2. Install dependencies  
   pip install -r requirements.txt  

3. Run all tests  
   pytest  

4. Generate report  
   pytest --html=report.html  

## Business Flow Tested
Login → Add Product → Cart → Checkout → Payment → Order Success

This framework validates the complete e-commerce purchase journey.
