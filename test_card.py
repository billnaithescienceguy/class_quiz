import unittest
from card import Card
Sofia
class TestCard(unittest.TestCase):

    def test_value(self):
        sample = Card(3, "Cups")
        self.assertEqual(sample.value, 3)

    def test_suit(self):
        sample = Card(3, "Cups")
        self.assertEqual(sample.suit, "Cups")

    def test_repr(self):
        sample = Card(3, "Cups")
        expected = "Card(value=3,suit=Cups)"
        output = repr(sample).replace(' ','').replace('\'', '').replace('"', '')
        self.assertEqual(output, expected)

    def test_str(self):
        sample = Card(3, "Cups")
        self.assertEqual(str(sample), "3 of Cups")

    def test_eq(self):
        sample = Card(3, "Cups")
        other_sample = Card(3, "Swords")
        self.assertTrue(sample == other_sample)

if __name__ == '__main__':
    unittest.main()

def __init__(self value, "suit"):
    self.suit = cups
    self.values=Card(3, "Cups")

def __repr__(self):
    suit= Card(3, cups)
    suit="Card(value=3, suit=cups)"
    cards= repr(suit).replace('value','suit').replace('cups','3').replace("suit","x")
    self.suit(cards,suit)

def __str__(self):
    self.suit=card(3,"cups")
    self.suit(str(suit), "3 of cups")

def __eq__(self):
    return f"(self.x, sef.suit ==  other_3 of cups)"True
