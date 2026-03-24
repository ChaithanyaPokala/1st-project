import pytest
from playwright.sync_api import sync_playwright,expect,Page
def test_file_uploading(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #single file uploading
    # page.locator("#singleFileInput").set_input_files("uploads/test1.txt")
    # page.get_by_text(text="Upload Single File").click()
    # expect(page.locator("#singleFileStatus")).to_contain_text("Single file selected")
    # page.wait_for_timeout(5000)


    #uploading multiple files
    files=("uploads/test1.txt","uploads/test2.txt")
    page.locator("#multipleFilesInput").set_input_files(files)
    page.wait_for_timeout(5000)
    page.get_by_text(text="Upload Multiple Files").click()
    expect(page.locator("#multipleFilesStatus")).to_contain_text("test1.txt")
    expect(page.locator("#multipleFilesStatus")).to_contain_text("test2.txt")

