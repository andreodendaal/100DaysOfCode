from unittest.mock import patch
import random

from guessing_game import get_random_number, Game

@patch.object(random, 'randint')
def test_getrandom_number(m):
    m.return_value = 17
    assert get_random_number() == 17