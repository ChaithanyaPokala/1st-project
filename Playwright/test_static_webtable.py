import pytest
from playwright.sync_api import sync_playwright,expect,Page
def test_static_webtable(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    table=page.locator("table[name='courses'] tbody")
    expect(table).to_be_visible()
    # to capture all the rows
    rows=table.locator('tr')
    row_count=rows.count()
    print("row_count",row_count)
    row_text=rows.all_inner_texts()
    print("row_text",row_text)
    #to capture all the columns headers
    headers=rows.locator('th')
    header_count=headers.count()
    print("header_count",header_count)
    header_text=headers.all_inner_texts()
    print("header_text",header_text)
    #to capture particular row
    particular_row=rows.nth(4).locator('td')
    particular_row_text=particular_row.all_inner_texts()
    print("particular_row_text",particular_row_text)
    expect(particular_row).to_have_text(['Rahul Shetty', 'WebSecurity Testing for Beginners-QA knowledge to next level', '20'])
    #to capture all the data in the table
    all_table_data=rows.all()
    for data in all_table_data[1:]:
        all_data=data.locator('td')
        all_data_text=all_data.all_inner_texts()
        print("all_data_text",all_data_text)
        for data in all_data_text:
            print(data)
    print("condition applied")
    for data in all_table_data[1:]:
        price=data.locator('td').nth(2).inner_text()
        if price==25:
            print(data.locator('td').nth(1).inner_text())


