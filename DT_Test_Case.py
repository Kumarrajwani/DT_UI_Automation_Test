from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from email_config import send_email

class DistribusionWebTest:

	def test_web_dt(self):
		driver = webdriver.Firefox()
		driver.get("https://distribusion.com/")						
		name = driver.find_element_by_id("form-field-name")
		name.send_keys("John")
		email =  driver.find_element_by_id("form-field-email")
		email.send_keys("John@trainline.com")
		comapany = driver.find_element_by_id("form-field-field_1")
		comapany.send_keys("Trainline")
		msg = driver.find_element_by_id("form-field-message")
		msg.send_keys("Hey Quentin, Please check our API integration.\nThanks.\nBest regards,\nJohn")
		privacy_check = driver.find_element_by_id("form-field-9ca20e1")
		privacy_check.send_keys(Keys.ENTER)
		send_msg = driver.find_element_by_css_selector('.elementor-form .elementor-button.elementor-size-md')
		driver.close()
 

dtobject = DistribusionWebTest()
dtobject.test_web_dt()

 

 
  
   
	
 
 