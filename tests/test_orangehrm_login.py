import allure
import pytest
from playwright.sync_api import Page, expect
from utils.screenshots import screenshot_step

from tests.helpers import (
    open_login_page,
    enter_username,
    enter_password,
    click_login,
)



@allure.feature("Authentication")
@allure.title("Verify successful OrangeHRM login")
@allure.description(
    "Verify that a user can log in with valid credentials "
    "and reach the dashboard."
)

@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke", "login", "regression")

@pytest.mark.parametrize(
    "username, password, should_login",
    [
        pytest.param(
            "Admin",
            "admin123",
            True,
            id="valid-credentials",
        ),
        pytest.param(
            "Admin",
            "wrong-password",
            False,
            id="invalid-password",
        ),
    ],
)

def test_login_scenarios(page, username, password, should_login):

    open_login_page(page)
    screenshot_step(page, "Step 1 - Open Orange HRM Site")

    enter_username(page, username)
    screenshot_step(page, "Step 2 - Enter Username")

    enter_password(page, password)
    screenshot_step(page, "Step 3 - Password")


    click_login(page)
    # screenshot_step(page, "Step 4 - login clicked")

    if should_login:
        with allure.step("Verify successful login"):
            expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index",timeout=15000)

    else:
        with allure.step("Verify unsuccessful login"):
            expect(page.get_by_role("alert")).to_contain_text(
                "Invalid credentials", timeout=20000
            )
#     # assert False, "Testing automatic failure screenshot"