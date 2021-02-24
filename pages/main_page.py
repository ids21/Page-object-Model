from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    def __init__(self, *args, **kwargs) -> None:
        super(MainPage, self).__init__(*args, **kwargs)
