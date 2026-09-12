class verticals:
    def __init__(self,page):
        self.page = page

        # Verticals
        self.vertical = page.locator('(//a[text()="Verticals"])[1]')

        # Trading
        self.Trading =  page.locator('//strong[text()="Trading"]')
        
        self.trade1 = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.trade2 =page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.trade3 = page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.trade4 = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.trade5 = page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.trade6 = page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.trade7 = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')

        self.Trading_list = [self.trade1,self.trade2,self.trade3,self.trade4,self.trade5,self.trade6,self.trade7]

        # Retail_Ecommerce
        self.Retail_Ecommerce = page.locator('//strong[text()="Retail and Ecommerce"]')

        self.RE1 = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        self.RE2 = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

        self.Retail_Ecommerce_list = [self.RE1, self.RE2]

        # Healthcare
        self.Healthcare = page.locator('//strong[text()="Healthcare"]')

        self.H1 = page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.H2 = page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

        self.Healthcare_list = [self.H1 , self.H2]

        # Fintech
        self.Fintech = page.locator('(//strong[text()="Fintech"])')

        self.f1 = page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.f2 = page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

        self.Fintech_list = [self.f1,self.f2]

        # custom
        self.custom = page.locator('//strong[text()="Custom App"]')

        self.c1 = page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.c2 = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.c3 =page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.c4 = page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.c5 = page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.c6 = page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.c7 = page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.c8 = page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        self.c9 = page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')

        self.custom_list = [self.c1,self.c2,self.c3,self.c4,self.c5,self.c6,self.c7,self.c8,self.c9]

    def click_trading_options(self):
        for i in self.Trading_list:
            self.vertical.hover()
            self.Trading.hover()
            i.click()
            print("url:", self.page.url)
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def click_Retail_Ecommerce_options(self):
        for i in self.Retail_Ecommerce_list:
            self.vertical.hover()
            self.Retail_Ecommerce.hover()
            i.click()
            print("url:", self.page.url)
            self.page.go_back()
            self.page.wait_for_load_state("load")

            
            # self.page.go_back()
    def click_Fintech_option(self):
        for i in self.Fintech_list:
            self.vertical.hover()
            self.Fintech.hover()
            i.click()
            print("url:", self.page.url)
            self.page.wait_for_load_state("load")
            self.page.go_back()


    def click_Healthcare_options(self):
        for i in self.Healthcare_list:
            self.vertical.hover()
            self.Healthcare.hover()
            i.click()
            print("url:", self.page.url)
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def click_custom_options(self):
        for i in self.click_custom_options:
            self.vertical.hover()
            self.custom.hover()
            i.click()
            print("url:", self.page.url)
            self.page.wait_for_load_state("load")
            self.page.go_back()



