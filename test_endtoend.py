import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PythonScripts.Baseclassfixture import Baseclass
from PythonScripts.CheckOutPage import CheckOutPage
from PythonScripts.ConfirmationPage import ConfirmPage
from PythonScripts.HomePage import HomePage


class TestOne(Baseclass):
    def test_endtoend(self):
        log = self.getlogger()
        homepage = HomePage(self.driver)
        Checkoutpage = homepage.shopItems()
        #checkOutPage = CheckOutPage(self.driver)
        log.info("Getting all card titles")
        select = Checkoutpage.getcardTitles()
        i = -1
        for phone in select:
            i = i+1
            iphone = phone.text
            log.info(iphone)
            #iphone = phone.find_element_by_xpath("div/h4/a").text
            if iphone == "iphone X":
                Checkoutpage.getcardOrder()[i].click()
        #self.driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()
        Checkoutpage.getcardItemself().click()
        #self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        confirmpage = Checkoutpage.getCheckoutITem()
        #confirmpage = ConfirmPage(self.driver)
        log.info("Going to get cuntry")
        confirmpage.getInput().send_keys("IND")
        #elf.driver.find_element_by_id("country").send_keys("IND")
        self.WaitMethod("//div[@class='suggestions']")
        #waits = WebDriverWait(self.driver, 9)
        #waits.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='suggestions']")))
        confirmpage.getCountry().click()
        confirmpage.getCheckbox().click()
        confirmpage.getSumbit().click()
        content = confirmpage.getAlert().text
        log.info(content)








