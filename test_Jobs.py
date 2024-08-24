from appium.webdriver.common.appiumby import AppiumBy
from typing import Any,Dict
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest,time

class Test_Jobs:
    def test_Notification(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            time.sleep(2)
            jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Jobs' and @index='1']")))
            jobs.click()
            time.sleep(10)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Jobs']"))).is_displayed()
            except:
                assert False,'Job page is missing'
            notification = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='2']")))
            notification.click()
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Notifications']"))).is_displayed()
            except:
                assert False,'Notification Page is Missing'
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
            jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Jobs' and @index='1']")))
            jobs.click()
            time.sleep(6)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Jobs']"))).is_displayed()
            except:
                assert False,'Job page is missing'
            my_profile = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            my_profile.click()
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
            jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Jobs' and @index='1']")))
            jobs.click()
            time.sleep(7)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Jobs']"))).is_displayed()
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
            jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Jobs' and @index='1']")))
            jobs.click()
            time.sleep(6)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Jobs']"))).is_displayed()
            except:
                assert False,'Job page is missing'
            search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='3']//android.widget.ImageView[@index='0']")))
            search_box.click()
            data='Sales'
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
            jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Jobs' and @index='1']")))
            jobs.click()
            time.sleep(13)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Jobs']"))).is_displayed()
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
            please_enter_input.send_keys('Sales')
            
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
            jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Jobs' and @index='1']")))
            jobs.click()
            time.sleep(13)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Jobs']"))).is_displayed()
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
            
            
    # def test_InterviewProcess_View_JoinInstitute(self, setup):
    #     self.driver = setup
    #     wait = WebDriverWait(self.driver, 23)
        
    #     try:
    #         click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
    #         click_on_app.click()

    #         check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
    #         assert check_dashboardlogo.is_displayed(), "Dashboard logo is not displayed"

    #         jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Jobs' and @index='1']")))
    #         jobs.click()
    #         time.sleep(7)
            
    #         manage_jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Jobs']")))
    #         assert manage_jobs.is_displayed(), "Manage Jobs page is missing"

    #         interview_process = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process']")))
    #         interview_process.click()
            
    #         assert interview_process.is_displayed(), "Interview Process page is missing"

    #         join_institute = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Join Institute']")))
    #         join_institute.click()
    #         time.sleep(4)

    #         assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Institute']"))).is_displayed(), "Institute page is missing"
            
    #         # Compare Joined Count
    #         actual_joined_count = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='2']//android.view.ViewGroup[1]//android.widget.TextView[@index='1']"))).text
    #         displayed_joined_count = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='3']//android.widget.TextView[@index='0']"))).text
    #         displayed_joined_count_num = int(re.search(r'\d+', displayed_joined_count).group()) if displayed_joined_count else None
    #         print(actual_joined_count)
    #         print(displayed_joined_count_num)
    #         assert actual_joined_count == displayed_joined_count_num, "Joined count does not match"
            
    #         # Compare Invited Count
    #         invited = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Invited']")))
    #         invited.click()

    #         actual_invited_count = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='2']//android.view.ViewGroup[2]//android.widget.TextView[@index='1']"))).text
    #         displayed_invited_count = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='3']//android.widget.TextView[@index='0']"))).text
    #         displayed_invited_count_num = int(re.search(r'\d+', displayed_invited_count.strip()).group()) if displayed_invited_count else None
            
    #         assert actual_invited_count.strip() == displayed_invited_count_num, "Invited count does not match"

    #         # Navigate Back
    #         back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
    #         back_button.click()
            
    #         assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process' and @index='1']"))).is_displayed(), "Failed to navigate back to Interview Process page"

    #     except Exception as e:
    #         assert False, f"Test failed due to an error: {str(e)}"

            
    def test_ActiveJobs_InterviewProcess_View_IntituteInvited(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Jobs' and @index='1']")))
            jobs.click()
            time.sleep(6)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Jobs']"))).is_displayed()
            except:
                assert False,'Job page is missing'
            interview_process = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process']")))
            interview_process.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process' and @index='1']"))).is_displayed()
            except:
                assert False,'Job page is missing'
            institite_invited = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Institute Invited']")))
            institite_invited.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Institute']"))).is_displayed()
            except:
                assert False,'Institute page is missing'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process' and @index='1']"))).is_displayed()
            except:
                assert False,'Institute page is missing'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Jobs']"))).is_displayed()
            except:
                assert False,'interview process page is missing'
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
            jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Jobs' and @index='1']")))
            jobs.click()
            time.sleep(6)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Jobs']"))).is_displayed()
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
            
    def test_ActiveJobs_JobProfile(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Jobs' and @index='1']")))
            jobs.click()
            time.sleep(6)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Jobs']"))).is_displayed()
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
            time.sleep(2)
            interview_process = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process']")))
            interview_process.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process' and @index='1']"))).is_displayed()
            except:
                assert False,'interview process page is not working proper'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process']"))).is_displayed()
            except:
                assert False,'interview process page back button is not working proper'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Jobs']"))).is_displayed()
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
            jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Jobs' and @index='1']")))
            jobs.click()
            time.sleep(6)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Jobs']"))).is_displayed()
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
            
    def test_Unpublished_ViewJobDetails(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Jobs' and @index='1']")))
            jobs.click()
            time.sleep(6)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Jobs']"))).is_displayed()
            except:
                assert False,'Job page is missing'    
                
            complete = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Completed']")))
            complete.click()
            
            unpublish = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Unpublished']")))
            unpublish.click()
            time.sleep(5)
            
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
            time.sleep(8)
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
            jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Jobs' and @index='1']")))
            jobs.click()
            time.sleep(6)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Jobs']"))).is_displayed()
            except:
                assert False,'Job page is missing'    
                
            complete = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Completed']")))
            complete.click()
            time.sleep(4)
            job=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@index='1']")))
            data=job.text
            job.click()
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
            time.sleep(4)
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process' and @index='1']"))).is_displayed()
            except:
                assert False,'interview process page is not working proper'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Jobs']"))).is_displayed()
            except:
                assert False,'Job Details page back button is not working proper'
        except:
            assert False,'Something went wrong'
            
    # def test_ActiveJobs_StartAcceptingApplication(self, setup):
    #     self.driver = setup
    #     wait = WebDriverWait(self.driver, 23)
    #     try:
    #         click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
    #         click_on_app.click()
    #         check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
    #         check_dashboardlogo.is_displayed()
    #         jobs = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Jobs' and @index='1']")))
    #         jobs.click()
    #         time.sleep(9)
    #         try:
    #             assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Jobs']"))).is_displayed()
    #         except:
    #             assert False,'Job page is missing'
    #         job = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@index='1']")))
            
    #         job.click()
    #         try:
    #             assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Job Details']"))).is_displayed()
    #         except:
    #             assert False,'Job details page is missing'
    #         start_accepting_application = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Start Accepting Applications']")))
    #         start_accepting_application.click()
            
    #         end_date = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
    #         end_date.click()
    #         next = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Next month")))
    #         next.click()
    #         select = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.View[@index='4']")))
    #         select.click()
    #         ok = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.Button[@text='OK']")))
    #         ok.click()
            
    #         time_ = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='3']//android.view.ViewGroup[@index='1' and @content-desc='']")))
    #         time_.click()
    #         select_hours = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "3")))
    #         select_hours.click()
    #         select_minutes= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "20")))
    #         select_minutes.click()
    #         ok = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.Button[@text='OK']")))
    #         ok.click()
            
    #         submit = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Submit']")))
    #         submit.click()
    #         time.sleep(4)
    #         try:
    #             assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Interview Process']"))).is_displayed()
    #         except:
    #             assert False,'StartAcceptingApplication is not properly done'
    #     except:
    #             assert False,'Something went wrong'
            