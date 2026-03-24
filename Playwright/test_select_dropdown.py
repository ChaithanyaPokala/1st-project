import pytest
from playwright.sync_api import sync_playwright,Page,expect
def test_verify_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("#country").select_option("germany")
    page.wait_for_timeout(2000)
    page.locator("#colors").select_option(index=[1,2,3])
    # page.locator("#colors").select_option(value=["red","blue","green"])
    page.locator("#colors").select_option(["Red","Blue","Green"])
    drop_down=page.locator("#country option")
    drop_down.count()
    print(drop_down.count())
    dp=page.locator("#colors option") #unsorted
    # dp=page.locator("#animals option") #sorted
    options_text=[text.strip() for text in dp.all_text_contents()]
    print(options_text)
    for text in options_text:
        print(text)
    orginal_list=options_text.copy()
    sorted_list=sorted(options_text)
    print(sorted_list)
    if orginal_list==sorted_list:
        print("ORIGINAL LIST AND SORTED")
    else:
        print("ORIGINAL LIST AND NOT SORTED")
