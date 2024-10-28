import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage

# def test_guest_can_add_product_to_basket(browser):
#    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_to_basket()
#    page.solve_quiz_and_get_code()

# def test_guest_can_see_prod_add_message(browser):
#    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_to_basket()
#    page.solve_quiz_and_get_code()
#    page.product_addition_message()

# def test_guest_can_see_price_message(browser):
#    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_to_basket()
#    page.solve_quiz_and_get_code()
#    page.price_message()
    
# def test_product_name_correct(browser):
#    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
#    page = ProductPage(browser,link)
#    page.open()
#    page.add_to_basket()
#    page.solve_quiz_and_get_code()
#    page.product_name_is_correct()

# def test_price_name_correct(browser):
#    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
#    page = ProductPage(browser,link)
#    page.open()
#    page.add_to_basket()
#    page.solve_quiz_and_get_code()
#    page.price_name_is_correct()

# def should_not_be_success_message(browser):
#    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
#    page = ProductPage(browser,link)
#    page.open()
#    page.add_to_basket()
#    page.solve_quiz_and_get_code()


# #@pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser,link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_not_be_success_message()

# def test_guest_cant_see_success_message(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser,link)
#     page.open()
#     page.should_not_be_success_message()

# #@pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser,link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.is_disappeared_success_message()

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

# def test_guest_can_add_product_to_basket(browser, link):
#     link = f'{link}'
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.product_name_is_correct()
#     page.price_name_is_correct()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page