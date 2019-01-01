from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import matplotlib.pyplot as plt 
import numpy as np
from array import array
import time

driver = webdriver.Firefox()
driver.get("https://www.in-pocasi.cz/")
element = driver.find_element_by_name("mesto")
element.send_keys("Strmilov")
driver.find_element_by_name("hledat").click()
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'sr_0')))
dest=0
teploty=[]
#assert "No results found." not in driver.page_source
text=[]
for j in range(1,8):
	#print(driver.find_element_by_id("d_%d"%j).text)
	text.append(driver.find_element_by_id("d_%d"%j).text)
	driver.find_element_by_id("d_%d"%j).click()
	for i in range(8):
		srazky=driver.find_element_by_id("sr_%d" % ((i)*3)).text
		teplota=driver.find_element_by_id("t_%d" % ((i)*3)).text
		teplota = teplota[:-3]
		teploty.append(float(teplota))
		if srazky.endswith(' mm'):
			srazky = srazky[:-3]
		dest=dest+float(srazky)
		#print (teplota)
print (text)
#element2 = driver.find_element_by_id("sr_3").text
#element3 = driver.find_element_by_id("sr_6").text
#element4 = driver.find_element_by_id("sr_9").text
#element5 = driver.find_element_by_id("sr_12").text
#element6 = driver.find_element_by_id("sr_15").text
#element7 = driver.find_element_by_id("sr_18").text
#element8 = driver.find_element_by_id("sr_21").text
print("V pristim tydnu naprsi %s mm" % dest)
#print(teploty)
x = np.arange(0, 7, float(1)/8)
dny = np.arange(0, 7, 1)
#print(teploty)
#pos_temp[teploty <= 0] = np.nan
#neg_temp[teploty > 0] = np.nan


#fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
#plt.plot(pos_temp, color='g')
#plt.plot(neg_temp, color='r')
#plt.fill_between(x, 0, pos_temp)
#plt.fill_between(x, 0, neg_temp)
plt.fill_between(x, 0, teploty,where=teploty[x] >= 0, facecolor='red', interpolate=True)
plt.ylabel('teplota')
plt.xlabel('cas')
plt.xticks(dny,text)


#ax2.fill_between(x, teploty, 1)
#ax2.set_ylabel('between y1 and 1')

#ax3.fill_between(x, teploty, y2)
#ax3.set_ylabel('between y1 and y2')
#ax3.set_xlabel('x')
#plt.plot(teploty)
#plt.fill_between(x, 0, teploty)
#plt.show()

#plt.plot(teploty)
plt.show()

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
driver.close()
