


import pytest
from pages.vertical import verticals

@pytest.mark.vertical
def test_trading(page):
    trade = verticals(page)
    trade.click_trading_options()

@pytest.mark.vertical
def test_Retail_Ecommerce(page):
    retail = verticals(page)
    retail.click_Retail_Ecommerce_options()

@pytest.mark.vertical
def test_Healthcare(page):
    health = verticals(page)
    health.click_Healthcare_options()

@pytest.mark.vertical
def test_Fintech(page):
    fint = verticals(page)
    fint.click_Fintech_option()


    
    
   
