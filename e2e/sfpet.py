from playwright.sync_api import Page, sync_playwright

def test_spef(page: Page):
    page.goto('https://sfpet.bmgf.io/')
    page.locator('#onetrust-accept-btn-handler').click()
    page.wait_for_load_state('domcontentloaded')
    page.locator('#chart1').hover()
    page.locator('#chart2').hover()
    page.evaluate('window.scrollBy(0, 1200)')
    page.locator('#chart80').hover()

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    test_spef(page)
    browser.close()

