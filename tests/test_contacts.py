import pytest
from pages.contacts import contacts

@pytest.mark.contacts
def test_contact(page):
    con = contacts(page)
    con.contact_page()