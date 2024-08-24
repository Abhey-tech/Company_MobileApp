from appium.webdriver.common.appiumby import AppiumBy
from typing import Any,Dict
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Test_Messages:
    def test_Notification(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 40)
        try:
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()
            check_dashboardlogo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            check_dashboardlogo.is_displayed()
            message = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Messages']")))
            message.click()
            time.sleep(2)
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Request Help']"))).is_displayed()
            except:
                assert False,'Messages Page is Missing'
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
            
    def test_chats(self, setup):
        self.driver = setup
        wait = WebDriverWait(self.driver, 40)

        try:
  
            click_on_app = wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Company_App")))
            click_on_app.click()

            # Step 2: Verify Dashboard logo
            dashboard_logo = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Dashboard']")))
            assert dashboard_logo.is_displayed(), "Dashboard logo not displayed"

            # Step 3: Navigate to Messages
            messages_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Messages']")))
            messages_tab.click()

            # Step 4: Select a specific chat
            chat_item = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.widget.TextView[@index='1']")))
            chat_item.click()

            # Step 5: Enter and send a message
            message_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@hint='Enter Message']")))
            message_input.send_keys('Hello')

            send_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup[@index='4']")))
            send_button.click()

            # Step 6: Verify that the message was sent by checking if the input field is empty
            time.sleep(2)  # Wait for the message to be sent
            input_field_after_send = message_input.text
            print('msg -',input_field_after_send)
            assert input_field_after_send =='Enter Message', "Message input field is not empty, message was not sent properly"
            print("Message sent successfully")

        except AssertionError as e:
            print(f"Test failed: {e}")
            assert False, e
        except Exception as e:
            print(f"Something went wrong: {e}")
            assert False, 'Something went wrong'
        finally:
            # Step 7: Navigate back and verify
            try:
                back_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ImageView[@index='0']")))
                back_button.click()

                # Verify that the user is back on the chat list screen
                chat_list_screen = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.ScrollView//android.view.ViewGroup[@index='1']")))
                assert chat_list_screen.is_displayed(), "Back Button is not working properly"
            except Exception as e:
                print(f"Back navigation failed: {e}")
                assert False, 'Message Back Button is not working properly'
            