from behave import given, when, then

@when('I navigate to the PIM module')
def step_impl(context):
    context.dashboard_page.navigate_to_pim()

@then('I should see the employee list')
def step_impl(context):
    assert context.pim_page.is_pim_page_displayed(), "PIM page is not displayed"
    
@then('I should see employee records')
def step_impl(context):
    employee_count = context.pim_page.get_employee_count()
    assert employee_count > 0, f"Expected employee records, but found {employee_count}"
    
    employees = context.pim_page.get_employee_list()
    context.employee_list = employees
    print(f"Found {len(employees)} employees")