from .context import src


def test_mirror():
    src.State.rows = 3
    state = src.State(value=1 << 4)
    new_state = state.mirror()
    assert new_state == state

    # Mirror 101100 (1 + 4 + 8 = 13) into 110001 (1 + 2 + 32 = 35)
    state = src.State(value=13)
    new_state = state.mirror()
    assert new_state == src.State(value=35)

    # Mirror back to the original state
    new_state = new_state.mirror()
    assert new_state == state

    # Mirror 001101 (4 + 8 + 32 = 44) into 010101 (2 + 8 + 32 = 42)
    state = src.State(value=44)
    new_state = state.mirror()
    assert new_state == src.State(value=42)

    # Mirror back to the original state
    new_state = new_state.mirror()
    assert new_state == state


def test_rotate():
    src.State.rows = 3
    state = src.State(value=1 << 4)
    new_state = state.rotate()
    assert new_state == src.State(value=2)

    # Rotate 101100 (1 + 4 + 8 = 13) into 100011 (1 + 16 + 32 = 49)
    state = src.State(value=13)
    new_state = state.rotate()
    assert new_state == src.State(value=49)

    # Rotate standard-size game
    src.State.rows = 5
    state = src.State(value=1 << 4)
    new_state = state.rotate()
    assert new_state == src.State(value=1 << 8)


def test_find_moves():
    src.State.rows = 3
    state = src.State(value=(1 << 4) + (1 << 2))
    assert len(src.find_moves(state)) == 0

    state = src.State(value=(1 << 4) + (1 << 5))
    assert src.find_moves(state) == {src.Action.from_int(1 << 3)}

    src.State.rows = 5
    state = src.State(value=(1 << 15) - 2 - (1 << 3))
    correct_moves = {src.Action.from_int(28542), src.Action.from_int(31678),
                     src.Action.from_int(32723), src.Action.from_int(32718)}
    assert src.find_moves(state) == correct_moves
