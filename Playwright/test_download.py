import pytest
from playwright.sync_api import sync_playwright,expect,Page
def test_download_file(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    page.locator("#inputText").fill("welcome")
    page.locator("#generateTxt").click()
    page.on("download",lambda download:download.save_as("downloads/test2.txt"))
    page.locator("#txtDownloadLink").click()


