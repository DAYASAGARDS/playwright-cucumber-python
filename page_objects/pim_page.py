from page_objects.base_page import BasePage

class PIMPage(BasePage):
    # Locators
    PAGE_TITLE = ".oxd-topbar-header-breadcrumb-module"
    EMPLOYEE_LIST = ".oxd-table-body"
    EMPLOYEE_ROWS = ".oxd-table-body .oxd-table-row"
    EMPLOYEE_NAME_CELL = ".oxd-table-cell:nth-child(3)"
    
    def is_pim_page_displayed(self):
        return self.is_visible(self.PAGE_TITLE) and self.page.text_content(self.PAGE_TITLE) == "PIM"
    
    def get_employee_list(self):
        # Wait for the employee list to load
        self.wait_for_element(self.EMPLOYEE_LIST)
        
        # Get all employee rows
        rows = self.page.query_selector_all(self.EMPLOYEE_ROWS)
        
        employees = []
        for row in rows:
            # Extract employee data from the row
            name = row.query_selector(self.EMPLOYEE_NAME_CELL).text_content().strip()
            employees.append(name)
            
        return employees
    
    def get_employee_count(self):
        self.wait_for_element(self.EMPLOYEE_ROWS)
        rows = self.page.query_selector_all(self.EMPLOYEE_ROWS)
        return len(rows)