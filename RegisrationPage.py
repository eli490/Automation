from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Replace with actual registration details
first_name = ""
last_name = ""
username = ""
email = ""
password = ""
confirm_password = password  # Should match the password

# Specify the path to the ChromeDriver executable
chrome_driver_path = "C:/Users/elvin.opak/SeleniumProject/Driver/chromedriver.exe"
service_obj = Service(chrome_driver_path)


def register_user():
    # Initialize the Chrome WebDriver with the specified Service
    driver = webdriver.Chrome(service=service_obj)

    try:
        # Open the web application
        driver.get("https://example.com")

        # Maximize the browser window
        driver.maximize_window()

        # Wait for the register button on the login page to be clickable
        register_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Register']"))
        )
        register_button.click()

        # Wait for the registration page to load and the fields to be visible
        WebDriverWait(driver, 40).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//input[@type='text']"))
        )

        # Select each field using index-based XPath
        first_name_field = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
        last_name_field = driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
        username_field = driver.find_element(By.XPATH, "(//input[@type='text'])[3]")
        email_field = driver.find_element(By.XPATH, "(//input[@type='text'])[4]")
        password_field = driver.find_element(By.XPATH, "(//input[@type='password'])[1]")
        confirm_password_field = driver.find_element(By.XPATH, "(//input[@type='password'])[2]")

        # Fill in the registration form fields
        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        username_field.send_keys(username)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password_field.send_keys(confirm_password)

        # Wait for the register button to become active/clickable
        final_register_button = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Register']"))
        )

        # Click the register button to submit the form
        final_register_button.click()

        # Optional: wait for a success message or next page to ensure registration was successful
        WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Registration successful')]")  # Adjust text to match the success
                # message
            )
        )

        print("User registered successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Wait for a few seconds before closing to observe the result
        time.sleep(5)
        driver.quit()


# Call the function to register the user
if __name__ == "__main__":
    register_user()
