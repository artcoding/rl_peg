from .context import src

def test_mirror():
    state = src.State(value=1<<4, rows=3)
    new_state = state.mirror()
    assert new_state == state

    # Mirror 101100 (1 + 4 + 8 = 13) into 110001 (1 + 2 + 32 = 35)
    state = src.State(value=13, rows=3)
    new_state = state.mirror()
    assert new_state == state.from_value(value=35)

    # Mirror bakc to the original state
    new_state = new_state.mirror()
    assert new_state == state

    # Mirror 001101 (4 + 8 + 32 = 44) into 010101 (2 + 8 + 32 = 42)
    state = src.State(value=44, rows=3)
    new_state = state.mirror()
    assert new_state == state.from_value(value=42)

    # Mirror bakc to the original state
    new_state = new_state.mirror()
    assert new_state == state
