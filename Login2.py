from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with actual login credentials
username = ""  # Replace with actual username
password = ""  # Replace with actual password

# Specify the path to the ChromeDriver executable
chrome_driver_path = "C:/Users/elvin.opak/SeleniumProject/Driver/chromedriver.exe"
service_obj = Service(chrome_driver_path)


# Function to log in to the web application
def login_to_application():
    # Initialize the Chrome WebDriver with the specified Service
    driver = webdriver.Chrome(service=service_obj)

    # Open the web application
    driver.get(
        "https://example.com")  # Replace with the actual URL of the login page

    # Maximize the browser window
    driver.maximize_window()

    try:
        # Wait for the username field to be present and visible
        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='username']"))
        )

        # Locate the username and password fields using XPath and enter the credentials
        username_field = driver.find_element(By.XPATH, "//*[@id='username']")
        password_field = driver.find_element(By.XPATH, "//*[@id='password']")

        username_field.send_keys(username)
        password_field.send_keys(password)

        # Wait for the login button to be clickable and then click it
        login_button = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']"))  # Replace with the correct XPath
        )
        login_button.click()

        # Wait for the dropdown to be clickable
        dropdown_element = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='provider_key']"))
            # Replace with the actual XPath of the dropdown
        )

        # Click the dropdown to reveal options
        dropdown_element.click()

        # Wait for the options list to become visible
        options_list = WebDriverWait(driver, 40).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='provider_key_list']"))
            # Replace with the XPath that correctly identifies the dropdown options list

        )
        options_list.click()

        # Click on the specific dropdown option
        dropdown_option = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='provider_key_list_0']"))  # Replace with the
            # correct XPath for the dropdown option
        )
        dropdown_option.click()

        # Wait for the proceed button to be clickable and then click it
        proceed_button = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']"))
            # Replace with the correct XPath of the proceed button
        )
        proceed_button.click()

        # Wait for the OTP verification page to load
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Login OTP Verification')]"))
            # Replace with the correct XPath or other identifier on the OTP page
        )

        # Print success message
        print("OTP verification page loaded successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()


# Call the function to log in
login_to_application()
