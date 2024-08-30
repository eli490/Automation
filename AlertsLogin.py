from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import traceback

# Replace with actual login credentials
username = ""
password = ""
max_alert_amount = ""
max_claim_alert_amount = ""
email_to_add = ""  # Replace with the actual email

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
                (By.XPATH, "//*[contains(text(), 'Welcome to the Alerts Portal, Please proceed to the different "
                           "pages')]")
            )
        )

        # Wait for the hamburger button to be visible and clickable using its class
        hamburger_button = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@type='button' and contains(@class, 'mud-button-root "
                                                  "mud-icon-button mud-inherit-text hover:mud-inherit-hover "
                                                  "mud-ripple mud-ripple-icon mud-icon-button-edge-start')]"))
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
                break

        # Handle the autocomplete input field by focusing on the parent div first
        for attempt in range(3):  # Retry up to 3 times
            try:
                # Locate the parent div for the autocomplete field
                parent_div = WebDriverWait(driver, 50).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//div[contains(@class, 'mud-input mud-input-outlined mud-input-adorned-end "
                                   "mud-select-input')]")
                    )
                )

                # Then locate the specific input within that div
                autocomplete_input = parent_div.find_element(By.XPATH, "//input[@type='text']")
                autocomplete_input.send_keys("SAMPLE SCHEME")

                # Wait for the autocomplete suggestions to appear
                suggestions = WebDriverWait(driver, 50).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'mud-list-item-text')]"))
                )

                # Print out all available suggestions
                for suggestion in suggestions:
                    print("Suggestion:", suggestion.text)

                # Select the desired suggestion
                for suggestion in suggestions:
                    if "SAMPLE SCHEME" in suggestion.text:  # Replace with the desired suggestion
                        suggestion.click()
                        break

                break  # Break the loop if no exception occurs

            except StaleElementReferenceException as e:
                print(f"Retrying due to stale element reference: {e}")
                time.sleep(0)  # Wait a bit before retrying

        # After selecting the customer, locate the Maximum Alert Amount field
        try:
            print("Attempting to locate the Maximum Alert Amount field...")

            # Locate the input field for Maximum Alert Amount by indexing it directly
            max_alert_amount_field = WebDriverWait(driver, 50).until(
                EC.visibility_of_element_located((By.XPATH, "(//input[@class='mud-input-slot mud-input-root "
                                                            "mud-input-root-outlined' and @type='text'])[1]"))
            )

            # Scroll to the element to make sure it's in view
            driver.execute_script("arguments[0].scrollIntoView(true);", max_alert_amount_field)
            time.sleep(2)  # Give some time for the scrolling

            # Ensure the element is clickable before interaction
            max_alert_amount_field = WebDriverWait(driver, 50).until(
                EC.element_to_be_clickable((By.XPATH, "(//input[@class='mud-input-slot mud-input-root "
                                                      "mud-input-root-outlined' and @type='text'])[1]"))
            )

            # Clear the field before entering the amount
            max_alert_amount_field.clear()
            max_alert_amount_field.send_keys(max_alert_amount)
            print("Successfully entered the Maximum Alert Amount.")

            # Locate the input field for Maximum Claim Amount by indexing it directly
            max_claim_alert_field = WebDriverWait(driver, 50).until(
                EC.visibility_of_element_located((By.XPATH, "(//input[@class='mud-input-slot mud-input-root "
                                                            "mud-input-root-outlined' and @type='text'])[2]"))
            )

            # Scroll to the element to make sure it's in view
            driver.execute_script("arguments[0].scrollIntoView(true);", max_claim_alert_field)
            time.sleep(2)  # Give some time for the scrolling

            # Ensure the element is clickable before interaction
            max_claim_alert_field = WebDriverWait(driver, 50).until(
                EC.element_to_be_clickable((By.XPATH, "(//input[@class='mud-input-slot mud-input-root "
                                                      "mud-input-root-outlined' and @type='text'])[2]"))
            )

            # Clear the field before entering the amount
            max_claim_alert_field.clear()
            max_claim_alert_field.send_keys(max_claim_alert_amount)
            print("Successfully entered the Maximum Claim Amount.")

            # Locate the Enter Email field
            email_field = WebDriverWait(driver, 50).until(
                EC.visibility_of_element_located((By.XPATH, "(//input[@class='mud-input-slot mud-input-root "
                                                            "mud-input-root-outlined' and @type='text'])[3]"))
            )
            email_field.clear()
            email_field.send_keys(email_to_add)

            # Locate and click the Add button
            add_button = WebDriverWait(driver, 50).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add Email']"))
            )
            add_button.click()
            print("Successfully added the email.")

            # Wait for 2 seconds before submitting the form
            time.sleep(2)

            # Locate and click the Submit button
            submit_button = WebDriverWait(driver, 50).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit Form']"))
            )
            submit_button.click()
            print("Successfully clicked the Submit button.")

        except (TimeoutException, ElementNotInteractableException):
            print("Failed to locate or interact with the Maximum Alert Amount, Maximum Claim Amount, Enter Email "
                  "fields, or Add button. Please check the XPath or element visibility.")
            traceback.print_exc()

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

    finally:
        # Wait for a few seconds before closing to observe the result
        time.sleep(2)
        driver.quit()


# Call the function to log in
if __name__ == "__main__":
    login_to_application()
