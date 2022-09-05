#
# screenshot.py
#
# kevinabrandon@gmail.com
#
# edit by simon@sandm.co.uk to use Chromedriver

import sys
import time
import traceback
from selenium import webdriver
from selenium.common import exceptions as seleniumexceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from configparser import ConfigParser

import util

# Read the configuration file for this application.
parser = ConfigParser()
parser.read('config.ini')

# Assign AboveTustin variables.
abovetustin_image_width = int(parser.get('abovetustin', 'image_width'))
abovetustin_image_height = int(parser.get('abovetustin', 'image_height'))

capabilities = webdriver.DesiredCapabilities.CHROME.copy()
capabilities['chrome.page.settings.resourceTimeout'] = "20000"
# capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
# capabilities['firefox.page.settings.resourceTimeout'] = "20000"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-web-security")
options.add_argument("--disable-site-isolation-trials")
options.add_argument("--userdata-dir=/home/pi/chromium")
options.add_argument("--user-agent=xxxxxxxxxxxxxxxx")
# options = webdriver.FirefoxOptions()
# options.add_argument("--headless")

#  Check for Crop settings
if parser.has_section('crop'):
    do_crop = parser.getboolean('crop', 'do_crop')
    crop_x = parser.getint('crop', 'crop_x')
    crop_y = parser.getint('crop', 'crop_y')
    crop_width = parser.getint('crop', 'crop_width')
    crop_height = parser.getint('crop', 'crop_height')
    if do_crop:
        try:
            from PIL import Image
            from io import BytesIO
            print('will crop')
        except ImportError:
            print('Image manipulation module "Pillow" not found, cropping disabled')
            do_crop = False
else:
    do_crop = False

# Assign dump1090 variables.
g_request_timeout = float(parser.get('abovetustin', 'request_timeout'))


class AircraftDisplay(object):
    def __init__(self, url):
        self.url = url
        self.browser = None
        self.loadmap()

    def loadmap(self):
        raise NotImplementedError

    def reload(self):
        self.browser.quit()
        self.browser = None
        self.loadmap()

    def screenshot(self, name):
        '''
        screenshot()
        Takes a screenshot of the browser
        '''
        if do_crop:
            print('cropping screenshot')
            #  Grab screenshot rather than saving
            im = self.browser.get_screenshot_as_png()
            im = Image.open(BytesIO(im))

            #  Crop to specifications
            im = im.crop((crop_x, crop_y, crop_width, crop_height))
            im.save(name)
        else:
            self.browser.save_screenshot(name)
        print("success saving screenshot: %s" % name)
        return name

    def ClickOnAirplane(self, ident):
        raise NotImplementedError


class Dump1090Display(AircraftDisplay):
    def loadmap(self):
        '''
        loadmap()
        Creates a browser object and loads the webpage.
        It sets up the map to the proper zoom level.

        Returns the browser on success, None on fail.

        Now using Chromedriver
        '''

        browser = webdriver.Chrome('/usr/bin/chromedriver', desired_capabilities=capabilities, options=options)
        # browser = webdriver.Firefox('/usr/bin/chromedriver', desired_capabilities=capabilities, options=options)
        browser.set_window_size(abovetustin_image_width, abovetustin_image_height)

        print("getting web page {}".format(self.url))
        browser.set_page_load_timeout(15)
        browser.get(self.url)

        # Need to wait for the page to load
        timeout = g_request_timeout
        print ("waiting for page to load...")
        wait = WebDriverWait(browser, timeout)
        try:
            element = wait.until(EC.element_to_be_clickable((By.ID,'dump1090_version')))
        except seleniumexceptions.TimeoutException:
            util.error("Loading %s timed out.  Check that you're using the "
                       "correct driver in the .ini file." % (self.url,))
            browser.save_screenshot('timeout.png')
            util.error('Saved screenshot at timeout.png')
            raise

        print("reset map:")
        resetbutton = browser.find_elements(By.XPATH, '//*[contains(@title,"Reset Map")]')
        resetbutton[0].click()


#        print("zoom in 3 times:")
#        try:
#           # First look for the Open Layers map zoom button.
#           zoomin = browser.find_element_by_class_name('ol-zoom-in')
#           print("Zoom: ",zoomin)
#       except seleniumexceptions.NoSuchElementException as e:
#           # Doesn't seem to be Open Layers, so look for the Google
#          # maps zoom button.
#         zoomin = browser.find_elements_by_xpath('//*[@title="Zoom in"]')
#        if zoomin:
#           zoomin = zoomin[0]
#       zoomin.click()
#       zoomin.click()
#       zoomin.click()

        self.browser = browser

    def clickOnAirplane(self, text):
        '''
        clickOnAirplane()
        Clicks on the airplane with the name text, and then takes a screenshot
        '''
        print(text)
        try:
            element = self.browser.find_elements(By.XPATH, "//td[text()='%s']" % text.lower())
            print("number of elements found: %i" % len(element))
            if len(element) > 0:
                print("clicking on {}!".format(text))
                element[0].click()
                time.sleep(5.0) # if we don't wait a little bit the airplane icon isn't drawn.
                return self.screenshot('tweet.png')
            else:
                print("couldn't find the object")
        except Exception as e:
            util.error("Could not click on airplane: {}".format(e))
            return None


class VRSDisplay(AircraftDisplay):
    def loadmap(self):
        '''
        loadmap()
        Creates a browser object and loads the webpage.
        It sets up the map to the proper zoom level.

        Returns the browser on success, None on fail.
        '''
        browser = webdriver.PhantomJS(desired_capabilities={'phantomjs.page.settings.resourceTimeout': '20000'})
        browser.set_window_size(abovetustin_image_width, abovetustin_image_height)

        print("getting web page {}".format(self.url))
        browser.set_page_load_timeout(15)
        browser.get(self.url)

        # Need to wait for the page to load
        timeout = g_request_timeout
        print ("waiting for page to load...")
        wait = WebDriverWait(browser, timeout)
        element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'vrsMenu')))
        self.browser = browser

    def clickOnAirplane(self, text):
        '''
        clickOnAirplane()
        Clicks on the airplane with the name text, and then takes a screenshot
        '''
        try:
            aircraft = self.browser.find_element(By.XPATH, "//td[text()='%s']" % text)
            aircraft.click()
            time.sleep(0.5) # if we don't wait a little bit the airplane icon isn't drawn.
            show_on_map = self.browser.find_element_by_link_text('Show on map')
            show_on_map.click()
            time.sleep(5.0)
            return self.screenshot('tweet.png')
        except Exception as e:
            util.error("Unable to click on airplane: {}'".format(e))
            return None
