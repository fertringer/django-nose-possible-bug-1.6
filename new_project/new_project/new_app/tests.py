from django_nose import FastFixtureTestCase
from views import view_category


class TestCategory(FastFixtureTestCase):
    def test_null_category(self):
        self.assertTrue(view_category())
