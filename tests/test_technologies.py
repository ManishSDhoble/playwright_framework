
import pytest
from pages.technology import technologies

@pytest.mark.technology
def test_ecom(page):
    ecom = technologies(page)
    ecom.click_Ecom_options()

@pytest.mark.technology
def test_mobileapp(page):
    mobile = technologies(page)
    mobile.click_mobile_app_options()

@pytest.mark.technology
def test_ai(page):
    i = technologies(page)
    i.click_AI_options()




