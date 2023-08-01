from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import pytest
class Test_checkout:
    @pytest.mark.sunil
    def test_checkout(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://automation.credence.in/login")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Credencetest123456@test.com")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Credence@123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//h3[normalize-space()='Apple Macbook Pro']").click()
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
        driver.find_element(By.XPATH, "//h3[normalize-space()='Apple iPad Retina']").click()
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
        driver.find_element(By.XPATH, "//h3[normalize-space()='Headphones']").click()
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()

        q1 = Select(driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]/select[1]"))
        q1.select_by_index(3)
        time.sleep(2)
        q2 = Select(driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/select[1]"))
        q2.select_by_index(2)
        time.sleep(2)
        q3 = Select(driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[3]/td[3]/select[1]"))
        q3.select_by_index(1)
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
        driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("sunil")
        driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("zarpala")
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("6000000001")
        driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys("karvenagar")
        driver.find_element(By.XPATH, "//input[@id='zip']").send_keys("411052")
        address1 = Select(driver.find_element(By.XPATH, "//select[@id='state']"))
        address1.select_by_visible_text('Pune')
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("sunil")
        driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys("257")
        year = Select(driver.find_element(By.XPATH, "//select[@id='exp_year']"))
        year.select_by_index(2)
        month = Select(driver.find_element(By.XPATH, "//select[@id='exp_month']"))
        month.select_by_index(6)
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("4716")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("1089")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("9971")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("6531")
        time.sleep(10)
        driver.find_element(By.XPATH, "//button[@id='confirm-purchase']").click()
        print(driver.find_element(By.XPATH, "//p[@class='w-lg-50 mx-auto']").text)
        time.sleep(10)
        try:
            (driver.find_element(By.XPATH, "//p[@class='lead w-lg-50 mx-auto']"))
            print(driver.find_element(By.XPATH, "//p[@class='lead w-lg-50 mx-auto']").text)
            assert True
            print("Placed order")
        except:
            assert False
            print("Failed to place order")