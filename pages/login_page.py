from playwright.sync_api import Page
class LoginPage:
    def __init__(self,page:Page):
        self.page=page
        self.login_link=self.page.locator("#login2")
        self.username_input=self.page.locator("loginusername")
        self.password_input=self.page.locator("loginpassword")
        self.login_button=self.page.locator("btn btn-primary")
        self.close_button=self.page.locator("btn btn-secondary")

    # Actions
    def perform_login(self,username,password):
        self.login_link.click()
        # self.username_input.fill("")
        self.username_input.fill("chaithanyatest")
        # self.password_input.fill("")
        self.password_input.fill("test@123")
        self.login_button.click()
