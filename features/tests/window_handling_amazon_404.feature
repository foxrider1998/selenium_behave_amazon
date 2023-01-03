
Feature: Testing Amazon 404 pages, window handling, waiting for windows to open, switch, close, go back

  Scenario Outline: Amazon 404 pages, open blogs, switch window, close, and go back
    Given <404> Page of Amazon
    When Store original windows
    Then Click to open blog
    When Switch to the newly opened window
    And User closes new window and goes back to old window
    Examples:
      |                                     404                                       |
      |   https://www.amazon.com/Aris/Aloodor-Elegr-Sd_wg=zyAcN&pf_rd_p=9b&sz10cnVl  |