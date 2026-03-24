import pytest
from playwright.sync_api import sync_playwright,Page,expect
def test_verify_css(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("#name").fill("chaitanya")
    page.get_by_placeholder("Enter EMail").fill("chaitanya@gmail.com")
    page.locator("#phone").fill("9876568898")
    # page.locator("#male").check()
    # page.wait_for_timeout(5000)
    # page.locator("input[value=sunday]").check()
    # page.locator("input[value=sunday]").uncheck()
    days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    checkboxes=[]
    for day in days:
        page.get_by_label(day)
        checkboxes.append(page.get_by_label(day))
        print(checkboxes)
        print(len(checkboxes))
        #to check all the checkboxes
    # for checkbox in checkboxes:
    #     checkbox.check()
    #     expect(checkbox).to_be_checked()

        # page.wait_for_timeout(5000)
        #to check last three checkboxes
    for checkbox in checkboxes[-3:]:
        checkbox.check()
        page.wait_for_timeout(2000)
        # expect(checkbox).to_be_checked()






