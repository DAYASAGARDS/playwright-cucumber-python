Feature: Employee List
  As an HR admin
  I want to view the list of employees
  So that I can manage employee records

  Scenario: View employee list in PIM module
    Given I am on the login page
    When I login with valid credentials
    And I navigate to the PIM module
    Then I should see the employee list
    And I should see employee records