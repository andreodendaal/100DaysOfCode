from unittest.mock import patch
import random
import pytest

from guessing_game import get_random_number, Game

@patch.object(random, 'randint')
def test_getrandom_number(m):
    m.return_value = 17
    assert get_random_number() == 17


@patch("builtins.input", side_effect=[11, '12', 'Bob', 12, 5, -1, 21, 7, None])
def test_guess(inp):
    game = Game()
    # good
    assert game.guess() == 11
    assert game.guess() == 12
    # not number
    with pytest.raises(ValueError):
        game.guess()
    # already used
    with pytest.raises(ValueError):
        game.guess()
    # good
    assert game.guess() == 5
    # out of range
    with pytest.raises(ValueError):
        game.guess()
    with pytest.raises(ValueError):
        game.guess()
    # good
    assert game.guess() == 7
    # not number
    with pytest.raises(ValueError):
        game.guess()