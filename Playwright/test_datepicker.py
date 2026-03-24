import pytest
from playwright.sync_api import sync_playwright,expect,Page
def select_date(page,target_year,target_month,target_day,is_future):
    while True:
        currentmonth=page.locator(".ui-datepicker-month").inner_text()
        # page.wait_for_timeout(5000)
        currentyear=page.locator(".ui-datepicker-year").inner_text()
        # page.wait_for_timeout(5000)
        if currentmonth==target_month and currentyear==target_year:
            break
        if is_future==True:

            page.locator(".ui-datepicker-next.ui-corner-all").click()
            # page.wait_for_timeout(5000)
        else:
            page.locator(".ui-datepicker-prev.ui-corner-all").click()
            # currentmonth = page.locator(".ui-datepicker-month").text_content()
            # currentyear = page.locator(".ui-datepicker-year").text_content()

    all_dates=page.locator("table tbody tr a").all()
    for date in all_dates:
        date_text=date.inner_text()
        if date_text==target_day:
            date.click()
            break




def test_datepicker(page:Page):
    page.goto("https://demo.automationtesting.in/Datepicker.html")
    date_input=page.locator("#datepicker1")
    date_input.click()
    page.wait_for_timeout(5000)
    is_future=False
    year="2022"
    month="May"
    day="25"
    select_date(page,year,month,day,is_future)
    page.wait_for_timeout(5000)
    print(date_input.input_value())








