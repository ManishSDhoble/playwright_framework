import pytest
from pages.portfolio import portfolios

@pytest.mark.portfolio
def test_viewmorecards(page):
    port = portfolios(page)
    port.portfolio_our_projects()

@pytest.mark.portfolio
def test_socialmedia(page):
    social = portfolios(page)
    social.socialmediapageclick()

