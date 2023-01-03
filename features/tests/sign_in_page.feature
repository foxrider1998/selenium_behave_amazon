
Feature: Test Scenarios for Amazon Sign In Page

  Scenario: User can go through Sign In Links and Fields
    Given Open Amazon page
    When Select: Hello, Sign In Account and Lists
    Then Verify user on the signin page
    And Fill up email/phone field: fakeEmail@FakeEmail
    Then Verify Error Message: There was a problem
    When Select Conditions of Use
    Then Verify Conditions of Use is the page
    And Go Back and Refresh the Page