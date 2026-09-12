
class blog:
    def __init__(self,page):
        self.page = page
            
    # Blog page
        self.blog = page.locator('(//a[text()="Blog"])[1]')
        # self.blog.click()
    # # # Horizontal clicks
        self.HB1 = page.locator('(//a[text()="App Development"])[1]')
        self.HB2 = page.locator('(//a[text()="Web Development"])[1]')
        self.HB3 =  page.locator('(//a[text()="Software Development"])[1]')
        self.HB4 =  page.locator('(//a[text()="Digital Marketing"])[1]')
        self.HB5 = page.locator('(//a[text()="Email Marketing"])[1]')
        self.HB6 = page.locator('(//a[text()="Artificial Intelligence"])[2]')
        self.HB7 = page.locator('(//a[text()="UI UX Design"])[1]')

        self.horizontal_links = [self.HB1,self.HB2,self.HB3,self.HB4,self.HB5,self.HB6,self.HB7]

    # Categories
        self.Categ1 =  page.locator('(//a[text()="App Development"])[3]')
        self.Categ2 = page.locator('(//a[text()="Artificial Intelligence"])[3]')
        self.Categ3 = page.locator('(//a[text()="Content Marketing"])')
        self.Categ4 = page.locator('(//a[text()="CRM Development"])[3]')
        self.Categ5 = page.locator('(//a[text()="Digital Marketing"])[2]')
        self.Categ6 = page.locator('(//a[text()="ECommerce Development"])[5]')
        self.Categ7 = page.locator('(//a[text()="Email Marketing"])[2]')
        self.Categ8 = page.locator('(//a[text()="Graphic Design"])[3]')
        self.Categ9 = page.locator('(//a[text()="Software & IT Company"])')
        self.Categ10 = page.locator('(//a[text()="Software Development"])[2]')
        self.Categ11 = page.locator('(//a[text()="UI UX Design"])[6]')
        self.Categ12 = page.locator('(//a[text()="Web Development"])[6]')

        self.categories_list = [self.Categ1,self.Categ2,self.Categ3,self.Categ4,self.Categ5,self.Categ6,self.Categ7,self.Categ8,self.Categ9,self.Categ10,self.Categ11,self.Categ12]
 
    # LINKS
    
        self.webdev = page.locator('(//a[text()="Web Development"])[7]')
        self.webdev1 = page.locator('(//a[@href="/cms-website-development-company-in-india"])')
        self.webdev2 = page.locator('//a[@href="/ecommerce-web-development-company-in-india"]')
        self.t1 = page.locator('(//span[@class="toggle-btn"])[1]')
        self.webdev21 = page.locator('//a[@href="/website-development-company-in-delhi-ncr"]')
        self.t2= page.locator('(//span[@class="toggle-btn"])[2]')
        self.webdev3 = page.locator('//a[@href="/custom-web-portal-development-company-in-india"]')
    
        self.appdev = page.locator('(//a[text()="App Development"])[4]')
        self.appdev1= page.locator('//a[@href="/ios-mobile-app-development-company-in-india"]')
        self.appdev2 = page.locator('//a[@href="/android-mobile-app-development-company-in-india"]')
    
        self.appdev21 = page.locator('//a[@href="/android-app-development-company-in-delhi-ncr"]')
        self.appdev22 = page.locator('//a[@href="/app-development-company-in-delhi-ncr"]')
    
    
        self.appdev3 = page.locator('//a[@href="/hybrid-mobile-app-development-company-in-india"]')
        self.appdev4 = page.locator('//a[@href="/cross-platform-mobile-app-development-company-in-india"]')
        self.appdev5 = page.locator('//a[@href="/progressive-web-app-development-company-in-india"]')
    
    
        self.graphicsdev = page.locator('//a[@href="/graphic-design-company-in-india"]')
        self.graphicsdev1  = page.locator('//a[@href="/logo-design-company-in-india"]')
        self.graphicsdev2 = page.locator('//a[@href="/banner-design-company-in-india"]')
        self.graphicsdev3 = page.locator('//a[@href="/packaging-design-company-in-india"]')
        self.graphicsdev4 = page.locator('//a[@href="/business-cards-design-company-in-india"]')
    
        self.UIUXDEV = page.locator('//a[@href="/ui-ux-design-company-in-india"]')
        self.UIUXDEV1 = page.locator('//a[@href="/mobile-app-design-company-in-india"]')
        self.UIUXDEV2 = page.locator('//a[@href="/responsive-web-design-company-in-india"]')
        self.UIUXDEV3 = page.locator('//a[@href="/brand-identity-design-services-company-in-india"]')
    
    
        self.porfolio = page.locator('(//a[@href="#"])[10]')
        self.porfolio1 = page.locator('//a[@href="/assets/trank-profile.pdf"]')
    
        self.links = [self.webdev,self.webdev1,self.webdev2,self.webdev3,self.appdev,self.appdev1,self.appdev2,self.appdev3,self.appdev4,self.appdev5,self.graphicsdev,self.graphicsdev1,self.graphicsdev2,self.graphicsdev3,self.graphicsdev4,self.UIUXDEV,self.UIUXDEV1,self.UIUXDEV2,self.UIUXDEV3]
    
    def blog_horizontal_links(self):
        self.blog.click()
        for i in self.horizontal_links:
            i.click()
            print("url:",  self.page.url)
            self.page.go_back()
            self.page.wait_for_load_state("load")
    
    def blog_categories(self):
        for i in self.categories_list:
            i.click()
            self.page.go_back()
            print("url:",  self.page.url)  
            self.page.wait_for_load_state("load")

    def blog_links(self):
        for i in self.links:
            i.click()
            print("url:",  self.page.url)
            self.pagepage.go_back()
            self.page.wait_for_load_state("load")

    
