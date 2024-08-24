from appium.webdriver.common.appiumby import AppiumBy
from typing import Any,Dict
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest,pyautogui,time,re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
#this is 
class Test_More:
    def test_View_Institutes(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            time.sleep(2)
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
            more.click()
            time.sleep(2)
            institutes = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Institutes']")))
            institutes.click()
            try:
                assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Institutes']"))).is_displayed()
            except:
                assert False,'Manage Institutes Page is Missing'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Institutes']"))).is_displayed()
            except:
                assert False,'Manage Institute back button is not working properly'
        except:
            assert False,'Something went Wrong'
    
    def test_Institutes_View_InstituteDetails(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            time.sleep(2)
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
            more.click()
            time.sleep(2)
            institutes = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Institutes']")))
            institutes.click()
            time.sleep(4)
            click_on_institutes = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.view.ViewGroup[@index='2']")))
            click_on_institutes.click()
            time.sleep(2)
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Institutes']"))).is_displayed()
            except:
                assert False,'Institutes page is missing'
            time.sleep(2)
            institutes_details= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Institute Details']")))
            institutes_details.click()
            time.sleep(4)
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='About Us']"))).is_displayed()
            except:
                assert False,'Institutes Details is missing'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Institutes']"))).is_displayed()
            except:
                assert False,'Institute Details Page back button is not working properly'
        except:
            assert False,'Something went Wrong'
            
            
    def test_Institutes_View_ManageTeam(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            time.sleep(2)
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
            more.click()
            time.sleep(2)
            institutes = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Institutes']")))
            institutes.click()
            time.sleep(3)
            click_on_institutes = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.view.ViewGroup[@index='2']")))
            click_on_institutes.click()
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Institutes']"))).is_displayed()
            except:
                assert False,'Institutes page is missing'
            time.sleep(2)
            manage_team= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Team']")))
            manage_team.click()
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Team Member']"))).is_displayed()
            except:
                assert False,'Manage Team Member Page is missing'
            time.sleep(1)
            click_one_memeber= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.view.ViewGroup//android.widget.TextView[@index='1']")))
            data=click_one_memeber.text
            click_one_memeber.click()
            time.sleep(2)
            try:
                data1=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@index='1']"))).text
                assert data.strip()==data1.strip()
            except:
                assert False,'memeber detail is missing'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Team Member']"))).is_displayed()
            except:
                assert False,'member Detail Page back button is not working properly'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Institutes']"))).is_displayed()
            except:
                assert False,'Manage Team Member Page back button is not working properly'
        except:
            assert False,'Something went Wrong'
            
    def test_Institutes_View_Departments(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            time.sleep(2)
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
            more.click()
            time.sleep(2)
            institutes = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Institutes']")))
            institutes.click()
            time.sleep(3)
            click_on_institutes = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.view.ViewGroup[@index='2']")))
            click_on_institutes.click()
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Institutes']"))).is_displayed()
            except:
                assert False,'Institutes page is missing'
            time.sleep(2)
            departments= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Departments']")))
            departments.click()
            time.sleep(4)
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Departments' and @index='1']"))).is_displayed()
            except:
                assert False,'Depatments Page is missing'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Institutes']"))).is_displayed()
            except:
                assert False,'Department Page back button is not working properly'
        except:
            assert False,'Something went Wrong'
            
    def test_Institutes_View_ManageCourse(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            time.sleep(2)
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
            more.click()
            time.sleep(2)
            institutes = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Institutes']")))
            institutes.click()
            time.sleep(3)
            click_on_institutes = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.view.ViewGroup[@index='2']")))
            click_on_institutes.click()
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Institutes']"))).is_displayed()
            except:
                assert False,'Institutes page is missing'
            time.sleep(2)
            manage_course= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Course']")))
            manage_course.click()
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Courses' and @index='1']"))).is_displayed()
            except:
                assert False,'Depatments Page is missing'
            click_on_course= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@index='0']")))
            click_on_course.click()
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Study Mode']"))).is_displayed()
            except:
                assert False,'Courses Details is showing'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Institutes']"))).is_displayed()
            except:
                assert False,'Manage Courses back button is not working properly'
        except:
            assert False,'Something went Wrong'
        
    def test_view_Teams(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 23)
        try:
            click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            time.sleep(2)
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
            more.click()
            time.sleep(2)
            teams = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Teams']")))
            teams.click()
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Team']"))).is_displayed()
            except:
                assert False,'Manage team page is missing'
            profile = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//android.widget.ScrollView//android.view.ViewGroup//android.widget.TextView[@index='1']")))
            for i in profile:
                data=i.text
                i.click()
                try:
                    data1=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@index='1']"))).text
                    assert data.strip()==data1.strip()
                except:
                    assert False,' profile data is not matched'
                back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
                back_button.click()
                try:
                    wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Team']"))).is_displayed()
                except:
                    assert False,'profile back button is not working properly'
                time.sleep(1)
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Teams']"))).is_displayed()
            except:
                assert False,'Manage Team back button is not working properly'
        except:
            assert False,'Something went wrong'
    
    def test_Directories_InstitutionDetails(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 25)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
            more.click()
            time.sleep(2)
            directories = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Directories']")))
            directories.click()
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Directories' and @index='1']")))
            except:
                assert False,'Directories Button is not working properly'
            # data=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//	android.widget.TextView[@index='1']"))).text
            select = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@index='1']")))
            for i in select:
                data=i.text
                i.click()
                try:
                    data1=  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.view.ViewGroup//android.widget.TextView[@index='0']"))).text
                    assert data==data1 and wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Institute Details']"))).is_displayed()
                except:
                    assert False,'Institute Details are not viewed properly'
                back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
                back_button.click()
                try:
                    assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Directories' and @index='1']"))).is_displayed()
                except:
                    assert False,'institute details Back Button is not Working Properly'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Directories']"))).is_displayed()
            except:
                assert False,'Directories Back Button is not Working Properly'
        except:
            assert False,'Something went Wrong'
            
            
    def test_feed_Notification(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 24)
        
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
            more.click()
            time.sleep(2)
            
            feed = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Feeds']")))
            feed.click()
            time.sleep(8)
            try:
                wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Feeds' and @index='1']"))).is_displayed()
            except:
                assert False,'Feed Page is not properly viewed'
            notification = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.ViewGroup[@index='2'  ]")))
            notification.click()
            time.sleep(2)
            try:
               wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Notifications' and @index='1']"))).is_displayed()
            except:
                assert False,'Notification Button is not working proper'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Feeds']"))).is_displayed()
            except:
                assert False,'Feed Notification Back Button is not Working Properly'
        except:
            assert False,'Something went wrong'
            
    def test_Feeds_Comments(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 25)

        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
            more.click()
            time.sleep(2)
            feed = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Feeds']")))
            feed.click()
            time.sleep(5)
            try:
                wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Feeds' and @index='1']"))).is_displayed()
            except:
                assert False,'Feed Page is not properly viewed'
            def post_comment(comment_text):
                try:
                    comment_button = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Comment']")))
                    comment_button.click()

                    input_comment = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@text='Write a comment...']")))
                    input_comment.send_keys(comment_text)

                    send_button = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='2' and @content-desc='']")))
                    send_button.click()

                    data=WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@text='Write a comment...']"))).text
                    try:
                        assert data=='Write a comment...'
                    except:
                        assert False,'message is not sended successfully'
                except Exception as e:
                    print(f"Exception occurred: {e}")
                    assert False, 'Comment is not posted properly'

            post_comment('Role ?')

        except Exception as e:
            print(f"Exception during initial attempt: {e}")
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(500, 1753)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(528, 881)
            actions.w3c_actions.pointer_action.release()
            actions.perform()

            try:
                post_comment('Role ?')
            except Exception as e:
                print(f"Exception during retry: {e}")
                assert False, 'No such post is available where automation will post the comment'

    def test_Feeds_Likes(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 25)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
            more.click()
            time.sleep(2)
            
            feed = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Feeds']")))
            feed.click()
            time.sleep(8)
            try:
                wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Feeds']"))).is_displayed()
            except:
                assert False,'Feed Page is not properly viewed'
            try:
                like = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Like']")))
                like.click()
                try:
                    assert WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Liked']"))).is_displayed()
                    like = WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Liked']")))
                    like.click()
                except:
                    assert False,'Like button is not properly work'
            except:
                actions = ActionChains(self.driver)
                actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                actions.w3c_actions.pointer_action.move_to_location(500, 1753)
                actions.w3c_actions.pointer_action.pointer_down()
                actions.w3c_actions.pointer_action.move_to_location(528, 881)
                actions.w3c_actions.pointer_action.release()
                actions.perform()
            try:
                like = WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.XPATH, '//android.view.ViewGroup[@content-desc="Like"]/android.widget.TextView')))
                like.click()
                try:
                    assert WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Liked']"))).is_displayed()
                    like = WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Liked']")))
                    like.click()
                except:
                    assert False,'Like button is not properly work'
            except:   
                actions = ActionChains(self.driver)
                actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                actions.w3c_actions.pointer_action.move_to_location(496, 1491)
                actions.w3c_actions.pointer_action.pointer_down()
                actions.w3c_actions.pointer_action.move_to_location(551, 716)
                actions.w3c_actions.pointer_action.release()
                actions.perform()
                like = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Like']")))
                like.click()
                try:
                    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Liked']"))).is_displayed()
                    like = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Liked']")))
                    like.click()
                except:
                    assert False,'Like button is not properly work'
        except:
            assert False ,"Connection Error"
            
    def test_Feeds_AddNew_Poll(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 27)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
            more.click()
            time.sleep(2)
            
            feed = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Feeds']")))
            feed.click()
            time.sleep(5)
            try:
                wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Feeds']"))).is_displayed()
            except:
                assert False,'Feed Page is not properly viewed'
            Poll = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text=' Add Poll']")))
            Poll.click()
            try:
                assert WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Create Poll']"))).is_displayed()
            except:
                assert False,'Poll button is working proper'
            clear = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Clear']")))
            clear.click()
            try:
                assert WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text=' Add Poll']"))).is_displayed()
            except:
                assert False,'Clear Button is Not working proper'
            time.sleep(2)
            Poll = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text=' Add Poll']")))
            Poll.click()
            try:
                assert WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Create Poll']"))).is_displayed()
            except:
                assert False,'Poll button is working proper'
            question = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@hint='E.g.,How do you commute to work?']")))
            question.send_keys('What is your preferred study method')
            
            option1 = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@text='Option 1']")))
            option1.send_keys('Group study')
            option2 = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@text='Option 2']")))
            option2.send_keys('Solo study')
            
            add_more_options = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text=' + Add More Option']")))
            add_more_options.click()
            option3 = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@text='Option 3']")))
            option3.send_keys('Tutoring sessions')
            
            poll_duration = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='1']")))
            poll_duration.click()
            select = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='7 days']")))
            select.click()
            next= WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Next']")))
            next.click()
            
            ask= WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "android.widget.EditText")))
            ask.send_keys('Late Morning')
            Post= WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Post']")))
            Post.click()
            try:
                assert WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Posted Successfully']"))).is_displayed()
            except:
                assert False,'Poll is not posted sucessfully'
        except:
            assert False ,"Connection Error"
    
    def test_Feeds_Poll(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 25)

        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()

            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            assert check_dashboardlogo.is_displayed(), 'Dashboard logo is not displayed'

            more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
            more.click()
            time.sleep(2)  

            feed = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Feeds']")))
            feed.click()
            time.sleep(8)  

            assert wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Feeds']"))).is_displayed(), 'Feed Page is not properly viewed'

            select = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.ScrollView//android.view.ViewGroup[@index='1']//android.view.ViewGroup[@index='2']")))
            select.click()

            assert wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.ScrollView//android.view.ViewGroup[@index='1']//android.view.ViewGroup[@index='2']//android.widget.TextView[@index='1']"))).is_displayed(), 'Poll is not working properly'

        except Exception as e:
            assert False, f'Something went wrong: {str(e)}'
            
    def test_Feeds_photo(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 27)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
            more.click()
            time.sleep(2)
            
            feed = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Feeds']")))
            feed.click()
            time.sleep(8)
            try:
                wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Feeds']"))).is_displayed()
            except:
                assert False,'Feed Page is not properly viewed'
            photo = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Photo']")))
            photo.click()
            try:
                assert WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Click here to upload photo']"))).is_displayed()
            except:
                assert False,'photo button is not working proper'
            clear = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Clear']")))
            clear.click()
            try:
                assert WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Photo']"))).is_displayed()
            except:
                assert False,'photo Clear button is not working proper'
            photo = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Photo']")))
            photo.click()
            post_now = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Post Now']")))
            post_now.click()
            time.sleep(7)
            try:
                data= WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@index='3']"))).text
                assert 'second ago' in data
            except:
                assert False,'photo is not successfully posted'
        except:
            assert False ,"Connection Error"
            
    def test_Video(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 28)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
            more.click()
            time.sleep(2)
            
            feed = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Feeds']")))
            feed.click()
            time.sleep(8)
            try:
                wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Feeds']"))).is_displayed()
            except:
                assert False,'Feed Page is not properly viewed'
            video = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Video']")))
            video.click()
            try:
                assert WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Click here to upload video']"))).is_displayed()
            except:
                assert False,'photo button is not working proper'
            clear = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Clear']")))
            clear.click()
            try:
                assert WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Video']"))).is_displayed()
            except:
                assert False,'photo Clear button is not working proper'
            photo = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Video']")))
            photo.click()
            post_now = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Post Now']")))
            post_now.click()
            time.sleep(7)
            try:
                data= WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@index='3']"))).text
                assert 'second ago' in data            
            except:
                assert False,'photo is not successfully posted'
        except:
            assert False ,"Connection Error"
    
    def test_PrivacyPolicy_Button(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 27)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
            more.click()
            time.sleep(2)
            
            privacy_policy = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Privacy Policy']")))
            privacy_policy.click()
            try:
                assert WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Privacy Policy' and @index='1']"))).is_displayed()
            except:
                assert False,'Privacy Policy page is not displayed properly'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Privacy Policy']")))
            except:
                assert False,'Privacy Policy Back Button is not  Working Properly'
        except:
            assert False ,"Connection Error"
            
    def test_Help_Button(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 28)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
            more.click()
            time.sleep(2)
            
            help = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Help']")))
            help.click()
            try:
                assert WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Help' and @index='1']"))).is_displayed()
            except:
                assert False,'Privacy Policy page is not displayed properly'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Help']")))
            except:
                assert False,'Privacy Policy Back Button is not  Working Properly'
        except:
            assert False ,"Connection Error"
            
    def test_syncCalendar(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 27)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
            more.click()
            time.sleep(2)
            
            sync_calander = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.ViewGroup[@index='6']")))
            sync_calander.click()
            # allow = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='Allow']")))
            # allow.click()
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Calendar Synced']")))
            except:
                assert False,'Calendar is not sync successfully'
            time.sleep(3)
            sync_calander = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.view.ViewGroup[@index='6']")))
            sync_calander.click()
            # allow = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='Allow']")))
            # allow.click()
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Calendar Sync Removed']")))
            except:
                assert False,'Calendar Sync is not removed successfully'
        except:
            assert False ,"somthing went wrong"
            
    def test_AboutCompany_Button(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 29)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
            more.click()
            time.sleep(2)
            try:
                about_company = WebDriverWait(self.driver,6).until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='About Company']")))
                about_company.click()
            except:
                els1 = self.driver.find_elements(by=AppiumBy.XPATH, value="\t\n//android.widget.Button[@text='Allow']")
                actions = ActionChains(self.driver)
                actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                actions.w3c_actions.pointer_action.move_to_location(652, 2670)
                actions.w3c_actions.pointer_action.pointer_down()
                actions.w3c_actions.pointer_action.move_to_location(679, 505)
                actions.w3c_actions.pointer_action.release()
                actions.perform()
                
                about_company = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='About Company']")))
                about_company.click()
            try:
                assert WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Company Details']"))).is_displayed()
            except:
                assert False,'Campus Details are not displayed properly'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='About Company']")))
            except:
                assert False,'About Campus Back Button is not  Working Properly'
        except:
            assert False ,"Connection Error"
            
    def test_Notifications(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 24)
        
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
            more.click()
            time.sleep(2)
            
            notifications = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Notifications']")))
            notifications.click()
            time.sleep(4)
            try:
                wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Manage Notifications']"))).is_displayed()
            except:
                assert False,'Manage Notification page is missing'
            click_on_notification = wait.until(EC.presence_of_all_elements_located((AppiumBy.XPATH, "//android.widget.ScrollView//android.widget.ImageView")))
            for i in click_on_notification:
                i.click()
            submit=wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.widget.TextView[@text='Submit']")))
            submit.click()
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Saved Successfully']")))
            except:
                assert False,'Saved Successfully Tostify is Missing'
            back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
            back_button.click()
            
            try:
                assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Notifications']")))
            except:
                assert False,'Notification Back button is not working properly'
        except:
            assert False ,"something went wrong"
    # def test_Communication_NewCommunication_through_email(self, setup):
    #     self.driver = setup
    #     wait = WebDriverWait(self.driver, 25)
    #     try:
    #         click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
    #         click_on_app.click()
    #         check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
    #         check_dashboardlogo.is_displayed()
    #         more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
    #         more.click()
    #         time.sleep(2)
    #         communication = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Communication']")))
    #         communication.click()
    #         time.sleep(10)
    #         try:
    #             assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Communication']")))
    #         except:
    #             assert False,'Manage Communication Page is not viewed Properly'
    #         new_communication = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='New Communication']")))
    #         new_communication.click()
    #         try:
    #             email=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Email']")))
    #             email.click()
    #         except:
    #             assert False,'Email button is missing in Manage Communication'
    #         try:
    #             assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Select Send to email']")))
    #         except:
    #             assert False,'Send Email Page is Missing'
    #         select= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView[@index='6']//android.view.ViewGroup[@index='2']//android.widget.ImageView[@index='3']")))
    #         select.click()
    #         next= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Next']")))
    #         next.click()
    #         try:
    #             assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Send email']")))
    #         except:
    #             assert False,'next button is not working proper'
    #         deafult_template= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@text='Please Select Template']")))
    #         deafult_template.click()
    #         select= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView[@index='0']//android.widget.TextView")))
    #         select.click()
    #         next= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Next']")))
    #         next.click()
    #         try:
    #             assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Email sent successfully']")))
    #         except:
    #             assert False,'Email is Not Sending Successful'
    #         back_to_new_commnication= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Back to New Communication']")))
    #         back_to_new_commnication.click()
            
    #         try:
    #             assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Communication']"))).is_displayed()
    #         except:
    #             assert False,'Back to communication button is not working proper'
    #         email=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Email']")))
    #         email.click()
    #         try:
    #             assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Select Send to email']")))
    #         except:
    #             assert False,'Send Email Page is Missing'
    #         select1= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView[@index='6']//android.view.ViewGroup[@index='2']//android.widget.ImageView[@index='3']")))
    #         select1.click()
    #         select2= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView[@index='6']//android.view.ViewGroup[@index='3']//android.widget.ImageView[@index='3']")))
    #         select2.click()
    #         next= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Next']")))
    #         next.click()
    #         try:
    #             assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Send email']")))
    #         except:
    #             assert False,'next button is not working proper'
    #         subject= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@hint='Please Enter Subject']")))
    #         subject.send_keys('interview')
    #         next= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Next']")))
    #         next.click()
    #         try:
    #             assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Email sent successfully']")))
    #         except:
    #             assert False,'Email is Not Sending Successful'
    #         check_applicants_staues= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Check applications status']")))
    #         check_applicants_staues.click()
    #         time.sleep(3)
    #         try:
    #             assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Notification Stats']")))
    #         except:
    #             assert False,'Notification Stats is not visisble properly'
    #         back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
    #         back_button.click()
    #         try:
    #             assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Check applications status']")))
    #         except:
    #             assert False,'Check applications status Back Button is Working Properly'
    #         back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
    #         back_button.click()
    #         try:
    #             assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Send email']")))
    #         except:
    #             assert False,'Check applications status Back Button is Working Properly'
    #         back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
    #         back_button.click()
    #         try:
    #             assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Select Send to email']")))
    #         except:
    #             assert False,'Send Email Back Button is Working Properly'
    #         back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
    #         back_button.click()
    #         try:
    #             assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Email']")))
    #         except:
    #             assert False,'Select Send to Email Page Back Button is Working Properly'
    #     except:
    #         assert False,'Something went Wrong'
            
    # def test_NewCommunication_through_SMS(self, setup):
    #     self.driver = setup
    #     wait = WebDriverWait(self.driver, 25)
    #     try:
    #         click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
    #         click_on_app.click()
    #         check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
    #         check_dashboardlogo.is_displayed()
    #         more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
    #         more.click()
    #         time.sleep(2)
    #         communication = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Communication']")))
    #         communication.click()
    #         time.sleep(10)
    #         try:
    #             assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Communication']")))
    #         except:
    #             assert False,'Manage Communication Page is not viewed Properly'
    #         new_communication = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='New Communication']")))
    #         new_communication.click()
    #         try:
    #             SMS=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='SMS']")))
    #             SMS.click()
    #         except:
    #             assert False,'sms button is missing in Manage Communication'
    #         try:
    #             assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Select Send to SMS']")))
    #         except:
    #             assert False,'Send Email Page is Missing'
                
    #         select= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView[@index='6']//android.view.ViewGroup[@index='2']//android.widget.ImageView[@index='3']")))
    #         select.click()
    #         next= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Next']")))
    #         next.click()
    #         deafult_template= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@text='Please Select Template']")))
    #         deafult_template.click()
    #         select= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView[@index='0']//android.widget.TextView")))
    #         select.click()
    #         next= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Next']")))
    #         next.click()
    #         try:
    #             assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Email sent successfully']")))
    #         except:
    #             assert False,'Email is Not Sending Successful'
    #     except:
    #         assert False,'Something went Wrong'
            
    # def test_NewCommunication_through_Notification(self, setup):
    #     self.driver = setup
    #     wait = WebDriverWait(self.driver, 25)
    #     try:
    #         click_on_app= wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
    #         click_on_app.click()
    #         check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
    #         check_dashboardlogo.is_displayed()
    #         more = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='More']")))
    #         more.click()
    #         time.sleep(2)
    #         communication = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Communication']")))
    #         communication.click()
    #         time.sleep(10)
    #         try:
    #             assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Communication']")))
    #         except:
    #             assert False,'Manage Communication Page is not viewed Properly'
    #         new_communication = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='New Communication']")))
    #         new_communication.click()
    #         try:
    #             notification=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Notification']")))
    #             notification.click()
    #         except:
    #             assert False,'sms button is missing in Manage Communication'
    #         try:
    #             assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Select Send to Notification']")))
    #         except:
    #             assert False,'Send Notification Page is Missing'
                
    #         select= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView[@index='6']//android.view.ViewGroup[@index='2']//android.widget.ImageView[@index='3']")))
    #         select.click()
    #         next= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Next']")))
    #         next.click()
    #         deafult_template= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@text='Please Select Template']")))
    #         deafult_template.click()
    #         time.sleep(4)
    #         select= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView[@index='0']//android.widget.TextView")))
    #         select.click()
    #         next= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Next']")))
    #         next.click()
    #         try:
    #             assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Notification sent successfully']")))
    #         except:
    #             assert False,'Email is Not Sending Successful'
    #         back_to_new_commnication= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Back to New Communication']")))
    #         back_to_new_commnication.click()
            
    #         try:
    #             assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Manage Communication']"))).is_displayed()
    #         except:
    #             assert False,'Back to communication button is not working proper'
    #         notification=wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Notification']")))
    #         notification.click()
    #         try:
    #             assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Select Send to Notification']")))
    #         except:
    #             assert False,'Send Notification Page is Missing'
    #         select1= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView[@index='6']//android.view.ViewGroup[@index='2']//android.widget.ImageView[@index='3']")))
    #         select1.click()
    #         select2= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView[@index='6']//android.view.ViewGroup[@index='3']//android.widget.ImageView[@index='3']")))
    #         select2.click()
    #         next= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Next']")))
    #         next.click()
            
    #         deafult_template= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@text='Please Select Template']")))
    #         deafult_template.click()
    #         time.sleep(4)
    #         select= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView[@index='0']//android.widget.TextView")))
    #         select.click()
    #         next= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Next']")))
    #         next.click()
    #         try:
    #             assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Notification sent successfully']")))
    #         except:
    #             assert False,'Email is Not Sending Successful'
    #         check_applicants_staues= wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Check applications status']")))
    #         check_applicants_staues.click()
    #         time.sleep(3)
    #         try:
    #             assert wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Notification Stats']")))
    #         except:
    #             assert False,'Notification Stats is not visisble properly'
    #         back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
    #         back_button.click()
    #         try:
    #             assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Check applications status']")))
    #         except:
    #             assert False,'Check applications status Back Button is Working Properly'
    #         back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
    #         back_button.click()
    #         back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
    #         back_button.click()
    #         try:
    #             assert  wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Select Send to Notification']")))
    #         except:
    #             assert False,'Send Email Back Button is Working Properly'
    #     except:
    #         assert False,'Something went Wrong'