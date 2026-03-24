import pytest
from playwright.sync_api import sync_playwright,Page,expect
def test_verify_bootstrap(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")
    page.locator("//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
    page.locator("//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
    page.locator("//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[6]/div/div[2]/div/div/div[2]/i").click()
