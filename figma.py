import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# the interface for turning on headless mode 
options = Options() 
options.add_argument("-headless") 
 
# Set up the Firefox webdriver
driver = webdriver.Firefox()

# Define the URL of your Figma prototype
figma_url = "https://www.figma.com/proto/cWHSjCZRNjS4GOpWkXdm9s/INKY?type=design&node-id=1-2&scaling=min-zoom&page-id=0%3A1&hotspot-hints=0&hide-ui=1"

# Define the path where you want to save the screenshot
save_path = "./image.png"


# Navigate to the Figma prototype
driver.get(figma_url)

# Wait for the page to fully load (you may need to adjust the sleep time depending on the size of your prototype)
driver.set_window_size(800, 580)
time.sleep(10)

# Take a screenshot of the page and save it to the specified path
driver.save_screenshot(save_path)

# Quit the webdriver
driver.quit()
