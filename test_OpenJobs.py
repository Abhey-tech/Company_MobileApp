from appium.webdriver.common.appiumby import AppiumBy
from typing import Any,Dict
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest,time,re
 
class Test_OpenJobs:
    def test_Notification(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            time.sleep(2)
            open_jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']")))
            open_jobs.click()
            time.sleep(4)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']"))).is_displayed()
            except:
                assert False,'Job page is missing'
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
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='2']")))
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
            open_jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']")))
            open_jobs.click()
            time.sleep(4)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']"))).is_displayed()
            except:
                assert False,'Job page is missing'
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
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            except:
                assert False,'My Profile Back Button is Working Properly'
        except:
            assert False,'Something went Wrong'
            
            
    def test_ActiveJobs_Stats(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            open_jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']")))
            open_jobs.click()
            time.sleep(4)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']"))).is_displayed()
            except:
                assert False,'Job page is missing'
            stats = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Stats']")))
            stats.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Applicants by Batches']"))).is_displayed()
            except:
                assert False,'Job Status page is missing'
            time.sleep(8)
            back_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                 assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Stats']"))).is_displayed()
            except:
                assert False,'All students back button is not working proper'
        except:
            assert False,'Something went wrong'
    
    def test_SearchBox(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            open_jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']")))
            open_jobs.click()
            time.sleep(4)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']"))).is_displayed()
            except:
                assert False,'Job page is missing'
            search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='3']//android.widget.ImageView[@index='0']")))
            search_box.click()
            data='Manual'
            enter_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@text='Search']")))
            enter_text.clear()
            enter_text.send_keys(data)
            search = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.ImageView")))
            search.click()
            time.sleep(4)
            try:
                data1=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='3']//android.widget.TextView[@index='1']"))).text
                print(data)
                print(data1)
                assert data==data1
            except:
                assert False,'search box is not working proper'
            try:
                data1=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@index='1']"))).text
                assert data.strip() in data1.strip()
            except:
                assert False,'search box is not working proper'
        except:
            assert False,'Something went wrong'
            
    def test_SaveFilter(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            open_jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']")))
            open_jobs.click()
            time.sleep(4)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']"))).is_displayed()
            except:
                assert False,'Job page is missing'
            filter = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Filter']")))
            filter.click()
            add_new_filter = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Add New Filter']")))
            add_new_filter.click()
            time.sleep(10)
            select_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Select Field']")))
            select_field.click()
            select= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Job Title']")))
            select.click()
            
            condititon = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Condition']")))
            condititon.click()
            select= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Equals']")))
            select.click()
            
            please_enter_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='3']//android.widget.EditText")))
            please_enter_input.send_keys('Mobile')
            
            save_a_filter= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Save A Filter']")))
            save_a_filter.click()
            
            data='First_Filter'
            filter_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@hint='Enter Filter Name']")))
            filter_name.send_keys(data)
            
            save= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Save']")))
            save.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Filter saved successfully']"))).is_displayed()
            except:
                assert False,'Filter is successfully saved tostify is missing'
            time.sleep(3)
            filter = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Filter']")))
            filter.click()
            savefilter = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Saved Filters']")))
            savefilter.click()
            try:
                data1= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@index='0']"))).text
                assert data==data1
            except:
                assert False,'Filter is successfully saved in Saved Filters folder'
            edit = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.ImageView[@index='1']")))
            edit.click()
            time.sleep(8)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Filters']"))).is_displayed()
            except:
                assert False,'Filter Edit Button is not working properly'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            
        except:
            assert False,'Something went wrong'
            
    def test_Delete_SaveFilter(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 30)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            open_jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']")))
            open_jobs.click()
            time.sleep(4)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']"))).is_displayed()
            except:
                assert False,'Job page is missing'
            filter = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Filter']")))
            filter.click()
            savefilter = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Saved Filters']")))
            savefilter.click()
            delete = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//	android.widget.ImageView[@index='0']")))
            delete.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Delete Successfully']"))).is_displayed()
            except:
                assert False,'Filter Delete  successfully  tostify is missing'
        except:
            assert False,'Something went wrong'

            
    def test_ActiveJobs_InterviewProcess_View_AllApplicants(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            open_jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']")))
            open_jobs.click()
            time.sleep(4)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']"))).is_displayed()
            except:
                assert False,'Job page is missing'
            interview_process = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process']")))
            interview_process.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process' and @index='1']"))).is_displayed()
            except:
                assert False,'Job page is missing'
            data2=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.view.ViewGroup[@index='1']//android.widget.TextView[@index='3']"))).text
            data=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='4']//android.widget.TextView[@index='1']"))).text
            all_applicants = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='All Applicants']")))
            all_applicants.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='All Applicants' and @index='1']"))).is_displayed()
            except:
                assert False,'All Applicants page is missing'
            
            applicants_count = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='2']//android.view.ViewGroup[1]//android.widget.TextView[@index='1']"))).text
            
            rows_count = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='4']//android.widget.TextView[@index='0']"))).text
            match = re.search(r'\d+', rows_count.strip())
            numeric_value = int(match.group()) if match else None
            print(numeric_value)
                
            try:
                data==applicants_count==numeric_value
            except:
                assert False,'applicants count will not matched'  
               
            
            offers = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Offers']")))
            offers.click()   
            time.sleep(3)
            offers_count = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='2']//android.view.ViewGroup[2]//android.widget.TextView[@index='1']"))).text
            
            rows_count = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='4']//android.widget.TextView[@index='0']"))).text
            match = re.search(r'\d+', rows_count.strip())
            numeric_value = int(match.group()) if match else None
            print(numeric_value)
                
            try:
                data2==offers_count==numeric_value
            except:
                assert False,'offers count will not matched'  
            
            applicant = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Applicants']")))
            applicant.click()
            time.sleep(1)
            try:
                WebDriverWait(self.driver,7).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='No Data Found !']"))).is_displayed()
            except:
                select = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.view.ViewGroup[@index='1']//android.view.ViewGroup[@index='0' and @content-desc='']")))
                select.click()  
                msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.view.ViewGroup[@index='1']//android.view.ViewGroup[@index='4' and @content-desc='']")))
                msg.click() 
                try:
                    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='E-Mail']"))).is_displayed()
                except:
                    assert False,'msg button is not working proper'
                email= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='E-Mail']")))
                email.click() 
                time.sleep(2)
                try:
                    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Send email']"))).is_displayed()
                except:
                    assert False,'send email page is not opened successfully'
                back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
                back_button.click()
                try:
                    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='All Applicants' and @index='1']"))).is_displayed()
                except:
                    assert False,'email page back button is not working proper'
                    
                msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.view.ViewGroup[@index='1']//android.view.ViewGroup[@index='4' and @content-desc='']")))
                msg.click() 
                try:
                    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='E-Mail']"))).is_displayed()
                except:
                    assert False,'msg button is not working proper'
                sms= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='SMS']")))
                sms.click() 
                time.sleep(2)
                try:
                    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Send SMS ']"))).is_displayed()
                except:
                    assert False,'send SMS page is not opened successfully'
                back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
                back_button.click()
                try:
                    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='All Applicants' and @index='1']"))).is_displayed()
                except:
                    assert False,'SMS page back button is not working proper'
                    
                msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.view.ViewGroup[@index='1']//android.view.ViewGroup[@index='4' and @content-desc='']")))
                msg.click() 
                try:
                    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='E-Mail']"))).is_displayed()
                except:
                    assert False,'msg button is not working proper'
                notification= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Notification']")))
                notification.click() 
                time.sleep(2)
                try:
                    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@hint='Please Select Template']"))).is_displayed()
                except:
                    assert False,'send email page is not opened successfully'
                back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
                back_button.click()
                try:
                    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='All Applicants' and @index='1']"))).is_displayed()
                except:
                    assert False,'notification page back button is not working proper'
                
                back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
                back_button.click()
                try:
                    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process' and @index='1']"))).is_displayed()
                except:
                    assert False,'all applicants page is missing'
                back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
                back_button.click()
                try:
                    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']"))).is_displayed()
                except:
                    assert False,'interview process page is missing'
        except:
            assert False,'Something went wrong'
            
    def test_ActiveJobs_InterviewProcess_AllApplicants_SearchBox(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            open_jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']")))
            open_jobs.click()
            time.sleep(4)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']"))).is_displayed()
            except:
                assert False,'Job page is missing'
            interview_process = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process']")))
            interview_process.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process' and @index='1']"))).is_displayed()
            except:
                assert False,'Job page is missing'
            # data=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='4']//android.widget.TextView[@index='1']"))).text
            all_applicants = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='All Applicants']")))
            all_applicants.click()
            time.sleep(3)
            try:
                WebDriverWait(self.driver,7).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='No Data Found !']"))).is_displayed()
                
            except:
                search = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='4']//android.widget.ImageView[@index='0']")))
                search.click()
                data='Riddhi'
                enter_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@text='Search']")))
                enter_text.clear()
                enter_text.send_keys(data)
                search = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.ImageView")))
                search.click()
                time.sleep(4)
                try:
                    data1=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='4']//android.view.ViewGroup[@index='1']"))).text
                    print(data)
                    print(data1)
                    assert data==data1
                except:
                    assert False,'search box is not working proper'
                try:
                    search_check=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='4']//android.widget.TextView[@index='2']"))).text
                    assert data.strip() in search_check.strip()
                except:
                    assert False,'search is working proper'
        except:
            assert False,'Something went wrong'
   
    def test_ActiveJobs_unpublish(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            open_jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']")))
            open_jobs.click()
            time.sleep(4)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']"))).is_displayed()
            except:
                assert False,'Job page is missing'
            job = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@index='1']")))
            data11=job.text
            job.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Job Details']"))).is_displayed()
            except:
                assert False,'Job details page is missing'
            unpublish = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Unpublish']")))
            unpublish.click()
            yes = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Yes']")))
            yes.click()
            complete = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Completed']")))
            complete.click()
            
            unpublish = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Unpublished']")))
            unpublish.click()
            time.sleep(2)
            search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='3']//android.widget.ImageView[@index='0']")))
            search_box.click()
            data=data11
            enter_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@text='Search']")))
            enter_text.clear()
            enter_text.send_keys(data)
            search = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.ImageView")))
            search.click()
            time.sleep(4)
            try:
                data1=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@index='1']"))).text
                assert data.strip() in data1.strip()
            except:
                assert False,'Job is not publish properly'
        except:
            assert False,'Something went wrong'
            
    def test_ActiveJobs_JobProfile(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            open_jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']")))
            open_jobs.click()
            time.sleep(4)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']"))).is_displayed()
            except:
                assert False,'Job page is missing'
            job = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@index='1']")))
            job.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Job Details']"))).is_displayed()
            except:
                assert False,'Job details page is missing'
                
            job_summary = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Job Summary' and @index='0']")))
            job_summary.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@text='Job Summary']"))).is_displayed()
            except:
                assert False,'job summary details is not viewed poperly'
                
            about_company = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='About Company']")))
            about_company.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@text='About Company']"))).is_displayed()
            except:
                assert False,'about company details is not viewed poperly'
                
            eligibility_criteria = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Eligibility Criteria']")))
            eligibility_criteria.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@text='Eligibility Criteria']"))).is_displayed()
            except:
                assert False,'eligibility criteria details is not viewed poperly'
                
            hiring_workflow = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Hiring Workflow']")))
            hiring_workflow.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@text='Hiring Workflow']"))).is_displayed()
            except:
                assert False,'hiring workflow details is not viewed poperly'
                
            interview_process = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process']")))
            interview_process.click()
            time.sleep(1)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process' and @index='1']"))).is_displayed()
            except:
                assert False,'interview process page is not working proper'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Job Details']"))).is_displayed()
            except:
                assert False,'interview process page back button is not working proper'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']"))).is_displayed()
            except:
                assert False,'Job Details page back button is not working proper'
        except:
            assert False,'Something went wrong'
            
    def test_Unpublished_PublishJob(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            open_jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']")))
            open_jobs.click()
            time.sleep(4)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']"))).is_displayed()
            except:
                assert False,'Job page is missing'
                
            complete = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Completed']")))
            complete.click()
            
            unpublish = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Unpublished']")))
            unpublish.click()
            time.sleep(2)
            data11=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//	android.widget.TextView[@index='1']"))).text
            publish = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Publish']")))
            publish.click()
            yes = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.Button[@text='YES']")))
            yes.click()
            time.sleep(2)
            complete.click()
            time.sleep(2)
            active_job = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Active Jobs']")))
            active_job.click()
            time.sleep(2)
            
            search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='3']//android.widget.ImageView[@index='0']")))
            search_box.click()
            data=data11
            enter_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@text='Search']")))
            enter_text.clear()
            enter_text.send_keys(data)
            search = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.ImageView")))
            search.click()
            time.sleep(4)
            try:
                data1=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@index='1']"))).text
                assert data.strip() in data1.strip()
            except:
                assert False,'Job is not publish properly'
        except:
            assert False,'Something went wrong'
            
    def test_Unpublished_ViewJobDetails(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            open_jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']")))
            open_jobs.click()
            time.sleep(4)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs' and @index='1']"))).is_displayed()
            except:
                assert False,'Job page is missing'    
                
            complete = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Completed']")))
            complete.click()
            time.sleep(2)
            unpublish = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Unpublished']")))
            unpublish.click()
            time.sleep(2)
            
            click_on_job = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@index='1']")))
            data11=click_on_job.text
            click_on_job.click()
            try:
                assert data11==wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@index='0']"))).text
            except:
                assert False,'Job details are not matched while viewing the job details in unpublish section'
            
            job_summary = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Job Summary' and @index='0']")))
            job_summary.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@text='Job Summary']"))).is_displayed()
            except:
                assert False,'job summary details is not viewed poperly'
                
            about_company = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='About Company']")))
            about_company.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@text='About Company']"))).is_displayed()
            except:
                assert False,'about company details is not viewed poperly'
                
            eligibility_criteria = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Eligibility Criteria']")))
            eligibility_criteria.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@text='Eligibility Criteria']"))).is_displayed()
            except:
                assert False,'eligibility criteria details is not viewed poperly'
                
            hiring_workflow = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Hiring Workflow']")))
            hiring_workflow.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@text='Hiring Workflow']"))).is_displayed()
            except:
                assert False,'hiring workflow details is not viewed poperly'
                
            Publish = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Publish']")))
            Publish.click()
            yes = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Yes']")))
            yes.click()
            time.sleep(2)
            complete.click()
            active_job = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Active Jobs']")))
            active_job.click()
            time.sleep(2)
            
            search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='3']//android.widget.ImageView[@index='0']")))
            search_box.click()
            data=data11
            enter_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@text='Search']")))
            enter_text.clear()
            enter_text.send_keys(data)
            search = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.ImageView")))
            search.click()
            time.sleep(4)
            try:
                data1=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='3']//android.widget.TextView[@index='1']"))).text
                print(data)
                print(data1)
                assert data==data1
            except:
                assert False,'search box is not working proper'
            try:
                data1=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@index='1']"))).text
                assert data.strip() in data1.strip()
            except:
                assert False,'Job is not publish properly'
        except:
            assert False,'Something went wrong'
            
    def test_View_CompletedJobs(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            open_jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']")))
            open_jobs.click()
            time.sleep(4)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']"))).is_displayed()
            except:
                assert False,'Job page is missing'    
                
            complete = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Completed']")))
            complete.click()
            time.sleep(4)
            job=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@index='1']")))
            data=job.text
            job.click()
            time.sleep(3)
            try:
                assert data== wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@index='0']"))).text
            except:
                assert False,'job details are not matched' 
            job_summary = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Job Summary' and @index='0']")))
            job_summary.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@text='Job Summary']"))).is_displayed()
            except:
                assert False,'job summary details is not viewed poperly'
                
            about_company = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='About Company']")))
            about_company.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@text='About Company']"))).is_displayed()
            except:
                assert False,'about company details is not viewed poperly'
                
            eligibility_criteria = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Eligibility Criteria']")))
            eligibility_criteria.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@text='Eligibility Criteria']"))).is_displayed()
            except:
                assert False,'eligibility criteria details is not viewed poperly'
                
            hiring_workflow = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Hiring Workflow']")))
            hiring_workflow.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@text='Hiring Workflow']"))).is_displayed()
            except:
                assert False,'hiring workflow details is not viewed poperly'
            time.sleep(2)
            interview_process = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process']")))
            interview_process.click()
            time.sleep(3)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process' and @index='1']"))).is_displayed()
            except:
                assert False,'interview process page is not working proper'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            time.sleep(2)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Job Details']"))).is_displayed()
            except:
                assert False,'Job Details page back button is not working proper'
            time.sleep(2)
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']"))).is_displayed()
            except:
                assert False,'Job Details page back button is not working proper'
            interview_process = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process']")))
            interview_process.click()
            time.sleep(5)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process' and @index='1']"))).is_displayed()
            except:
                assert False,'interview process page is not working proper'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Open Jobs']"))).is_displayed()
            except:
                assert False,'interview process page back button is not working proper'
           
            stats = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Stats']")))
            stats.click()
            time.sleep(5)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Applicants by Batches']"))).is_displayed()
            except:
                assert False,'Job Status page is missing'
            time.sleep(8)
            back_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                 assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Stats']"))).is_displayed()
            except:
                assert False,'stats page back button is not working proper'
        except:
            assert False,'Something went wrong'