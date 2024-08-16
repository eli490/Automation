from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

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
        WebDriverWait(driver, 40).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='provider_key_list']"))
        )

        # Use ActionChains to hover over and click the specific dropdown option
        dropdown_option = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='provider_key_list_0']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(dropdown_option).click().perform()

        # Ensure the selected value is now in the dropdown field
        selected_value = driver.find_element(By.XPATH, "//*[@id='provider_key']").get_attribute("value")
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
