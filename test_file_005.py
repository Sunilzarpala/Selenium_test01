import allure
import pytest
from selenium import webdriver
class Test_practice_01:
    def test_sum_001(self):
        a=5
        b=9
        c= a+b
        print('sum of a and b:',c )
        if c==14:
            assert True
        else:
            assert False


    def test_credenceURL_002(self):
        driver= webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("you are at credence.in")
            assert True
            driver.close()
        else:
            print('you entered wrong URL' )
            driver.close()
            assert False


    def test_sum_008(self):
        a = 3
        b = 7
        sum = a + b
        print("Sum of a and b is :" + str(sum))
        if sum == 10:
            assert True
        else:
            assert False



    def test_sub_009(self):
        a = 3
        b = 7
        sub = a - b
        print("Subtraction of a from b is :" + str(sub))
        if sub == -4:
            assert True
        else:
            assert False