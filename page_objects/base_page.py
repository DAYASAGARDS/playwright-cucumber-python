from utils.config import BASE_URL, DEFAULT_TIMEOUT

class BasePage:
    def __init__(self, page):
        self.page = page
        self.base_url = BASE_URL
        self.default_timeout = DEFAULT_TIMEOUT
        
    def navigate_to(self, path=""):
        url = f"{self.base_url}{path}"
        self.page.goto(url)
        
    def get_title(self):
        return self.page.title()
        
    def wait_for_element(self, selector):
        return self.page.wait_for_selector(selector, timeout=self.default_timeout)
    
    def is_visible(self, selector):
        try:
            element = self.page.wait_for_selector(selector, timeout=5000, state="visible")
            return element is not None
        except:
            return False