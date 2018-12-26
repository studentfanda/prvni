from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from array import array

driver = webdriver.Firefox()
driver.get("https://www.in-pocasi.cz/")
element = driver.find_element_by_name("mesto")
element.send_keys("Strmilov")
driver.find_element_by_name("hledat").click()

dest=0
prvek=[]
for i in range(8):
	text='sr_%d' % ((i)*3)
	prvek.append(driver.find_element_by_id(text).text)
	if prvek[i].endswith(' mm'):
		prvek[i] = prvek[i][:-3]
	dest=dest+float(prvek[i])
#	print (prvek[i])
#element2 = driver.find_element_by_id("sr_3").text
#element3 = driver.find_element_by_id("sr_6").text
#element4 = driver.find_element_by_id("sr_9").text
#element5 = driver.find_element_by_id("sr_12").text
#element6 = driver.find_element_by_id("sr_15").text
#element7 = driver.find_element_by_id("sr_18").text
#element8 = driver.find_element_by_id("sr_21").text
print ("V pristim tydnu naprsi "dest " mm")

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
