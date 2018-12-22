from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://1024game.org/?fbclid=IwAR1faznA6NoGxOPbshz6c9E1Qiw3DCbFLKns5nxxy5jY0QPbuAwOknDsnkI")

while True:
    for key in [Keys.DOWN, Keys.UP, Keys.ARROW_LEFT, Keys.ARROW_RIGHT]:
        actions = ActionChains(driver)
        actions.send_keys(key)
        actions.perform()
