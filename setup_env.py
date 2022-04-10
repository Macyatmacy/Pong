import gym
import ale_py
import random
from ale_py import ALEInterface
from ale_py.roms import Pong

ale = ALEInterface()

ale.loadROM(Pong)
env = gym.make("ALE/Pong-v5")


def setup_env():
    return env.unwrapped.get_action_meanings()
