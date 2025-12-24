from body import get_pos
import pytest

def test_get_pos_zero_acceleration():
    """
    If acceleration = 0, motion should continue at constant velocity.
    """
    current_pos = 10.0
    previous_pos = 5.0
    acceleration = 0.0
    dt = 1.0

    result = get_pos(current_pos, previous_pos, acceleration, dt)

    expected = 15.0

    assert result == expected


def test_get_pos_constant_acceleration():
    """
    Test basic Verlet integration with constant acceleration.
    """
    current_pos = 10.0
    previous_pos = 9.0
    acceleration = 2.0
    dt = 1.0

    result = get_pos(current_pos, previous_pos, acceleration, dt)

    expected = 13.0
 
    assert result == expected

if __name__ == "__main__":
    pytest.main(["testing.py"])