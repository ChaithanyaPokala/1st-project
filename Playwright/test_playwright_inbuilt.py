import pytest
from playwright.sync_api import sync_playwright,Page,expect
def test_verify_pw_locators(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # page.get_by_label()
    page.get_by_label("Name:").fill("chaithanya")
    page.wait_for_timeout(5000)
    expect(page.get_by_label("Name:").fill("chaithanya")).to_be_visible()
    # page.get_by_placeholder
    email=page.get_by_placeholder("Enter EMail")
    email.fill("chaithu@gmail.com")
    expect(email).to_be_visible()
    #page.get_by_text()
    expect(page.get_by_text("Upload Files")).to_be_visible()
    #page.get_by_role
    page.get_by_role("heading",text="Static Web Table")

