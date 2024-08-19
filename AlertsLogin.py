from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Replace with actual login credentials
username = "elvin.opak@smartapplicationsgroup.com"
password = "Sumova@26"

# Specify the path to the ChromeDriver executable
chrome_driver_path = "C:/Users/elvin.opak/SeleniumProject/Driver/chromedriver.exe"
service_obj = Service(chrome_driver_path)


def login_to_application():
    # Initialize the Chrome WebDriver with the specified Service
    driver = webdriver.Chrome(service=service_obj)

    try:
        # Open the web application
        driver.get("https://qa.data.smartapplicationsgroup.com:30489/login")

        # Maximize the browser window
        driver.maximize_window()

        # Wait for the username field to be present and visible
        username_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='text']"))
        )
        password_field = driver.find_element(By.XPATH, "//input[@type='password']")

        # Enter credentials
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Wait for the login button to be clickable and then click it
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))
        )
        login_button.click()

        # Wait for the hamburger button to be visible and clickable
        hamburger_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='button']"))
            # Update with actual XPath
        )
        hamburger_button.click()

        # Print success message for navigation pane
        print("Hamburger button clicked, navigation pane displayed.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Wait for a few seconds before closing to observe the result
        time.sleep(5)
        driver.quit()


# Call the function to log in
if __name__ == "__main__":
    login_to_application()
