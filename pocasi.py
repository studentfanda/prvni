from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.in-pocasi.cz/")
element1 = driver.find_element_by_name("mesto")
element1.send_keys("Strmilov")
driver.find_element_by_name("hledat").click()

element2 = driver.find_element_by_id("t_0").text
print (element2)

assert " teplota:" in driver.page_source
#element2.send_keys("fs@strmilov.cz")
#


#while true:
#for i in range(10):  # Vnejsi cyklus
#	ActionChains(self._current_browser()).send_keys(Keys.ARROW_RIGHT).perform()
#    for j in range(5):  # Vnitrni cyklus
#       ActionChains(self._current_browser()).send_keys(Keys.ARROW_DOWN).perform()
#        if i <= j:
#            break



#assert "Po" in driver.title
#elem = driver.find_element_by_name("slovo-obec")
#print (elem)
#elem.clear()
#elem.send_keys("Strmilov")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#nadpis = driver.find_element_by_name('name')
print ("Dobehnul az do konce")
#driver.close()
