from selenium import webdriver

web_driver_path = "E:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=web_driver_path)
driver.get("https://www.python.org/")
# price_element = driver.find_element_by_id("priceblock_ourprice")
# search_bar = driver.find_element_by_name("q")
# doc_link = driver.find_element_by_css_selector(".documentation-widget a")
driver.find_element_by_xpath("//*[@id='touchnav-wrapper']/header/div/div[1]/a")
print(driver.find_element_by_xpath("//*[@id='touchnav-wrapper']/header/div/div[1]/a")
.text)


driver.quit()
