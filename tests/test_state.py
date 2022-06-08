from .context import src

def test_mirror():
    state = src.State(value=1<<4, rows=3)
    new_state = state.mirror()
    assert new_state == state

