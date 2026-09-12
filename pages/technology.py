
class technologies:
    def __init__(self,page):
        self.page = page

    # Technologies
        self.Technologies = page.locator('(//a[text()="Technologies"])[1]')
    # ecom
        self.Ecom = page.locator('//strong[text()="eCommerce Development"]')

        self.ecom1 = page.locator('//a[text()="Magento Development"]')
        self.ecom2 = page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.ecom3 = page.locator('(//a[text()="Codeigniter Development"])[1]')
        self.ecom4 = page.locator('(//a[text()="WordPress Development"])[1]')
        self.ecom5 = page.locator('(//a[text()="Big Commerce"])[1]')
        self.ecom6 = page.locator('(//a[text()="Shopify Development"])[1]')
        self.ecom7 = page.locator('(//a[text()="CS-Cart Development"])[1]')
        self.ecom8 = page.locator('(//a[text()="Node JS Development"])[1]')
        self.ecom9 = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.ecom10 = page.locator('(//a[text()="Woo Commerce"])[1]')
        self.ecom11= page.locator('(//a[text()="Laravel Development"])[1]')
        self.ecom12= page.locator('(//a[text()="Prestashop Development"])[1]')
        self.ecom13= page.locator('(//a[text()="Drupal Development"])[1]')
        self.ecom14= page.locator('(//a[text()="Wix Development"])[1]')
        self.ecom15= page.locator('(//a[text()="Joomla Development"])[1]')
        self.ecom16= page.locator('(//a[text()="React JS Development"])[1]')
        self.ecom17= page.locator('(//a[text()="Express JS Development"])[1]')

    # mobile app
        self.mobileapp = page.locator('//strong[text()="Mobile App Development"]')

        self.m1 = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.m2 = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.m3 = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.m4 = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.m5 = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.m6 = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.m7 = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.m8 = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')

    # ai

        self.AI = page.locator('//strong[normalize-space()="Artificial Intelligence"]')
        self.Ecom_list = [self.ecom1,self.ecom2,self.ecom3,self.ecom4,self.ecom5,self.ecom6,self.ecom7,self.ecom8,self.ecom9,self.ecom10,self.ecom11,self.ecom12,self.ecom13,self.ecom14,self.ecom15,self.ecom16,self.ecom17]
        self.mobileapp_list = [self.m1,self.m2,self.m3,self.m4,self.m5,self.m6,self.m7,self.m8]


    def click_Ecom_options(self):
        for i in self.Ecom_list:
            self.Technologies.hover()
            self.Ecom.hover()
            i.click()
            print("url:", self.page.url)
            self.page.go_back()
            self.page.wait_for_load_state("load")

            

    def click_mobile_app_options(self):

        for i in self.mobileapp_list:
            self.Technologies.hover()
            self.mobileapp.hover()
            i.click()
            print("url:",  self.page.url)
            self.page.go_back()
            self.page.wait_for_load_state("load")

    def click_AI_options(self):
        self.Technologies.hover()
        self.AI.hover()
        self.AI.click()
        print("url:",  self.page.url)
        self.page.go_back()
        self.page.wait_for_load_state("load")

        
        
            


