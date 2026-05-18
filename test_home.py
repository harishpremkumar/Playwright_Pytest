import re
from playwright.sync_api import Page, expect

def test_homepage_has_Playwright(page: Page):
    # connect to the target page
    page.goto("https://www.saucedemo.com/")

    # expect the page title "to contain" a substring.
    expect(page).to_have_title(re.compile("Swag Labs"))

    page.screenshot(full_page=True,path="Homepage.png")
    page.fill("#user-name", "Harish")
    page.type("#password", "secret_sauce")
    print(page.get_by_text(text="secret_sauce"))



