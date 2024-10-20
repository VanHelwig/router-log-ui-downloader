#!/usr/bin/env python3

# import list
import yaml
import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import glob

# Load the YAML configuration file
config_path = '/home/user/Scripts/Config/YAML/routerlogconfig.yml'
with open(config_path, 'r') as config_file:
    config = yaml.safe_load(config_file)

# Access the variables from the YAML configuration
router_ip = config['router']['ip']
router_password = os.getenv('ROUTER_PASSWORD')
router_url = config['urls']['router_url']
submenu_url = config['urls']['submenu']
password_field_xpath = config['xpaths']['password_field']
download_button_xpath = config['xpaths']['download_button']
driver_path = config['settings']['driver_path']
timeout = config['settings'].get('timeout', 5)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set up WebDriver with Firefox options
options = Options()
service = Service(driver_path)
driver = webdriver.Firefox(service=service, options=options)

# Function to wait for file download to complete
def wait_for_download_completion(download_dir):
    logging.info('Waiting for download to complete...')
    while any(glob.glob(f"{download_dir}/*.part")):  # Checking for incomplete files
        time.sleep(1)

# Navigate to router web UI and download logs locally
try:
    # Capture the list of files before the download starts
    download_dir = os.path.expanduser("~/Downloads")  # Default download location
    files_before = set(os.listdir(download_dir))

    # Navigate to the router login
    logging.info('Navigating to the router login page...')
    driver.get(router_url)

    # Wait for the password field to be present using the provided XPath
    logging.info('Waiting for password field...')
    password_field = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, password_field_xpath))
    )

    # Send the password and press Enter to submit the form
    logging.info('Entering password and submitting form...')
    password_field.send_keys(router_password + Keys.RETURN)
    
    # Wait for the page to load after login
    logging.info('Waiting for page load after login...')
    time.sleep(5)  # Adjust this based on actual load time if needed

    # Navigate to the submenu page where the download button is located
    logging.info('Navigating to submenu...')
    driver.get(submenu_url)
    time.sleep(5)  # Adjust this based on actual load time if needed

    # Find the download button using the provided XPath and click it
    logging.info('Waiting for download button and clicking...')
    download_button = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, download_button_xpath))
    )
    download_button.click()

    # Wait for the download to complete
    wait_for_download_completion(download_dir)

    # Capture the list of files after the download completes
    files_after = set(os.listdir(download_dir))

    # Identify the new files by comparing the before and after sets
    new_files = files_after - files_before
    logging.info(f'Newly downloaded files: {new_files}')

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    # Close the browser
    logging.info('Closing the browser...')
    driver.quit()
