class contacts:

    def __init__(self,page):
        self.page = page
        self.ContactUs= page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
        self.name = page.locator('(//input[@placeholder="Your Name"])[2]')
        self.email = page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.sendOTP = page.locator('(//button[text()="Send OTP"])[2]')
        self.enterOTP= page.locator('(//input[@placeholder="Enter OTP"])[2]')
        self.company = page.locator('(//input[@placeholder="Your Company"])[2]')
        self.service = page.locator('(//select[@name="service"])[2]')
        self.phone =page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.message = page.locator('(//textarea[@placeholder="Message"])[2]')
        self.submit = page.locator('(//input[@value="Submit"])[2]')

    def contact_page(self):
        self.ContactUs.click()
        
    # form
        self.name.fill("Manish S D")
        self.email.fill("manishsdhoble@gmail.com")
        self.page.once("dialog", lambda dialog : dialog.accept())
        self.sendOTP.click()
        self.enterOTP.fill("12345")
        self.company.fill("ABC")
        self.service.select_option("App Development")
        self.phone.type("9876543210")
        self.message.type("TRY TO AUTOMATE CAPTCHA FIRST THEN SUBMIT")
        # self.page.wait_for_timeout(1000)
        # self.submit.click()
        # self.page.wait_for_timeout(5000)