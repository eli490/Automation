from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace with actual login credentials
username = "elvin.opak"
password = "Sumova@24"

# Specify the path to the ChromeDriver executable
chrome_driver_path = "C:/Users/elvin.opak/SeleniumProject/Driver/chromedriver.exe"
service_obj = Service(chrome_driver_path)


# Function to log in to the web application
def login_to_application():
    # Initialize the Chrome WebDriver with the specified Service
    driver = webdriver.Chrome(service=service_obj)

    # Open the web application
    driver.get("https://qa.data.smartapplicationsgroup.com/connect/login")

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
            EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']"))
        )
        login_button.click()

        # Wait for the dropdown to be clickable
        dropdown_element = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='provider_key']"))
        )

        # Click the dropdown to reveal options
        dropdown_element.click()

        # Wait for the options list to become visible
        dropdown_options = WebDriverWait(driver, 40).until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, "//*[@id='provider_key_list_1']//div[contains(@class, 'ant-select-item-option')]")
            )
        )

        # Ensure that dropdown options are available
        if dropdown_options:
            # Select the desired option; adjust the index as needed
            option_to_select = dropdown_options[0]  # Example: select the first option
            option_to_select.click()

            # Wait a bit for the selection to register
            time.sleep(2)

            # Wait for the dropdown to close
            WebDriverWait(driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//*[@id='provider_key_list_1']"))
            )
        else:
            print("No dropdown options found.")

        # Scroll to the proceed button if necessary
        proceed_button = WebDriverWait(driver, 40).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@type='submit']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", proceed_button)

        # Wait for the proceed button to be clickable and then click it
        proceed_button = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']"))
        )
        proceed_button.click()

        # Wait for the OTP verification page to load
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Login OTP Verification')]"))
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
