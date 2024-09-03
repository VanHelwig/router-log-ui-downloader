#!/usr/bin/env python3

# import list
import yaml
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Load the YAML configuration file
config_path = '/home/user/Scripts/Config/YAML/routerlogconfig.yml'
with open(config_path, 'r') as config_file:
    config = yaml.safe_load(config_file)

# Access the variables from the YAML configuration
router_ip = config['router']['ip']
router_password = config['router']['password']
router_url = config['urls']['router_url']
submenu_url = config['urls']['submenu']
password_field_xpath = config['xpaths']['password_field']
download_button_xpath = config['xpaths']['download_button']
download_dir = config['settings']['download_dir']
driver_path = config['settings']['driver_path']

# Configure Firefox profile for downloads
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.download.folderList", 2)  # 2 for custom location
firefox_profile.set_preference("browser.download.dir", download_dir)
firefox_profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

# Set up WebDriver with Firefox profile
options = Options()
options.profile = firefox_profile
service = Service(driver_path)
driver = webdriver.Firefox(service=service, options=options)

# Navigate to router web UI and download logs locally
try:
    # Capture the list of files before the download starts
    files_before = set(os.listdir(download_dir))

    # Navigate to the router login
    # Wait for the password field to be present using the provided XPath
    # Send the password and press Enter to submit the form
    # Wait for the page to load after login
    driver.get(router_url)
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, password_field_xpath))
    )
    password_field.send_keys(router_password + Keys.RETURN)
    time.sleep(5)

    # Navigate to the submenu page where the download button is located
    # Wait for the page to load
    # Find the download button using the provided XPath and click it
    # Wait for the download to complete (adjust time as needed)
    driver.get(submenu_url)
    time.sleep(5)
    download_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, download_button_xpath))
    )
    download_button.click()
    time.sleep(10)

    # Capture the list of files after the download completes
    # Identify the new files by comparing the before and after sets
    # Print the names of the newly downloaded files
    files_after = set(os.listdir(download_dir))
    new_files = files_after - files_before
    print(f'Newly downloaded files: {new_files}')

finally:
    # Close the browser
    driver.quit()
