Feature: User Authentication
  As a user
  I want to be able to login to the OrangeHRM system
  So that I can access the system features

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter valid username and password
    And I click on the login button
    Then I should be logged in successfully
    And I should see the dashboard page

  Scenario: Failed login with invalid credentials
    Given I am on the login page
    When I enter invalid username "invalid" and password "invalid123"
    And I click on the login button
    Then I should see an error message