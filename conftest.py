import time,pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from typing import Any,Dict
from pytest_html_reporter import attach
from appium.options.common import AppiumOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def setup():
    cap:Dict[str,Any]= {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:platformVersion": "13",
    'newCommandTimeout': 300 ,
    'autoGrantPermissions': True
    }
    driver = webdriver.Remote('http://localhost:4723', options=AppiumOptions().load_capabilities(cap))
   
    yield driver
    # time.sleep(2)
    # try:
    #     driver.quit()
    # except:
    #    WebDriverWait(driver, 25).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Done"))).is_displayed()
        
    driver.press_keycode(3)  
    driver.press_keycode(187) 
    time.sleep(1)

    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(778, 487)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(1260, 500)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
        
    el1 = driver.find_element(by=AppiumBy.ID, value="com.google.android.apps.nexuslauncher:id/clear_all")
    el1.click()
    driver.quit()
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        if "setup" in item.funcargs:
            driver = item.funcargs["setup"]
            screenshot = driver.get_screenshot_as_png()
            attach(data=screenshot)