import allure
from playwright.sync_api import Page, expect


# def screenshot_step(page, name):
#     with allure.step(name):
#         page.wait_for_load_state("domcontentloaded",timeout=5000)
#         page.locator("body").wait_for(state="visible")
#         screenshot = page.screenshot(full_page=True)

#         allure.attach(
#             screenshot,
#             name=name,
#             attachment_type=allure.attachment_type.PNG,
#         )



def screenshot_step(page: Page, name: str):
    with allure.step(name):
        expect(
            page.get_by_placeholder("Username")
        ).to_be_visible(timeout=15000)
        screenshot = page.screenshot(full_page=True)

        allure.attach(
            screenshot,
            name=name,
            attachment_type=allure.attachment_type.PNG,
        )
