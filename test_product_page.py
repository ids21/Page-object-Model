import pytest
import faker
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

links = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
]


product_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"


class TestUserAddToCartFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        password = 'sad@dsa99'
        faker_: faker.Faker = faker.Faker(locale='ru-RU')
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(faker_.email(), password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser) -> None:
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.should_not_see_success_message_upon_opening_product_page()

    @pytest.mark.need_review
    @pytest.mark.parametrize("link", links)
    def test_user_can_add_product_to_cart(self, browser, link: str) -> None:
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_cart(True)
        product_page.should_be_present_in_cart()
        product_page.should_check_overall_cost()


@pytest.mark.need_review
@pytest.mark.parametrize("link", links)
def test_guest_can_add_product_to_cart(browser, link: str) -> None:
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart(True)
    product_page.should_be_present_in_cart()
    product_page.should_check_overall_cost()


@pytest.mark.skip
@pytest.mark.parametrize("link", (pass_test if pass_test != 7 else pytest.param(pass_test, marks=pytest.mark.xfail) for pass_test  in range(10)))
def test_guest_can_add_product_to_cart_with_different_offer_numbers(
        browser, link: str) -> None:
    uri = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    product_page = ProductPage(browser, uri)
    product_page.open()
    product_page.add_to_cart(True)
    product_page.should_be_present_in_cart()
    product_page.should_check_overall_cost()


def test_guest_can_add_non_promo_product_to_cart(browser) -> None:
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_be_present_in_cart()
    product_page.should_check_overall_cost()


def test_guest_cant_see_success_message(browser) -> None:
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_not_see_success_message_upon_opening_product_page()


def test_guest_should_see_login_link_on_product_page(browser) -> None:
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser) -> None:
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser
                                                                 ) -> None:
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_empty()
    cart_page.should_contain_empty_text()