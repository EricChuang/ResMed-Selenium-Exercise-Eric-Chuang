import time
import math
from selenium import webdriver
from selenium.webdriver.common import keys

#See a webpage as an object
class Webpage_check:

#Initiate the webpage object giving its driver and URL
    def __init__(self, driver, URL):
        self.driver = driver
        self.URL = URL

#Method that searches a string in headings and paragraphs

    def find_text(self, tag, string):
        if tag == 'h':
            inc = 1
            while True:
                heading = 'h'+str(inc)
                heading_elements = self.driver.find_elements_by_tag_name(heading)
                if len(heading_elements) != 0:
                    for element in heading_elements:

                        if string.lower() == element.text.lower():
                            print(string, "found")
                            return element

                else:
                    print(string, "not found")

                inc += 1
            return 0

        else:
            if tag == 'p':
                paragraph_elements = self.driver.find_elements_by_tag_name('p')
                if len(paragraph_elements) != 0:
                    for element in paragraph_elements:
                        if string in element.text:
                            print(string, "found")
                            return element
                else:
                    print(string,"not found")
            else:
                return 0





    def link_find(self, linkstrings):

        for string in linkstrings:
            element = self.driver.find_element_by_link_text(string)
            if element != 0:
                return element
        return 0

#Method that searches multiple texts and simply state the presence/absence of the texts
    def heading_ispresent(self, strings):
        found_text = []

        for string in strings:
            element = self.find_text('h', string)
            found_text.append(element.text)

        return found_text

#Method that searches multiple links and simply state the presence/absence of the links
    def link_ispresent(self, linkstrings):
        found_link = []
        for string in linkstrings:
            element = self.driver.find_element_by_link_text(string)
            found_link.append(element.text)
        return found_link


def main():

#Start Selenium Chromedriver and go to ResMed USA website
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.resmed.com/us/en/consumer.html')

#Find the search box and click
    searchbox = driver.find_element_by_class_name('search-txt')
    if searchbox.text == 'What are you looking for?':
        searchbox.click()

#Enter "AirMini" in the searchbox and submit
    search_box = driver.find_element_by_id('primary-search')
    search_box.send_keys("AirMini")
    search_box.submit()

#Find and click the device "AirMini" in search results
    search_result = Webpage_check(driver,driver.current_url)
    heading_AirMini_element = search_result.find_text('h', "AirMini")

    if heading_AirMini_element != 0:
        heading_AirMini_element.click()

#Create a webpage check object for the AirMini webpage
    AirMini_webpage = Webpage_check(driver,driver.current_url)

#Search for texts in headings & links in links
    text_to_check = ['Small', 'Smart', 'Proven', 'HumidX system']
    found_text = AirMini_webpage.heading_ispresent(text_to_check)

    list1 = []
    list2 = []
    for text in found_text:
        list1.append(text.lower())
    for text in text_to_check:
        list2.append(text.lower())

    if list1 == list2:
        print(text_to_check, "are present")

    link_to_check = {'Read more'}
    found_link = AirMini_webpage.link_ispresent(link_to_check)

    link1 = []
    link2 = []
    for text in found_link:
        link1.append(text.lower())

    for text in link_to_check:
        link2.append(text.lower())

    if link1 == link2:
        print(link_to_check, "present")


#Find and click the tab "Cleaning"
    element = AirMini_webpage.link_find(['Cleaning'])
    print(element.get_property('title'))
    element.click()


#Search for text in headings
    text_to_check_cleaning = ['For P10 users']
    found_text_cleaning = AirMini_webpage.heading_ispresent(text_to_check_cleaning)
    list1 = []
    list2 = []
    for text in found_text_cleaning:
        list1.append(text.lower())
    for text in text_to_check_cleaning:
        list2.append(text.lower())

    if list1 == list2:
        print(text_to_check, "are present")

main()