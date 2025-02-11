from behave import given, when, then

@given('I am on the SauceDemo login page')
def navigate_to_login_page(context):
    context.login_page.navigate()

@when('I login with "{username}" and "{password}"')
def login_with_credentials(context, username, password):
    context.login_page.login(username, password)

@when('I add "{item}" to the cart')
def add_item_to_cart(context, item):
    context.inventory_page.add_item_to_cart(item)

@then('I should see "{count}" item in the cart')
def verify_cart_count(context, count):
    cart_count = context.inventory_page.get_cart_count()
    assert int(cart_count) == int(count), f"Expected {count} items in cart, but found {cart_count}"

@then('I should see "{item}" in the cart')
def verify_item_in_cart(context, item):
    context.inventory_page.open_cart()  # First open the cart
    assert context.cart_page.is_item_in_cart(item), f"Expected {item} in cart, but not found"

@when('I click on the hamburger menu')
def click_hamburger_menu(context):
    context.inventory_page.click_hamburger_menu()

@when('I click on the About link')
def click_about_link(context):
    context.inventory_page.click_about_link()

@then('I should be redirected to "{url}"')
def verify_redirection(context, url):
    assert context.inventory_page.get_current_url() == url, f"Not redirected to {url}"
