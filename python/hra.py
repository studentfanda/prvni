from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://1024game.org/?fbclid=IwAR1faznA6NoGxOPbshz6c9E1Qiw3DCbFLKns5nxxy5jY0QPbuAwOknDsnkI")
while True:
	for l in range(10):
		for i in range(5):
			for j in range(10):
				
				for k in range(10):
					actions = ActionChains(driver)
					actions.send_keys(Keys.ARROW_DOWN)
					actions.perform()
				actions = ActionChains(driver)
				actions.send_keys(Keys.ARROW_LEFT)
				actions.perform()
			actions = ActionChains(driver)
			actions.send_keys(Keys.ARROW_RIGHT)
			#actions.perform()
			#actions = ActionChains(driver)
			#actions.send_keys(Keys.ARROW_DOWN)
			actions.perform()
			actions = ActionChains(driver)
			actions.send_keys(Keys.ARROW_LEFT)
			actions.perform()
			driver.refresh()
	actions = ActionChains(driver)
	actions.send_keys(Keys.ARROW_UP)
	actions.perform()
 #   for key in [, Keys.UP, , Keys.ARROW_RIGHT]:
 #       actions = ActionChains(driver)
  #      actions.send_keys(key)
   #     actions.perform()
