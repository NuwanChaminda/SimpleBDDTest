Feature: Selenium SDET test

  @Test_01
  Scenario Outline: As a Amazon User I could select item and get that item into cart
    Given I have go to <access_url> with page title <page_title_home>
    When I typed <search_words> in search box related to path <searchbox_element_path> and moved to page with title <page_title_search>
    And I clicked on 1st result <first_result_element> in search results and moved to page with title <page_title_1st_results>
    And I clicked on add to cart button <add_to_cart_element> in 1st result page and moved to page with title <page_title_add_cart>
    Then I clicked on cart button <cart_element> and get the cart page and moved to page with title <page_title_cart>

    Examples:
    |cart_element|add_to_cart_element|first_result_element|searchbox_element_path|search_words|access_url|page_title_home|page_title_search|page_title_1st_results|page_title_add_cart|page_title_cart|
    |//a[@data-csa-c-content-id="sw-gtc_CONTENT"]|//input[@id="add-to-cart-button"]|//div[@class="a-section aok-relative s-image-fixed-height"]//img[@data-image-index="1"]|//input[@id="twotabsearchtextbox"]|Apple iPhone 14 Pro|https://www.amazon.com|Amazon.com. Spend less. Smile more.|Amazon.com : apple iphone 14 pro|Amazon.com: Apple iPhone 14 Pro, 256GB, Space Black - Unlocked (Renewed) : Cell Phones & Accessories|Amazon.com Shopping Cart|Amazon.com Shopping Cart|