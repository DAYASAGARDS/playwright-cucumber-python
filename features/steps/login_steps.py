from behave import given, when, then

@given('I am on the login page')
def step_impl(context):
    context.login_page.navigate()

@when('I enter valid username and password')
def step_impl(context):
    # Using default credentials from config
    context.username = "Admin"
    context.password = "admin123"
    context.page.fill(context.login_page.USERNAME_INPUT, context.username)
    context.page.fill(context.login_page.PASSWORD_INPUT, context.password)

@when('I enter invalid username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.username = username
    context.password = password
    context.page.fill(context.login_page.USERNAME_INPUT, username)
    context.page.fill(context.login_page.PASSWORD_INPUT, password)

@when('I click on the login button')
def step_impl(context):
    context.page.click(context.login_page.LOGIN_BUTTON)

@when('I login with valid credentials')
def step_impl(context):
    context.login_page.navigate()
    context.login_page.login()

@then('I should be logged in successfully')
def step_impl(context):
    assert context.dashboard_page.is_dashboard_displayed(), "Dashboard is not displayed after login"

@then('I should see the dashboard page')
def step_impl(context):
    assert context.dashboard_page.is_dashboard_displayed(), "Dashboard page is not displayed"

@then('I should see an error message')
def step_impl(context):
    assert context.login_page.is_error_displayed(), "Error message is not displayed"