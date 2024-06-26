import unittest
from Movie import Movie
class Test(unittest.TestCase):
    def test_create(self):
        m = Movie("Avengers", "2010")
        self.assertEqual(m.get__title(),"Avengers")
        self.assertEqual(m.get__year(), "2010")
        n = Movie(" Infinity war", "2017")
        self.assertEqual(n.get__title(),"Infinity war")
        self.assertEqual(n.get__year(), "2017")
        try:
            assert False
        except ValueError:
            assert True