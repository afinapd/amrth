Feature: SauceDemo Website Functionality
    As a user of SauceDemo
    I want to be able to login and use the website features
    So that I can shop and navigate through the site

    Background:
        Given I am on the SauceDemo login page

    @tc-1
    Scenario: Add item to cart
        When I login with "standard_user" and "secret_sauce"
        And I add "Sauce Labs Bolt T-Shirt" to the cart
        Then I should see "1" item in the cart
        And I should see "Sauce Labs Bolt T-Shirt" in the cart
        
    @tc-2
    Scenario: Navigate to About page
        When I login with "standard_user" and "secret_sauce"
        And I click on the hamburger menu
        And I click on the About link
        Then I should be redirected to "https://saucelabs.com/"