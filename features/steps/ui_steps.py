import time
from behave import *
from config import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from UI_Methods.drivers import drivers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
use_step_matcher("re")


@given("I have go to (?P<access_url>.+) with page title (?P<page_title_home>.+)")
def step_impl(context, access_url, page_title_home):
    context.driver = drivers().get_chrome_driver(configarations['chrome_driver']['location'])
    context.driver.get("{0}".format(access_url))
    # assert "{0}".format(page_title_home) == context.driver.title


@when("I typed (?P<search_words>.+) in search box related to path (?P<searchbox_element_path>.+) and moved to page with title (?P<page_title_search>.+)")
def step_impl(context, search_words, searchbox_element_path, page_title_search):
    context.searchbox_elm = context.driver.find_element(By.XPATH, "{0}".format(searchbox_element_path))
    context.searchbox_elm.clear()
    context.searchbox_elm.send_keys("{0}".format(search_words))
    context.searchbox_elm.send_keys(Keys.RETURN)
    # assert "{0}".format(page_title_search) == context.driver.title


@step("I clicked on 1st result (?P<first_result_element>.+) in search results and moved to page with title (?P<page_title_1st_results>.+)")
def step_impl(context, first_result_element, page_title_1st_results):
    context.first_result_elm = context.driver.find_element(By.XPATH, "{0}".format(first_result_element))
    # context.driver.implicitly_wait(10)
    # wait = WebDriverWait(context.driver, 10)
    # context.first_result_elm = wait.until(EC.element_to_be_clickable(((By.XPATH,"{0}".format(first_result_element)))))
    context.first_result_elm.click()
    # context.driver.implicitly_wait(10)
    # assert "{0}".format(page_title_1st_results) in context.driver.title


@step("I clicked on add to cart button (?P<add_to_cart_element>.+) in 1st result page and moved to page with title (?P<page_title_add_cart>.+)")
def step_impl(context, add_to_cart_element, page_title_add_cart):
    # context.add_to_cart_element = context.driver.find_element(By.XPATH, "{0}".format(add_to_cart_element))
    context.driver.implicitly_wait(10)
    wait = WebDriverWait(context.driver, 10)
    context.add_to_cart_element = wait.until(EC.element_to_be_clickable(((By.XPATH, "{0}".format(add_to_cart_element)))))
    context.add_to_cart_element.click()
    # assert "{0}".format(page_title_add_cart) in context.driver.title


@Then("I clicked on cart button (?P<cart_element>.+) and get the cart page and moved to page with title (?P<page_title_cart>.+)")
def step_impl(context, cart_element, page_title_cart):
    context.cart_element = context.driver.find_element(By.XPATH, "{0}".format(cart_element))
    context.cart_element.click()
    # assert "{0}".format(page_title_cart) in context.driver.title
