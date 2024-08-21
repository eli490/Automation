from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Replace with actual login credentials
username = ""
password = ""

# Specify the path to the ChromeDriver executable
chrome_driver_path = "C:/Users/elvin.opak/SeleniumProject/Driver/chromedriver.exe"
service_obj = Service(chrome_driver_path)


# Function to log in to the web application
def login_to_application():
    # Initialize the Chrome WebDriver with the specified Service
    driver = webdriver.Chrome(service=service_obj)

    # Open the web application
    driver.get("")

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
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'ant-select-item-option-content')]"))
        )

        # Print out all available options in the dropdown
        for option in dropdown_options:
            print("Dropdown option:", option.text)

        # Select the specific option using ActionChains (example selecting the first one)
        actions = ActionChains(driver)
        actions.move_to_element(dropdown_options[0]).click().perform()

        # Print the selected value
        selected_value = dropdown_options[0].text
        print(f"Selected provider key: {selected_value}")

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
