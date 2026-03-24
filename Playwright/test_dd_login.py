import pytest
from playwright.sync_api import sync_playwright,Page,expect
login_data=[("testingload123@gmail.com","test@123","valid"),
            ("invalid@example.com","test@123","invalid"),
            ("valid@example.com","tstxyz","invalid"),
            ("","","invalid")]
@pytest.mark.parametrize("email,password,validity", login_data)
def test_dd_login(email,password,validity,page:Page):
    page.goto("https://demowebshop.tricentis.com/login")
    # page.locator("body > div.master-wrapper-page > div.master-wrapper-content > div.header > div.header-links-wrapper > div.header-links > ul > li:nth-child(2) > a").click()
    page.locator(".email").fill(email)
    page.locator(".password").fill(password)
    page.locator("body > div.master-wrapper-page > div.master-wrapper-content > div.master-wrapper-main > div.center-2 > div > div.page-body > div.customer-blocks > div.returning-wrapper > div.form-fields > form > div.buttons > input").click()
    if validity=="valid":
        expect(page.locator(".ico-logout")).to_be_visible()
    else:
        expect(page.locator(".validation-summary-errors")).to_be_visible()
