from appium.webdriver.common.appiumby import AppiumBy
from typing import Any,Dict
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest,time,re
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction

class Test_Dashboard:
    def test_Notification(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            time.sleep(2)
            notification = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='2']")))
            notification.click()
            time.sleep(6)
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Notifications']"))).is_displayed()
            except:
                assert False,'Notification Page is Missing'
            time.sleep(4)
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            except:
                assert False,'Notification Back Button is Working Properly'
        except:
            assert False,'Something went Wrong'
            
            
    def test_myprofile_logo(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            time.sleep(4)
            my_profile = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            my_profile.click()
            time.sleep(6)
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Phone']"))).is_displayed()
            except:
                assert False,'Notification Page is Missing'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            except:
                assert False,'My Profile Back Button is Working Properly'
        except:
            assert False,'Something went Wrong'
            
    def test_View_Jobs(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            time.sleep(4)
            job = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text=' Jobs']")))
            job.click()
            time.sleep(6)
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='All Jobs']")))
            except:
                assert False,'All Jobs Page is Missing'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            except:
                assert False,'All Jobs Back Button is Working Properly'
        except:
            assert False,'Something went Wrong'
            
    def test_View_JobOpening(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            time.sleep(4)
            job_opening = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Jobs Opening']")))
            job_opening.click()
            time.sleep(6)
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Campus Job Openings']")))
            except:
                assert False,'Campus Job Openings Page is Missing'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            except:
                assert False,'All Jobs Back Button is Working Properly'
        except:
            assert False,'Something went Wrong'
            
    def test_View_OffersMade(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            time.sleep(4)
            offers_made = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Offers Made']")))
            offers_made.click()
            time.sleep(6)
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Jobs Offers']")))
            except:
                assert False,'Jobs Offers Page is Missing'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            except:
                assert False,'All Jobs Back Button is Working Properly'
        except:
            assert False,'Something went Wrong'
            
    def test_View_PendingVacancies(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            time.sleep(4)
            pending_vacancies = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Pending Vacancies']")))
            pending_vacancies.click()
            time.sleep(6)
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Campus Jobs']")))
            except:
                assert False,'Jobs Offers Page is Missing'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            except:
                assert False,'All Jobs Back Button is Working Properly'
        except:
            assert False,'Something went Wrong'
            
            
    def test_View_JobsStats(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            time.sleep(4)
            data=wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.ScrollView[@index='1']//android.widget.TextView[@index='0']"))).text
            
            stats = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.ScrollView[@index='1']//android.view.ViewGroup[@index='3']")))
            stats.click()
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Jobs Stats']")))
            except:
                assert False,'Job Stats page is missing'
            try:
                assert  data.strip()==wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@index='0']"))).text
            except:
                assert False,'Job Details are not matched'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            except:
                assert False,'All Jobs Back Button is Working Properly'
            time.sleep(3)
        except:
            assert False,'Something went Wrong'
            
    def test_ViewAllJobs_Button(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            time.sleep(4)
            
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(661, 2294)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(674, 1560)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
                
            viewall = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='View All']")))
            viewall.click()
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='0']//android.widget.TextView[@text='Jobs' and @index='1']"))).is_displayed()
            except:
                assert False,'All Jobs Back Button is Working Properly'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            except:
                assert False,'All Jobs Back Button is Working Properly'
        except:
            assert False,'Something went Wrong'