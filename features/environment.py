from playwright.sync_api import sync_playwright
from page_objects.login_page import LoginPage
from page_objects.dashboard_page import DashboardPage
from page_objects.pim_page import PIMPage
import os
from datetime import datetime

def before_all(context):
    print("Initializing Playwright...")
    context.playwright = sync_playwright().start()
    # Create traces directory if it doesn't exist
    os.makedirs("traces", exist_ok=True)
    context.browser = context.playwright.chromium.launch(headless=False)

def before_scenario(context, scenario):
    context.browser_context = context.browser.new_context()
    # Start tracing
    context.browser_context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )
    context.page = context.browser_context.new_page()
    
    # Initialize page objects
    context.login_page = LoginPage(context.page)
    context.dashboard_page = DashboardPage(context.page)
    context.pim_page = PIMPage(context.page)
    print(f"Playwright initialized. Browser and page are ready. Context page: {context.login_page}")

def after_scenario(context, scenario):
    # Generate unique filename with timestamp and scenario name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    scenario_name = scenario.name.replace(" ", "_").lower()
    trace_file = f"traces/{timestamp}_{scenario_name}.zip"
    
    # Stop tracing and save to file
    context.browser_context.tracing.stop(path=trace_file)
    print(f"Trace saved to: {trace_file}")
    
    context.browser_context.close()

def after_all(context):
    context.browser.close()
    context.playwright.stop()