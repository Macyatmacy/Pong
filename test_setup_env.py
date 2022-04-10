from setup_env import setup_env


def test_setup():
    assert setup_env() == ["NOOP", "FIRE", "RIGHT", "LEFT", "RIGHTFIRE", "LEFTFIRE"]
