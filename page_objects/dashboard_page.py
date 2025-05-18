from page_objects.base_page import BasePage

class DashboardPage(BasePage):
    # Locators
    DASHBOARD_TITLE = ".oxd-topbar-header-title"
    PIM_MENU = "//span[text()='PIM']"
    
    def is_dashboard_displayed(self):
        return self.is_visible(self.DASHBOARD_TITLE)
    
    def navigate_to_pim(self):
        self.page.click(self.PIM_MENU)