
# from nose.tools import assert_equals
from chai import Chai

from minimatch.balanced import balanced_match

class TestCase(Chai):

    def test_balanced_ok(self):
        self.expect(balanced_match("{", "}", "foo")).returns(None)
        self.expect(balanced_match("{", "}", "foo{bar}")).args({ start: equals(3), start_delim: equals("{") })
