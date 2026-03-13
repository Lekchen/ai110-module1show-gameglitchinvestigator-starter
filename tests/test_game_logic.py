import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"


def test_check_guess_returns_too_high_when_guess_greater_than_secret():
    # Test that check_guess returns "Too High" when guess > secret
    result = check_guess(75, 50)
    assert result[0] == "Too High"
