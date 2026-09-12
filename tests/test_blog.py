

import pytest

from pages.blog import blog

@pytest.mark.blogs
def test_blog(page):
    blogs = blog(page)
    blogs.blog_horizontal_links()
    blogs.blog_categories()
    blogs.blog_links