from .context import src


def test_mirror():
    src.Action.rows = 3
    action = src.Action(move_from=5, kill=4, move_to=3)
    new_action = action.mirror()
    assert new_action == src.Action(move_from=3, kill=4, move_to=5)

    src.Action.rows = 5
    action = src.Action(4, 8, 13)
    new_action = action.mirror()
    assert new_action == src.Action(4, 7, 11)

    # Mirror back to the original state
    new_action = new_action.mirror()
    assert new_action == action


def test_rotate():
    src.Action.rows = 4
    action = src.Action(move_from=5, kill=4, move_to=3)
    new_action = action.rotate()
    assert new_action == src.Action(move_from=7, kill=4, move_to=2)

    src.Action.rows = 5
    action = src.Action(4, 8, 13)
    new_action = action.rotate()
    assert new_action == src.Action(8, 7, 6)
