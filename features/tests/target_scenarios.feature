Feature: Tests for Target site

  Scenario: Verify "Your cart is empty" message
    Given Open Target main page
    When Click on cart icon
    Then Empty Cart message is shown

  Scenario: Verify ability to open Sign In form
    Given Open Target main page
    When Click Account button
    Then Click Sign In button
    Then Verify Sign In page

  Scenario Outline: Search for a product
    Given Open Target main page
    When Search for <product>
    Then Search results for <product_results> are shown
    Examples:
    |product   |product_results  |
    |tea       |tea              |
    |mug       |mug              |
    |coffee    |coffee           |

  Scenario: Verify benefit cells
    Given Open Target main page
    When Click Target Circle
    Then Verify 5 benefit cells are shown

  Scenario Outline: Verify cart addition
    Given Open Target main page
    When Search for <product>
    Then Click Add to Cart Button
    Then Click 2nd Add to Cart Button
    Then Click View Cart Button
    Then Verify Cart
    Examples:
    |product     |
    |bread       |