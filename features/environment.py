from playwright.sync_api import sync_playwright
from page_objects.login_page import LoginPage
from page_objects.dashboard_page import DashboardPage
from page_objects.pim_page import PIMPage

def before_all(context):
    print("Initializing Playwright...")
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)

def before_scenario(context, scenario):
    context.browser_context = context.browser.new_context()
    context.page = context.browser_context.new_page()
    
    # Initialize page objects
    context.login_page = LoginPage(context.page)
    context.dashboard_page = DashboardPage(context.page)
    context.pim_page = PIMPage(context.page)
    print(f"Playwright initialized. Browser and page are ready. Context page: {context.login_page}")

def after_scenario(context, scenario):
    context.browser_context.close()

def after_all(context):
    context.browser.close()
    context.playwright.stop()