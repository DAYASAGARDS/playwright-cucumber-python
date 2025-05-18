from page_objects.base_page import BasePage
from utils.config import USERNAME, PASSWORD

class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "button[type='submit']"
    ERROR_MESSAGE = ".oxd-alert-content-text"
    
    def navigate(self):
        super().navigate_to()
        self.wait_for_element(self.USERNAME_INPUT)
    
    def login(self, username=USERNAME, password=PASSWORD):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)
    
    def is_error_displayed(self):
        return self.is_visible(self.ERROR_MESSAGE)
    
    def get_error_message(self):
        if self.is_error_displayed():
            return self.page.text_content(self.ERROR_MESSAGE)
        return None