import gym
import ale_py
import random
from ale_py import ALEInterface
from ale_py.roms import Pong
import matplotlib.pyplot as plt

ale = ALEInterface()

ale.loadROM(Pong)
env = gym.make("ALE/Pong-v5")
# env = gym.make('ALE/Pong-v5', render_mode='human')


first_frame = env.reset()
plt.imshow(first_frame)

for i in range(1000):
    a = random.sample(list(range(5)), 1)[0]
    next_frame, next_frames_reward, next_state_terminal, info = env.step(a)
    plt.imshow(next_frame)
    if next_state_terminal:
        env.reset()
