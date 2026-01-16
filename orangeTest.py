# open web browser (Chrome/firefox/IE)
# open URL 
# provide email
# provide password 
# click login 
# capture titel of the dashboard page 
# verify title of the page 
# close bowser 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

# 1️⃣ Open browser
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

# 2️⃣ Open URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# 3️⃣ Wait & enter username
username = wait.until(
    EC.visibility_of_element_located((By.NAME, "username"))
)
username.send_keys("Admin")

# 4️⃣ Wait & enter password
password = wait.until(
    EC.visibility_of_element_located((By.NAME, "password"))
)
password.send_keys("admin123")

# 5️⃣ Click login button
login_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
login_btn.click()

# 6️⃣ Validate title
act_title = driver.title
exp_title = "OrangeHRM"

try:
    dashboard_header = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )
    print("Login test passed :) - Dashboard loaded")

except:
    print("Login test failed :( - Dashboard not loaded")

# 7️⃣ Close browser
#driver.quit()

time.sleep(5)

