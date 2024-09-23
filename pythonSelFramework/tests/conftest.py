"""
import pytest
import time
import self

from numpy.core.multiarray import item
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome" # py.test --browser_name firefox
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = ChromeService("C:/Users/vinhf/OneDrive/Desktop/testBrowsers/chromedriver.exe")  # install Chrome webdriver and specify the lovation fron Mac
        driver = webdriver.Chrome(service=service_obj)  # declare webdriver of Chrome
#       service = Service("C:/Users/vinhf/OneDrive/Desktop/testBrowsers/chromedriver.exe")
#       driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service_obj = FirefoxService("C:\\Users\\vinhf\\OneDrive\\Desktop\\testBrowsers\\geckodriver\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)  # firefox invocation Gecko Driver
    elif browser_name == "IE":
        print("IE driver")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = f'<div><img src="screenshots/{file_name}" alt="screenshot" style="width:304px;height:228px;" onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    if driver is not None:
        file_path = f"C:/Users/vinhf/PycharmProjects/pythonSelFramework/reports/screenshots{name}"
        driver.get_screenshot_as_file(file_path)
        print(f"Screenshot saved to {file_path}")
    else:
        print("Driver is not initialized.")


# Run in command line -> py.test --html=report.html
# Run file in command line -> pytest test_HomePage.py -s
# Configure and run in Jenkins website:
# cd tests
# py.test --browser_name firefox --html=report.html
# Configure parameter for browserName to select before run build:
# use %browserName% instead of using "$browserName" - if you have selected 'Execute Windows batch command' option (Window Users)
#cd tests
#py.test --browser_name "$browserName" --html=$WORKSPACE/reports/report.html


"""
import pytest
import openpyxl
import time
import os  # Try
import base64  # Try

from numpy.core.multiarray import item
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome" # py.test --browser_name firefox
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service = Service("C:/Users/vinhf/OneDrive/Desktop/testBrowsers/chromedriver.exe")
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = Service("C:\\Users\\vinhf\\OneDrive\\Desktop\\testBrowsers\\geckodriver\\geckodriver.exe")
        driver = webdriver.Firefox(service=service)  # firefox invocation Gecko Driver
    elif browser_name == "IE":
        print("IE driver")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
#    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;"'\
                            'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

# Run in command line -> py.test --html=report.html
# Run file in command line -> pytest test_HomePage.py -s

