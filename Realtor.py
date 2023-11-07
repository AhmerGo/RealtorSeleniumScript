from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



import time
import random

def random_wait(min_seconds=2, max_seconds=5):
    """Wait for a random time interval."""
    time.sleep(random.uniform(min_seconds, max_seconds))


url = "https://www.realtor.com/"

# Setup with modified options

driver = Driver() 
driver.set_window_size(1366, 768)
driver.get(url)

wait = WebDriverWait(driver, 20)
random_wait()

# Search for "Waukesha, WI"
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='search-bar']")))
search_box.send_keys("Waukesha, WI")
random_wait()
search_box.send_keys(Keys.ENTER)
random_wait()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

# Click 'More filter'
more_filter_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='More filter']")))
more_filter_btn.click()
random_wait()

# Scroll and click on Home Stories filter
home_stories_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='Home Stories-radio-group-Any']")))
ActionChains(driver).move_to_element(home_stories_label).click(home_stories_label).perform()
random_wait()

# Scroll and click on the 'chevron-status-wrapper' element
chevron_status_wrapper = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='chevron-status-wrapper'])[2]")))
chevron_status_wrapper.click()
random_wait()

# Select '7 days' from the dropdown
dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "(//select[@data-name='select-element'])[10]")))
dropdown.click()
random_wait()
seven_days_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@label='7 days']")))
seven_days_option.click()
random_wait()

# Input "Private well" and press enter
keyword_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Select a keyword or type here']")))
keyword_input.send_keys("Private well")
random_wait()
keyword_input.send_keys(Keys.ENTER)
random_wait()

# Click 'view-more-filters-results'
view_more_filters_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='view-more-filters-results']")))
view_more_filters_btn.click()
random_wait()

matching_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//section[@class='PropertiesList_propertiesContainer__HTNbx PropertiesList_listViewGrid__U_BlK'][1]//*[starts-with(@id, 'placeholder')]")))
count = len(matching_elements)

# Construct the array of XPaths
xpath_array = [f"//section[@class='PropertiesList_propertiesContainer__HTNbx PropertiesList_listViewGrid__U_BlK'][1]//*[starts-with(@id, 'placeholder')][{i}]" for i in range(1, count+1)]

# Click on each XPath, perform actions, and then go back
for xpath in xpath_array:
    prop = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    prop.click()
    random_wait()

    agent_overview_element = driver.find_element(By.XPATH, "(//span[starts-with(@class, 'LDPAgentOverviewstyles')])[2]")
    print(agent_overview_element.text)

    driver.back()
    random_wait()

driver.quit()
