from .context import src


def test_mirror():
    state = src.State(value=1 << 4, rows=3)
    new_state = state.mirror()
    assert new_state == state

    # Mirror 101100 (1 + 4 + 8 = 13) into 110001 (1 + 2 + 32 = 35)
    state = src.State(value=13, rows=3)
    new_state = state.mirror()
    assert new_state == state.from_value(value=35)

    # Mirror back to the original state
    new_state = new_state.mirror()
    assert new_state == state

    # Mirror 001101 (4 + 8 + 32 = 44) into 010101 (2 + 8 + 32 = 42)
    state = src.State(value=44, rows=3)
    new_state = state.mirror()
    assert new_state == state.from_value(value=42)

    # Mirror back to the original state
    new_state = new_state.mirror()
    assert new_state == state


def test_rotate():
    state = src.State(value=1 << 4, rows=3)
    new_state = state.rotate()
    assert new_state == state.from_value(value=2)

    # Rotate 101100 (1 + 4 + 8 = 13) into 100011 (1 + 16 + 32 = 49)
    state = src.State(value=13, rows=3)
    new_state = state.rotate()
    assert new_state == state.from_value(value=49)

    # Rotate standard-size game
    state = src.State(value=1 << 4, rows=5)
    new_state = state.rotate()
    assert new_state == state.from_value(value=1 << 8)
