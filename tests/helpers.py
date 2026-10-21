import allure


@allure.step("Open login page")
def open_login_page(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@allure.step("Enter username: {username}")
def enter_username(page, username):
    page.get_by_placeholder("Username").fill(username)

@allure.step("Enter password")
def enter_password(page, password):
    page.get_by_placeholder("Password").fill(password)

@allure.step("Click Login button")
def click_login(page):
    page.get_by_role("button", name="Login").click()
