import json
from pathlib import Path
import allure
import pytest
from playwright.sync_api import Page, expect

from tests.helpers import (
    open_login_page,
    enter_username,
    enter_password,
    click_login,
)

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

@allure.feature("Authentication")
@allure.title("Verify successful OrangeHRM login")
@allure.description(
    "Verify that a user can log in with valid credentials "
    "and reach the dashboard."
)

@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke", "login", "regression")


def test_login_scenarios(page, username, password, should_login):

    open_login_page(page)
    enter_username(page, username)
    enter_password(page, password)
    click_login(page)

    if should_login:
        with allure.step("Verify successful login"):
            expect(page).to_have_url(
                "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
            )
    else:
        with allure.step("Verify unsuccessful login"):
            expect(page.get_by_text("Invalid credentials")).to_be_visible()
# def test_orangehrm_login(page):
#     open_login_page(page)

#     enter_username(page, "Admin")
#     enter_password(page, "admin123")
#     click_login(page)

#     with allure.step("Verify dashboard URL"):
#         expect(page).to_have_url(
#             "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
#         )

#     with allure.step("Verify dashboard heading"):
#         expect(
#             page.get_by_role("heading", name="Dashboard")
#         ).to_be_visible()
#     # expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index",timeout=15000)

#     # assert False, "Testing automatic failure screenshot"