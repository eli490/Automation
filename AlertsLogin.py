from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Replace with actual login credentials
username = ""
password = ""

# Specify the path to the ChromeDriver executable
chrome_driver_path = "C:/Users/elvin.opak/SeleniumProject/Driver/chromedriver.exe"
service_obj = Service(chrome_driver_path)


def login_to_application():
    # Initialize the Chrome WebDriver with the specified Service
    driver = webdriver.Chrome(service=service_obj)

    try:
        # Open the web application
        driver.get("")

        # Maximize the browser window
        driver.maximize_window()

        # Wait for the username field to be present and visible
        username_field = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='text']"))
        )
        password_field = driver.find_element(By.XPATH, "//input[@type='password']")

        # Enter credentials
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Wait for the login button to be clickable and then click it
        login_button = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))
        )
        login_button.click()

        # Wait for the welcome message to appear
        WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located(
                (By.XPATH,
                 "//*[contains(text(), 'Welcome to the Alerts Portal, Please proceed to the different pages')]")
            )
        )

        # Wait for the hamburger button to be visible and clickable using its class
        hamburger_button = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//*[@type='button' and contains(@class, 'mud-button-root mud-icon-button "
                                        "mud-inherit-text hover:mud-inherit-hover mud-ripple mud-ripple-icon "
                                        "mud-icon-button-edge-start')]"))
        )
        hamburger_button.click()

        # Wait for the navigation pane to be visible after clicking the hamburger button
        WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "mud-drawer"))
        )

        # Select the "Customer Alert Settings" menu item
        customer_alert_settings = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Claim Alerts')]"))
        )
        customer_alert_settings.click()

        # Select the "Create New" button
        create_new_button = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create New']"))
        )
        create_new_button.click()

        # Selecting the dropdown that contains a list of countries
        dropdown_option = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@type='text' and contains(@class, 'mud-input-slot')]"))
        )
        dropdown_option.click()

        # Wait for the countries' list to be visible
        WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "mud-list"))
        )

        # Get all dropdown options
        options = WebDriverWait(driver, 50).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'mud-list-item')]"))
        )

        # Print out all available options in the dropdown
        for option in options:
            print("Dropdown option:", option.text)

        # Use explicit wait before interacting with each option to avoid stale element issues
        for option in options:
            WebDriverWait(driver, 10).until(EC.visibility_of(option))
            if option.text == "KENYA":  # Replace "KENYA" with the desired option
                option.click()
                print(f"Selected country: {option.text}")
                break

        # Handling the autocomplete input field by focusing on the parent div first
        for attempt in range(3):  # Retry up to 3 times
            try:
                # Locate the parent div
                parent_div = WebDriverWait(driver, 50).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//div[contains(@class, 'mud-input mud-select-input')]"))
                )

                # Then locate the specific input within that div
                autocomplete_input = parent_div.find_element(By.XPATH, ".//input[@type='text']")
                autocomplete_input.send_keys("TEST CUSTOMER 13")

                # Wait for the autocomplete suggestions to appear
                suggestions = WebDriverWait(driver, 50).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'mud-list-item-text')]"))
                )

                # Print out all available suggestions
                for suggestion in suggestions:
                    print("Suggestion:", suggestion.text)

                # Select the desired suggestion
                for suggestion in suggestions:
                    if "TEST CUSTOMER 13" in suggestion.text:  # Replace with the desired suggestion
                        suggestion.click()
                        print(f"Selected customer: {suggestion.text}")
                        break

                break  # Break the loop if no exception occurs

            except Exception as e:
                print(f"Retrying due to stale element reference: {e}")
                time.sleep(2)  # Wait a bit before retrying

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Wait for a few seconds before closing to observe the result
        time.sleep(60)
        driver.quit()


# Call the function to log in
if __name__ == "__main__":
    login_to_application()
