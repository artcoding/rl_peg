from .context import src

def test_mirror():
    state = src.State(value=1<<4, rows=3)
    new_state = state.mirror()
    assert new_state == state

    # Mirror 101100 (1 + 4 + 8 = 13) into 110001 (1 + 2 + 32 = 35)
    state = src.State(value=13, rows=3)
    new_state = state.mirror()
    print(new_state.value)
    assert new_state == state.from_value(value=35)

    new_state = new_state.mirror()
    assert new_state == state

