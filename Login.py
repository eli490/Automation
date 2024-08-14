from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with actual login credentials
username = "elvin.opak"  # Replace with actual username
password = "Sumova@24"  # Replace with actual password

# Specify the path to the ChromeDriver executable
chrome_driver_path = "C:/Users/elvin.opak/SeleniumProject/Driver/chromedriver.exe"
service_obj = Service(chrome_driver_path)


# Function to log in to the web application
def login_to_application():
    # Initialize the Chrome WebDriver with the specified Service
    driver = webdriver.Chrome(service=service_obj)

    # Open the web application
    driver.get(
        "https://qa.data.smartapplicationsgroup.com/connect/login")  # Replace with the actual URL of the login page

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
        login_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='main-login-container-wrapper']"))  # Replace with the
            # correct XPath
        )
        login_button.click()

        # Wait for some indication of a successful login, like the presence of a dashboard element
        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='main-login-container-wrapper']"))
            # Replace with the correct XPath or other identifier
        )

        # Print success message
        print("Login successful.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()


# Call the function to log in
login_to_application()
