Feature: Tests for Target site

  Scenario: Verify "Your cart is empty" message
    Given Open Target main page
    When Click on cart icon
    Then "Your cart is empty" message displays

  Scenario: Verify ability to open Sign In form
    Given Open Target main page 2
    When Click Account button
    Then Click Sign In button
    Then Verify Sign In page